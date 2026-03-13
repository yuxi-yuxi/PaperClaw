---
name: citation-alert
description: Monitors incoming citations to the team's own papers and classifies them by type and context. Use when the user wants to know who has cited their work, track citation velocity, find papers that build on or challenge their results, generate a citation report for a grant renewal or review, or discover unexpected applications of their work. Triggers on phrases like "who cited our paper", "citation alert", "citation count", "has anyone cited X", "citation report", "who's building on our work", "citation velocity", "h-index".
---

# Citation Alert

Tracks incoming citations to the team's published and preprint work. Classifies citations by type, monitors velocity, and flags when citations indicate a challenge or unexpected use of the work.

## Setting Up Citation Tracking

Register papers to monitor:

```json
{
  "paper_id": "DOI:10.1038/s41586-024-00001-0",
  "title": "Our Key Paper Title",
  "authors": ["Smith, A.", "Jones, B."],
  "published": "2023-06-15",
  "last_checked": "2024-03-01",
  "citation_count_at_last_check": 47
}
```

## Fetching Citations

### Semantic Scholar (primary)
```
GET https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations?fields=title,authors,year,abstract,venue,citationCount&limit=100
```

For pagination beyond 100: use `offset` parameter.

### OpenAlex (cross-check)
```
GET https://api.openalex.org/works?filter=cites:{doi}&per-page=50&sort=cited_by_count:desc
```

### Google Scholar (manual fallback)
If APIs miss papers (common for very recent citations):
`https://scholar.google.com/scholar?cites={scholar_id}`

Report the Scholar ID alongside the DOI in the paper registry.

## Citation Classification

For each new citing paper, classify the citation type by analyzing the sentence(s) surrounding the citation:

| Type | Signal phrases | Meaning |
|------|---------------|---------|
| **Builds on** | "following", "extending", "inspired by", "building on", "we adapt" | Uses our method |
| **Benchmarks against** | "compared to", "outperforms", "baseline", "we evaluate against" | Uses our paper as a benchmark |
| **Reviews / surveys** | "review", "survey", "overview", "taxonomy" | Included in a review |
| **Challenges** | "however", "in contrast", "fails to", "does not generalize", "we find that [our paper] does not" | Disputes our results |
| **Background** | "has been shown that", "it is established", "prior work" | Used as context-setting |
| **Applies** | "we apply", "we use the method of", "following the approach of" | Applied our method to a new domain |

Flag `challenges` citations for immediate review.

## Velocity Report

Track citation counts over time:

```
## Citation Velocity Report
Paper: "Our Key Paper" (DOI: 10.xxxx/...)
Published: 2023-06-15

Month     | New Citations | Total | Velocity (per month)
----------|--------------|-------|--------------------
Jul 2023  | 2            | 2     | 2
Aug 2023  | 4            | 6     | 4
...
Feb 2024  | 18           | 89    | 18  ← acceleration

Field average (comparable papers): ~5/month at this age
Status: OUTPACING FIELD AVERAGE
```

## Citation Alert Digest

```
## PaperClaw Citation Alert — March 2024

### "Our Key Paper" (Smith et al., 2023) — 12 new citations

🔨 Builds on (5):
  - "Extending [Our Method] to Clinical Settings" — Chen et al., Nature Medicine
  - "Cross-lingual Transfer for [Task] Using [Our Approach]" — Kim et al., ACL 2024

⚔️ Challenges (1): ← PRIORITY REVIEW
  - "Revisiting [Our Claim]: Evidence from Larger Models" — Brown et al., arXiv:2403.xxxxx
    Context: "We find that [our method] fails to generalize above 7B parameters, 
    contradicting [Smith et al. 2023]."

📊 Benchmarked against (4):
  [list of comparison papers]

📋 Background citations (2):
  [standard background citations]
```

## H-Index and Impact Metrics

When asked for the team's h-index or citation metrics:

```python
# h-index calculation
papers = sorted(citation_counts, reverse=True)
h = sum(1 for i, c in enumerate(papers, 1) if c >= i)
```

Report:
- h-index
- Total citations
- Citations in last 12 months
- Most-cited paper
- Fastest-growing paper (highest velocity)
- Papers with 0 citations (may need promotion)

## Integration Notes

- `challenges` citations should immediately be added to `contradiction-detection` for analysis
- Papers that "build on" our work are candidates for collaboration or follow-up
- Use `claim-tracker` — if a challenge citation disputes a registered claim, update the claim status
- Citation data feeds grant renewal sections: "Our [Year] paper has been cited N times, including by [high-impact work]"
