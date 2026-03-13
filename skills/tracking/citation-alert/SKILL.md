# Citation Alert

## Overview
Monitors citation activity for the team's own papers and key papers in their field. Alerts when tracked papers receive new citations, identifies who is citing the team's work, and surfaces new papers that build on, challenge, or compare against the team's contributions.

## When to Use
- User wants to know who is citing their paper
- User asks "has anyone cited [our paper] recently?"
- Lab wants to monitor the impact and reception of a published paper
- User wants to know if anyone has compared against their method
- User asks "who else is working on problems similar to ours?"

## Key Capabilities
- Track citation counts over time for team's own papers
- Alert when a new paper cites a tracked work (daily or weekly)
- Classify new citations by type: builds on / compares against / challenges / cites as background
- Identify which labs and institutions are citing the team's work
- Track citation velocity: is citation count accelerating or stagnating?
- Surface citing papers that are most relevant to the team's current research

## Usage Examples

### Set up citation alerts for team's papers
```python
citation_alert.watch(
    dois=["10.48550/arXiv.xxxx.xxxxx", "10.1038/..."],
    alert_frequency="weekly",
    min_relevance=0.5
)
```

### Get recent citations for a paper
```python
citation_alert.get_recent(
    doi="10.48550/arXiv.xxxx.xxxxx",
    since="2024-01-01",
    classify_type=True
)
```

### Find papers that compare against your method
```python
citation_alert.find_comparisons(
    method_name="ContrastiveFold",
    paper_doi="10.48550/arXiv.xxxx.xxxxx"
)
```

### Citation velocity report
```python
citation_alert.velocity_report(
    doi="10.48550/arXiv.xxxx.xxxxx",
    window_months=12,
    compare_to_field_average=True
)
```

## Output Format
Citation alerts list: new paper title, authors, venue, date, citation context (the sentence where the team's paper is cited), and classification. Velocity report shows monthly citation counts with trend line and field comparison.

## Notes
- Citation data sourced from Semantic Scholar and OpenAlex — coverage is broad but not instantaneous
- New citations typically appear in the index within 1–4 weeks of publication
- Combine with `claim-tracker` — if a key claim is being challenged by citing papers, that triggers an alert
- Combine with `living-review` — highly relevant citing papers can be automatically added to the review
