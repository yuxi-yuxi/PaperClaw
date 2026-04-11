#!/usr/bin/env python3
"""
Generate HTML Report from Living Review JSON

This script reads the review.json and generates a styled HTML report
following the Apple-inspired design system in DESIGN.md.

Usage:
    python generate_report.py [--output OUTPUT_PATH]
"""

import json
import argparse
from datetime import datetime
from pathlib import Path
from collections import defaultdict

REVIEW_FILE = Path(__file__).parent / "review.json"
DEFAULT_OUTPUT = Path(__file__).parent.parent.parent / "literature_review_monoamine_interactions.html"


def load_review():
    """Load the review JSON."""
    with open(REVIEW_FILE, "r") as f:
        return json.load(f)


def group_papers_by_category(papers):
    """Group papers by their category."""
    grouped = defaultdict(list)
    for paper in papers:
        category = paper.get("category", "Uncategorized")
        grouped[category].append(paper)
    return dict(grouped)


def generate_paper_card(paper):
    """Generate HTML for a single paper card."""
    doi_url = f"https://doi.org/{paper['doi']}" if paper.get('doi') else "#"
    authors = ", ".join(paper.get("authors", []))
    tags_html = "".join([
        f'<span class="tag">{tag}</span>'
        for tag in paper.get("tags", [])
    ])
    needs_review = paper.get("needs_review", False)
    review_badge = '<span class="tag needs-review">Needs Review</span>' if needs_review else ""

    return f'''
    <div class="paper-card">
        <div class="paper-header">
            <a href="{doi_url}" target="_blank" class="paper-title">{paper.get("title", "Untitled")}</a>
            <span class="citation-count">{paper.get("citations", 0)} citations</span>
        </div>
        <div class="paper-meta">
            <span class="authors">{authors}</span>
            <span class="year">({paper.get("year", "N/A")})</span>
        </div>
        <div class="paper-tags">{tags_html}{review_badge}</div>
        <div class="paper-claims">
            {"".join([f'<p class="claim">• {claim}</p>' for claim in paper.get("key_claims", [])])}
        </div>
    </div>
    '''


def generate_update_history(history):
    """Generate HTML for update history section."""
    rows = ""
    for entry in reversed(history[-10:]):  # Show last 10 updates
        rows += f'''
        <tr>
            <td>{entry.get("date", "")}</td>
            <td>{entry.get("action", "")}</td>
            <td>{entry.get("description", "")}</td>
            <td>+{entry.get("papers_added", 0)} / -{entry.get("papers_removed", 0)}</td>
        </tr>
        '''
    return rows


def generate_html(review):
    """Generate the full HTML report."""
    meta = review.get("meta", {})
    papers = review.get("papers", [])
    history = review.get("update_history", [])

    grouped = group_papers_by_category(papers)

    # Generate paper sections
    paper_sections = ""
    category_order = [
        "Highly Cited Foundational Papers",
        "Key Mechanistic Papers",
        "Recent Advances (2022-2026)",
        "Uncategorized"
    ]

    for category in category_order:
        if category not in grouped:
            continue
        papers_in_cat = grouped[category]
        paper_cards = "".join([generate_paper_card(p) for p in papers_in_cat])
        paper_sections += f'''
        <section class="paper-section">
            <h2>{category}</h2>
            <div class="paper-grid">
                {paper_cards}
            </div>
        </section>
        '''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{meta.get("title", "Literature Review")}</title>
    <style>
        :root {{
            --black: #000000;
            --white: #ffffff;
            --gray-light: #f5f5f7;
            --gray-dark: #1d1d1f;
            --blue: #0071e3;
            --text-primary: #1d1d1f;
            --text-secondary: #86868b;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', Roboto, sans-serif;
            line-height: 1.47;
            color: var(--text-primary);
            background: var(--white);
        }}

        .container {{
            max-width: 980px;
            margin: 0 auto;
            padding: 0 22px;
        }}

        /* Hero Section */
        .hero {{
            background: var(--black);
            color: var(--white);
            padding: 80px 0;
            text-align: center;
        }}

        .hero h1 {{
            font-size: 48px;
            font-weight: 600;
            line-height: 1.07;
            letter-spacing: -0.5px;
            margin-bottom: 20px;
        }}

        .hero .meta {{
            display: flex;
            justify-content: center;
            gap: 16px;
            flex-wrap: wrap;
        }}

        .meta-pill {{
            background: rgba(255,255,255,0.1);
            padding: 8px 16px;
            border-radius: 980px;
            font-size: 14px;
            color: var(--text-secondary);
        }}

        .meta-pill strong {{
            color: var(--white);
        }}

        .living-badge {{
            background: var(--blue);
            color: var(--white);
            padding: 6px 14px;
            border-radius: 980px;
            font-size: 12px;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            margin-top: 24px;
        }}

        .living-badge::before {{
            content: "●";
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}

        /* Key Finding */
        .key-finding {{
            background: var(--gray-light);
            padding: 60px 0;
        }}

        .finding-card {{
            background: var(--white);
            padding: 40px;
            border-radius: 18px;
            box-shadow: 0 3px 30px rgba(0,0,0,0.1);
        }}

        .finding-card h2 {{
            font-size: 24px;
            margin-bottom: 16px;
            color: var(--blue);
        }}

        .finding-card p {{
            font-size: 21px;
            line-height: 1.4;
        }}

        /* Paper Sections */
        .paper-section {{
            padding: 60px 0;
        }}

        .paper-section:nth-child(even) {{
            background: var(--gray-light);
        }}

        .paper-section h2 {{
            font-size: 32px;
            font-weight: 600;
            margin-bottom: 32px;
            text-align: center;
        }}

        .paper-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 24px;
        }}

        .paper-card {{
            background: var(--white);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
            transition: transform 0.2s, box-shadow 0.2s;
        }}

        .paper-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(0,0,0,0.12);
        }}

        .paper-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 8px;
        }}

        .paper-title {{
            font-size: 17px;
            font-weight: 600;
            color: var(--blue);
            text-decoration: none;
            line-height: 1.3;
        }}

        .paper-title:hover {{
            text-decoration: underline;
        }}

        .citation-count {{
            font-size: 12px;
            color: var(--text-secondary);
            white-space: nowrap;
            background: var(--gray-light);
            padding: 4px 8px;
            border-radius: 6px;
        }}

        .paper-meta {{
            font-size: 14px;
            color: var(--text-secondary);
            margin-bottom: 12px;
        }}

        .paper-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 12px;
        }}

        .tag {{
            font-size: 11px;
            padding: 4px 8px;
            border-radius: 6px;
            background: var(--gray-light);
            color: var(--text-secondary);
        }}

        .tag.needs-review {{
            background: #fff3cd;
            color: #856404;
        }}

        .paper-claims {{
            font-size: 14px;
            color: var(--text-primary);
        }}

        .claim {{
            margin-bottom: 6px;
        }}

        /* Update History */
        .history-section {{
            background: var(--black);
            color: var(--white);
            padding: 60px 0;
        }}

        .history-section h2 {{
            font-size: 28px;
            margin-bottom: 24px;
            text-align: center;
        }}

        .history-table {{
            width: 100%;
            border-collapse: collapse;
            background: var(--gray-dark);
            border-radius: 12px;
            overflow: hidden;
        }}

        .history-table th,
        .history-table td {{
            padding: 16px;
            text-align: left;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}

        .history-table th {{
            background: rgba(255,255,255,0.05);
            font-weight: 600;
        }}

        /* Footer */
        footer {{
            text-align: center;
            padding: 40px 0;
            color: var(--text-secondary);
            font-size: 14px;
        }}

        footer a {{
            color: var(--blue);
        }}
    </style>
</head>
<body>
    <section class="hero">
        <div class="container">
            <h1>{meta.get("title", "Literature Review")}</h1>
            <div class="meta">
                <span class="meta-pill">📄 <strong>{len(papers)}</strong> papers</span>
                <span class="meta-pill">📅 Updated: <strong>{meta.get("last_updated", "N/A")}</strong></span>
                <span class="meta-pill">📚 Version <strong>{meta.get("version", 1)}</strong></span>
            </div>
            <div class="living-badge">Living Review - Auto-Updated</div>
        </div>
    </section>

    <section class="key-finding">
        <div class="container">
            <div class="finding-card">
                <h2>Key Finding</h2>
                <p>The additive effect of serotonin and dopamine conveys significant reward-related information that neither system alone can provide. This joint activity is essential for normal behavioral function and is disrupted in psychiatric disorders including depression, schizophrenia, and addiction.</p>
            </div>
        </div>
    </section>

    <div class="papers-container">
        <div class="container">
            {paper_sections}
        </div>
    </div>

    <section class="history-section">
        <div class="container">
            <h2>Update History</h2>
            <table class="history-table">
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Action</th>
                        <th>Description</th>
                        <th>Papers Δ</th>
                    </tr>
                </thead>
                <tbody>
                    {generate_update_history(history)}
                </tbody>
            </table>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>Generated with <a href="https://github.com/paperclaw/paperclaw">PaperClaw</a> Living Review System</p>
            <p>Data sourced from Semantic Scholar • Managed with Zotero</p>
        </div>
    </footer>
</body>
</html>
'''
    return html


def main():
    parser = argparse.ArgumentParser(description="Generate HTML report from living review")
    parser.add_argument("--output", type=str, help="Output path for HTML file")
    args = parser.parse_args()

    output_path = Path(args.output) if args.output else DEFAULT_OUTPUT

    print("Loading review data...")
    review = load_review()

    print("Generating HTML report...")
    html = generate_html(review)

    print(f"Writing to {output_path}...")
    with open(output_path, "w") as f:
        f.write(html)

    print(f"✓ Report generated: {output_path}")
    print(f"  Papers: {len(review.get('papers', []))}")
    print(f"  Version: {review.get('meta', {}).get('version', 1)}")


if __name__ == "__main__":
    main()
