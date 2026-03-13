# Hypothesis Versioning

## Overview
Maintains a version-controlled registry of the team's hypotheses — tracking how they evolved, what evidence shaped each revision, and why earlier versions were updated or abandoned. Provides an auditable scientific record of the team's thinking over time.

## When to Use
- User wants to record or update a research hypothesis
- User asks "how has our hypothesis on [topic] changed over time?"
- Lab wants to document the reasoning behind a major pivot
- PI wants to show reviewers or funders the intellectual progression of the research
- User wants to trace which papers caused a hypothesis revision

## Key Capabilities
- Register hypotheses with version history and supporting evidence
- Track revisions: what changed, what triggered the change, and who made it
- Link each hypothesis version to the papers, experiments, or discussions that motivated it
- Generate a hypothesis evolution timeline
- Compare two versions of a hypothesis with a structured diff
- Flag hypotheses that are contradicted by recent literature
- Export hypothesis history for grant applications or thesis documentation

## Usage Examples

### Register a new hypothesis
```python
hypothesis_versioning.register(
    hypothesis="Contrastive pretraining on evolutionary sequences improves fitness prediction in low-data regimes",
    author="alice",
    supporting_evidence=["DOI:10.1038/...", "DOI:10.1101/..."],
    confidence=0.7,
    project="protein_fitness"
)
```

### Update a hypothesis with new version
```python
hypothesis_versioning.update(
    hypothesis_id="hyp_0042",
    new_text="Contrastive pretraining improves fitness prediction, but only when fine-tuned on homologous sequences",
    change_reason="Ablation results in Experiment 7 showed no improvement without homolog fine-tuning",
    triggered_by=["exp_007", "DOI:10.1101/..."]
)
```

### View hypothesis evolution timeline
```python
hypothesis_versioning.timeline(
    hypothesis_id="hyp_0042",
    include_evidence=True,
    format="narrative"
)
```

### Check if hypothesis is contradicted by recent literature
```python
hypothesis_versioning.check_literature(
    hypothesis_id="hyp_0042",
    search_recent_months=6
)
```

## Output Format
Each hypothesis record contains: ID, current version, full version history, evidence chain, confidence score, and status (active / refined / abandoned / confirmed). Timeline output is narrative or structured JSON.

## Notes
- Hypothesis versioning is not experiment tracking — use `experiment-log` for that
- Confidence scores are team-assigned, not automatically computed
- Abandoned hypotheses are preserved, never deleted — they are scientifically valuable
