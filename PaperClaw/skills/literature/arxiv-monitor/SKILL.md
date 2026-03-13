---
name: arxiv-monitor
description: Monitors arXiv for new papers matching research interests. Use when the user wants to know what's new on arXiv, set up monitoring for a topic or author, get a weekly digest of relevant preprints, or find out if anyone has published on a specific topic recently. Triggers on phrases like "what's new on arXiv", "monitor arXiv for", "recent papers on", "arXiv digest", "any new preprints about", "has anyone published on X".
---

# arXiv Monitor

Replaces manual daily browsing of arXiv with targeted, relevance-scored alerts. Fetches new submissions, scores them against a research profile, and surfaces only what matters.

## Fetching Recent Papers

Use the arXiv API (`http://export.arxiv.org/api/query`) to fetch recent submissions:

```
GET http://export.arxiv.org/api/query?search_query=cat:cs.LG+AND+ti:protein&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending
```

Key parameters:
- `cat:` — arXiv category (e.g., `cs.LG`, `cs.AI`, `q-bio.QM`, `stat.ML`, `physics.bio-ph`)
- `ti:` / `abs:` — search in title / abstract
- `au:` — filter by author name
- `submittedDate` — sort by submission date to get newest first

## Supported Categories

| Domain | Key Categories |
|--------|---------------|
| Machine Learning | `cs.LG`, `cs.AI`, `stat.ML` |
| Computational Biology | `q-bio.QM`, `q-bio.GN`, `q-bio.BM` |
| Physics / Biophysics | `physics.bio-ph`, `cond-mat.soft` |
| NLP | `cs.CL` |
| Computer Vision | `cs.CV` |
| Robotics | `cs.RO` |

## Scoring Relevance

For each paper, compute a relevance score (0–1):
1. Keyword overlap: count matches between paper title+abstract and the team's keyword list
2. Category match: bonus if paper is in a primary category of interest
3. Author match: bonus if paper is by a tracked author or lab
4. Citation signal: not available for new preprints — skip

Return only papers above a minimum relevance threshold (default: 0.5).

## Output Format

Return a ranked list, most relevant first:

```
[1] Title: Contrastive Learning for Protein Fitness Prediction
    Authors: Zhang et al. | arXiv:2403.12345 | cat:cs.LG, q-bio.QM
    Relevance: 0.87 | Submitted: 2024-03-15
    Summary: Proposes NT-Xent pretraining on evolutionary sequences to improve 
    low-data fitness prediction. Achieves state-of-the-art on ProteinGym.
    Tags: #contrastive-learning #protein-lm #fitness-prediction
```

## Setting Up a Watch

When asked to monitor a topic on a recurring basis, output a configuration block:

```yaml
watch:
  query: "contrastive learning protein fitness"
  categories: [cs.LG, q-bio.QM]
  author_ids: []
  keywords: [contrastive, protein, fitness, low-data]
  frequency: weekly
  min_relevance: 0.6
  notify: slack:#lab-papers
```

Instruct the user to save this and schedule with `cron` or a task runner of their choice.

## Checking for Competitor Activity

When a user asks "has [lab/author] published anything new":
1. Search by author: `au:Lastname_F` in arXiv API
2. Filter by recent submission date (last 30 days by default)
3. Return matches with full metadata

## Rate Limiting

arXiv API fair use: max 3 requests/second, 1 request/3 seconds preferred. Add `time.sleep(1)` between batch requests.

## Integration Notes

- Combine with `living-review` to auto-ingest high-relevance papers into the team's corpus
- Use `preprint-watch` to track specific preprints after they're identified here
- For biomedical papers, combine with PubMed/bioRxiv monitoring from `semantic-scholar`
