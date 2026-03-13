# Preprint Watch

## Overview
Monitors preprint servers (arXiv, bioRxiv, medRxiv, SSRN, ChemRxiv) for papers relevant to the team's active research. Distinguishes between preprints and peer-reviewed work, tracks when monitored preprints get published, and alerts when a preprint that the team has cited gets updated or retracted.

## When to Use
- User wants to monitor preprint servers for a specific topic
- User asks "has the preprint for [paper] been published yet?"
- User wants to know if a preprint they cited has been updated since they read it
- Lab wants to track competitor preprints in an active area
- User asks "what preprints came out this week on [topic]?"

## Key Capabilities
- Monitor arXiv, bioRxiv, medRxiv, ChemRxiv, and SSRN by topic, keyword, or author
- Track preprint-to-publication transitions (when a preprint gets accepted and published)
- Alert when a monitored preprint is updated (new version posted)
- Distinguish preprints from peer-reviewed work throughout the literature base
- Flag preprints in the team's library that have since been retracted or significantly revised
- Compare preprint v1 vs. latest version when a paper has been revised

## Usage Examples

### Monitor preprints on a topic
```python
preprint_watch.monitor(
    topic="diffusion models for protein design",
    servers=["arxiv", "biorxiv"],
    frequency="daily",
    min_relevance=0.7
)
```

### Check if a preprint has been published
```python
preprint_watch.check_publication_status(
    arxiv_id="2310.xxxxx"
)
# Returns: {"status": "published", "journal": "Nature Methods", "doi": "10.1038/...", "published_date": "2024-03-15"}
```

### Check if cited preprints have been updated
```python
preprint_watch.check_updates(
    preprints=review.get_papers(source="preprint"),
    alert_on=["new_version", "retraction", "publication"]
)
```

### Compare preprint versions
```python
preprint_watch.diff_versions(
    arxiv_id="2310.xxxxx",
    v1=1,
    v2="latest",
    focus="results"  # results | methods | abstract | full
)
```

## Output Format
Monitoring alerts are structured as: paper title, server, date, relevance score, and 2-sentence summary. Publication status returns: current status, journal (if published), DOI, and date. Version diff highlights changed sections.

## Notes
- arXiv papers update by appending versions (v1, v2, v3) — major revisions sometimes change results significantly
- bioRxiv papers sometimes change substantially between preprint and publication — always cite the published version in final manuscripts
- Combine with `arxiv-monitor` — preprint watch focuses on tracking known papers while arxiv-monitor discovers new ones
