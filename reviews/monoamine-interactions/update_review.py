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
    args = parser.parse_args()

    update_review(dry_run=args.dry_run, since_date=args.since, min_citations=args.min_citations)


if __name__ == "__main__":
    main()
