# Living Review: Monoamine Interactions

This is a **living literature review** that is continuously updated as new papers are published.

## Quick Start

### Update the review with new papers
```bash
# Dry run - see what would be added
python update_review.py --dry-run

# Actually update the review
python update_review.py

# Search from a specific date
python update_review.py --since 2024-01-01

# Require higher citation threshold
python update_review.py --min-citations 10
```

### Regenerate the HTML report
```bash
python generate_report.py
```

## Files

| File | Description |
|------|-------------|
| `review.json` | The structured review data (papers, metadata, history) |
| `update_review.py` | Script to check for new papers on Semantic Scholar |
| `generate_report.py` | Script to generate HTML report from JSON |
| `README.md` | This file |

## Review Structure

The `review.json` contains:

- **meta**: Title, topic, search queries, Zotero collection, version
- **papers**: Array of papers with DOIs, claims, tags, notes
- **update_history**: Log of all changes to the review

## Adding Papers Manually

Edit `review.json` and add a paper entry:

```json
{
  "id": "author2024",
  "doi": "10.1234/example",
  "title": "Paper Title",
  "authors": ["Author, A.", "et al."],
  "year": 2024,
  "citations": 50,
  "added_by": "your_name",
  "added_date": "2026-04-11",
  "tags": ["tag1", "tag2"],
  "category": "Recent Advances (2022-2026)",
  "key_claims": ["Main finding from this paper"],
  "notes": "Why this paper is important"
}
```

Then regenerate the report:
```bash
python generate_report.py
```

## Automation

Set up a cron job or GitHub Action to run weekly:

```bash
# Weekly update (Sundays at midnight)
0 0 * * 0 cd /path/to/reviews/monoamine-interactions && python update_review.py
```

## Review Workflow

1. **Auto-discovery**: `update_review.py` finds new papers
2. **Triage**: Papers marked `needs_review: true` need manual review
3. **Curate**: Add key claims, fix tags, update notes
4. **Publish**: Run `generate_report.py` to update HTML
