---
name: preprint-watch
description: Monitors tracked preprints on arXiv, bioRxiv, and medRxiv for new versions, journal publication, peer review outcomes, and major revisions. Use when the user wants to be notified when a specific preprint is updated, published, or retracted, when tracking competitor papers, or when monitoring their own preprint's trajectory. Triggers on phrases like "watch this preprint", "track this arXiv paper", "has this been published yet", "any updates to", "monitor this preprint", "is this still a preprint", "what happened to", "version history".
---

# Preprint Watch

Tracks specific preprints over time — new versions, peer-reviewed publication, citations received, and any challenges or corrections. Particularly useful for monitoring competitor work and papers on which the team is building.

## Preprint Watch Record

```json
{
  "id": "watch_0023",
  "title": "Contrastive Protein Language Models for Fitness Prediction",
  "arxiv_id": "2310.12345",
  "biorxiv_doi": null,
  "added_by": "alice",
  "added_date": "2024-01-10",
  "reason": "Competitor paper — directly relevant to our Aim 1",
  "priority": "high",
  "current_version": "v2",
  "versions": [
    {"version": "v1", "date": "2023-10-18", "changes": "Initial submission"},
    {"version": "v2", "date": "2024-01-05", "changes": "Added experiments on medRxiv families; revised ablations"}
  ],
  "published": null,
  "published_venue": null,
  "citation_count": 12,
  "last_checked": "2024-03-15"
}
```

Store watch list in `preprint_watch.json`.

## Adding a Preprint to Watch

When the user says "watch this preprint" or provides an arXiv/bioRxiv link:

1. Fetch current metadata from arXiv API:
```
GET http://export.arxiv.org/api/query?id_list={arxiv_id}
```
Or bioRxiv API:
```
GET https://api.biorxiv.org/details/biorxiv/{doi}/na/json
```

2. Store title, authors, current version, submission date
3. Ask: priority (high / medium / low) and reason for watching
4. Confirm: "✅ Now watching arXiv:2310.12345 — will alert on new versions and publication"

## Checking for Updates

When asked "any updates to [paper]" or running a routine check:

### arXiv version check
```python
import feedparser
url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
feed = feedparser.parse(url)
current_version = feed.entries[0].get('arxiv_version', 'v1')
updated_date = feed.entries[0].updated
```

Compare to stored `current_version`. If changed → alert.

### bioRxiv version check
```
GET https://api.biorxiv.org/details/biorxiv/{doi}/na/json
```
Check `version` field in response.

### Published journal check
Cross-reference via CrossRef — preprints often link to published version:
```
GET https://api.crossref.org/works?filter=relation.type:is-preprint-of&query={title}
```
Or check DOI resolution for the preprint — if it redirects to a journal, it's published.

Also check Semantic Scholar for the paper's `publicationVenue` field:
```
GET https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}?fields=publicationVenue,journal
```

## Version Diff Summary

When a new version is detected, generate a change summary:

```
🆕 UPDATE: arXiv:2310.12345 — "Contrastive Protein LMs" — v1 → v2

Key changes in v2 (2024-01-05):
  • Added experiments on 5 additional protein families from ProteinGym
  • Revised ablation Table 3 — contrastive vs. MLM comparison now includes ESM-2-650M
  • New Section 4.3: analysis of failure cases
  • Abstract updated to remove claim about "state-of-the-art" on ProteinGym

⚠️ Notable: The abstract revision suggests they lost SOTA on some benchmark. 
   Worth reading Table 3 carefully — affects our comparison claims.
```

## Publication Alert

When a watched preprint is published:

```
📰 PUBLISHED: arXiv:2310.12345 → Nature Methods (2024-03-10)
   "Contrastive Protein Language Models for Fitness Prediction"
   DOI: 10.1038/s41592-024-XXXXX

Impact:
  - This is now a peer-reviewed result — upgrade from evidence grade C → B
  - Update claim_0038 in claim-tracker (evidence source changed)
  - Our submitted comparison should cite the journal version, not arXiv
  - Citation count: 12 (preprint) → likely to accelerate post-publication
```

## Citation Velocity Tracking

For high-priority preprints, track citation count over time:

```
arXiv:2310.12345 citation trajectory:
  2023-10 (submission): 0 citations
  2023-11: 2 citations
  2023-12: 5 citations
  2024-01: 8 citations
  2024-02: 12 citations
  2024-03: 19 citations ← accelerating — this paper is gaining traction
```

Rising citation velocity on a preprint = signal the community is taking it seriously.

## Tracking Our Own Preprint

When monitoring the team's own submitted preprint:

```
Our paper: arXiv:2403.XXXXX — "Homolog-Aware Fine-Tuning for Protein Fitness"
Status: Under review at NeurIPS 2024

Citations so far: 3 (2 weeks post-submission)
  - Cited by: [arXiv:2404.11111] — comparison paper using our benchmark
  - Cited by: [arXiv:2404.22222] — concurrent work; check for overlap

Version: v1 only — no revisions since submission
```

## Weekly Watch Report

```
## Preprint Watch Update — Week of [Date]

🆕 New versions:
  arXiv:2310.12345 (v1→v2) — major revision, new experiments added
  
📰 Published:
  bioRxiv:2023.08.15 → Cell Systems — now peer-reviewed, update evidence grades

📊 Citation milestones:
  arXiv:2301.99999 — reached 100 citations (was 87 last week) — accelerating

🔍 No change:
  [8 papers] — checked, no updates
```

## Integration Notes

- When a watched preprint is published → update `claim-tracker` evidence grade (C → B)
- When a new version adds/removes claims → update `claim-tracker` or `contradiction-detection`
- Use `arxiv-monitor` for discovery; use `preprint-watch` for ongoing tracking of specific papers
- High citation velocity on competitor paper → flag in next `team-sync` agenda
