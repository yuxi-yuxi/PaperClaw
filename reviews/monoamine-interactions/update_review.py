#!/usr/bin/env python3
"""
Living Review Updater for Monoamine Interactions Review

This script checks for new papers on Semantic Scholar and updates the living review.
Run periodically (e.g., weekly) to keep the review current.

Usage:
    python update_review.py [--dry-run] [--since YYYY-MM-DD]
"""

import json
import os
import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv(Path(__file__).parent.parent.parent / ".env")

SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
REVIEW_FILE = Path(__file__).parent / "review.json"
S2_API_BASE = "https://api.semanticscholar.org/graph/v1"


def load_review():
    """Load the current review JSON."""
    with open(REVIEW_FILE, "r") as f:
        return json.load(f)


def save_review(review_data):
    """Save the review JSON."""
    with open(REVIEW_FILE, "w") as f:
        json.dump(review_data, f, indent=2)


def get_existing_dois(review_data):
    """Get set of DOIs already in the review."""
    return {p.get("doi", "").lower() for p in review_data["papers"] if p.get("doi")}


def search_semantic_scholar(query, year_from=None, limit=50):
    """Search Semantic Scholar for papers matching query."""
    headers = {"x-api-key": SEMANTIC_SCHOLAR_API_KEY} if SEMANTIC_SCHOLAR_API_KEY else {}

    params = {
        "query": query,
        "limit": limit,
        "fields": "paperId,title,authors,year,citationCount,externalIds,abstract,publicationDate",
    }

    if year_from:
        params["year"] = f"{year_from}-"

    try:
        response = requests.get(
            f"{S2_API_BASE}/paper/search",
            headers=headers,
            params=params,
            timeout=30
        )
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.RequestException as e:
        print(f"Error searching Semantic Scholar: {e}")
        return []


def filter_new_papers(papers, existing_dois, min_citations=0):
    """Filter papers to only include new, relevant ones."""
    new_papers = []

    for paper in papers:
        doi = paper.get("externalIds", {}).get("DOI", "")
        if not doi:
            continue

        if doi.lower() in existing_dois:
            continue

        citations = paper.get("citationCount", 0) or 0
        if citations < min_citations:
            continue

        new_papers.append({
            "paperId": paper.get("paperId"),
            "doi": doi,
            "title": paper.get("title"),
            "authors": [a.get("name", "") for a in paper.get("authors", [])[:3]],
            "year": paper.get("year"),
            "citations": citations,
            "abstract": paper.get("abstract", "")[:500] if paper.get("abstract") else "",
            "publication_date": paper.get("publicationDate"),
        })

    # Sort by citations (descending)
    return sorted(new_papers, key=lambda x: x["citations"], reverse=True)


def format_paper_for_review(paper, added_by="auto"):
    """Format a paper dict for the review JSON."""
    year = paper.get("year", datetime.now().year)
    first_author = paper["authors"][0].split()[-1].lower() if paper["authors"] else "unknown"

    return {
        "id": f"{first_author}{year}",
        "doi": paper["doi"],
        "title": paper["title"],
        "authors": paper["authors"] + (["et al."] if len(paper["authors"]) >= 3 else []),
        "year": year,
        "citations": paper["citations"],
        "added_by": added_by,
        "added_date": datetime.now().strftime("%Y-%m-%d"),
        "tags": ["recent", "auto-discovered"],
        "category": "Recent Advances (2022-2026)",
        "key_claims": [],
        "notes": f"Auto-discovered. Abstract: {paper['abstract'][:200]}..." if paper["abstract"] else "Auto-discovered. Review for relevance.",
        "needs_review": True
    }


def normalize_title(title):
    """Normalize title for comparison: lowercase, remove punctuation, extra spaces."""
    import re
    title = title.lower()
    title = re.sub(r'[^\w\s]', '', title)  # Remove punctuation
    title = re.sub(r'\s+', ' ', title).strip()  # Normalize whitespace
    return title


def title_similarity(title1, title2):
    """Calculate word overlap ratio between two titles."""
    words1 = set(normalize_title(title1).split())
    words2 = set(normalize_title(title2).split())
    if not words1 or not words2:
        return 0.0
    intersection = words1 & words2
    union = words1 | words2
    return len(intersection) / len(union)


def verify_doi(doi, expected_title, strict=True):
    """
    Verify a DOI resolves to the expected paper.

    Uses word overlap similarity (Jaccard index) for robust matching.
    Requires >50% word overlap to consider a match.
    """
    headers = {"x-api-key": SEMANTIC_SCHOLAR_API_KEY} if SEMANTIC_SCHOLAR_API_KEY else {}

    try:
        response = requests.get(
            f"{S2_API_BASE}/paper/DOI:{doi}",
            headers=headers,
            params={"fields": "title,authors,year"},
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            actual_title = data.get("title", "")

            # Use word overlap similarity instead of prefix matching
            similarity = title_similarity(expected_title, actual_title)

            # Require >50% word overlap for a match
            if similarity > 0.5:
                return True, actual_title, None
            else:
                return False, actual_title, f"Title mismatch (similarity: {similarity:.0%})"
        elif response.status_code == 404:
            return False, None, "DOI not found"
        elif response.status_code == 429:
            return False, None, "Rate limited (429) - retry later"
        else:
            return False, None, f"API error: {response.status_code}"
    except Exception as e:
        return False, None, str(e)


def verify_all_dois(review_data):
    """Verify all DOIs in the review."""
    print("=" * 60)
    print("DOI Verification")
    print("=" * 60)

    papers = review_data.get("papers", [])
    errors = []
    verified = 0

    for i, paper in enumerate(papers):
        doi = paper.get("doi", "")
        title = paper.get("title", "")
        paper_id = paper.get("id", f"paper_{i}")

        if not doi:
            print(f"  SKIP: {paper_id} - No DOI")
            continue

        is_valid, actual_title, error = verify_doi(doi, title)

        if is_valid:
            print(f"  OK: {paper_id}")
            verified += 1
        else:
            print(f"  ERROR: {paper_id}")
            print(f"       DOI: {doi}")
            print(f"       Expected: {title[:50]}...")
            if actual_title:
                print(f"       Got: {actual_title[:50]}...")
            if error:
                print(f"       Reason: {error}")
            errors.append({
                "id": paper_id,
                "doi": doi,
                "expected_title": title,
                "actual_title": actual_title,
                "error": error
            })

        # Rate limiting
        import time
        time.sleep(0.5)

    print(f"\n{'=' * 60}")
    print(f"Verified: {verified}/{len(papers)}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\nPapers with DOI issues:")
        for e in errors:
            print(f"  - {e['id']}: {e['error']}")

    return errors


def update_review(dry_run=False, since_date=None, min_citations=5):
    """Main update function."""
    print("=" * 60)
    print("Living Review Updater - Monoamine Interactions")
    print("=" * 60)

    review = load_review()
    existing_dois = get_existing_dois(review)
    print(f"\nCurrent papers in review: {len(review['papers'])}")

    # Determine date range
    if since_date:
        year_from = int(since_date[:4])
    else:
        # Default: search from last update year
        last_update = review.get("meta", {}).get("last_updated", "2024-01-01")
        year_from = int(last_update[:4])

    print(f"Searching for papers from {year_from} onwards...")

    # Search using configured queries
    all_new_papers = []
    queries = review.get("meta", {}).get("search_queries", [])

    for query in queries:
        print(f"\n  Searching: '{query}'...")
        papers = search_semantic_scholar(query, year_from=year_from, limit=30)
        new_papers = filter_new_papers(papers, existing_dois, min_citations=min_citations)
        print(f"    Found {len(new_papers)} new papers (>= {min_citations} citations)")
        all_new_papers.extend(new_papers)

    # Deduplicate by DOI
    seen_dois = set()
    unique_new_papers = []
    for paper in all_new_papers:
        doi = paper["doi"].lower()
        if doi not in seen_dois:
            seen_dois.add(doi)
            unique_new_papers.append(paper)

    # Sort by citations
    unique_new_papers.sort(key=lambda x: x["citations"], reverse=True)

    print(f"\n{'=' * 60}")
    print(f"Total unique new papers found: {len(unique_new_papers)}")

    if not unique_new_papers:
        print("No new papers to add. Review is up to date!")
        return

    print("\nTop new papers:")
    for i, paper in enumerate(unique_new_papers[:10], 1):
        print(f"  {i}. [{paper['citations']} cites] {paper['title'][:60]}...")
        print(f"     DOI: {paper['doi']}")

    if dry_run:
        print("\n[DRY RUN] No changes made. Run without --dry-run to update.")
        return

    # Add papers to review
    papers_to_add = unique_new_papers[:10]  # Add top 10 by default
    for paper in papers_to_add:
        formatted = format_paper_for_review(paper)
        review["papers"].append(formatted)

    # Update metadata
    review["meta"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    review["meta"]["version"] = review["meta"].get("version", 1) + 1

    # Add update history entry
    review["update_history"].append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "action": "auto_update",
        "description": f"Added {len(papers_to_add)} new papers from Semantic Scholar search",
        "papers_added": len(papers_to_add),
        "papers_removed": 0
    })

    save_review(review)
    print(f"\n✓ Added {len(papers_to_add)} papers to the review.")
    print(f"✓ Review updated to version {review['meta']['version']}")
    print(f"\nNote: New papers are marked with 'needs_review: true'.")
    print("Run 'python generate_report.py' to regenerate the HTML report.")


def main():
    parser = argparse.ArgumentParser(description="Update the living literature review")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be added without making changes")
    parser.add_argument("--since", type=str, help="Search for papers since this date (YYYY-MM-DD)")
    parser.add_argument("--min-citations", type=int, default=5, help="Minimum citations for inclusion (default: 5)")
    parser.add_argument("--verify", action="store_true", help="Verify all DOIs in the review are correct")
    args = parser.parse_args()

    if args.verify:
        review = load_review()
        verify_all_dois(review)
    else:
        update_review(dry_run=args.dry_run, since_date=args.since, min_citations=args.min_citations)


if __name__ == "__main__":
    main()
