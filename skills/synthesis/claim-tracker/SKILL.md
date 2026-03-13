# Claim Tracker

## Overview
Tracks specific scientific claims across the literature over time — who made the claim, who replicated it, who challenged it, and whether it still stands. Acts as a provenance system for the ideas a team builds on, preventing citation of retracted, updated, or disproven work.

## When to Use
- User wants to verify a specific claim before building on it
- User asks "has anyone replicated [finding] from [paper]?"
- User needs to track whether a claim has been updated or superseded
- Lab wants to maintain a live registry of claims central to their research
- Writing a paper and need to know the full citation chain for a key premise

## Key Capabilities
- Register a claim with its source paper, date, and context
- Search for follow-up papers citing, extending, or challenging the claim
- Flag claims that come from retracted papers (cross-references Retraction Watch)
- Track claim evolution: original → replication → challenge → resolution
- Notify team when a tracked claim is cited by new work
- Generate a provenance trace for any claim: full chain of evidence

## Usage Examples

### Register and track a claim
```python
claim_tracker.register(
    claim="GPT-3 achieves few-shot performance comparable to fine-tuned BERT on SuperGLUE",
    source_doi="10.48550/arXiv.2005.14165",
    registered_by="alice",
    importance="critical"  # critical | supporting | background
)
```

### Check if a claim still stands
```python
claim_tracker.verify(
    claim_id="claim_0042",
    search_challenges=True,
    check_retractions=True
)
```

### Get full provenance trace
```python
claim_tracker.provenance(
    claim_id="claim_0042",
    format="narrative"  # narrative | timeline | graph
)
```

### List all critical claims in team's research
```python
claim_tracker.list(importance="critical", status="all")
```

## Output Format
Each claim record contains: claim text, source paper, registration date, current status (standing/challenged/refuted/retracted), evidence chain, and team notes. Provenance output available as narrative, timeline, or graph.

## Notes
- Retraction Watch database is checked via CrossRef API
- Claims marked "critical" trigger automatic alerts when challenged in new literature
- Combine with `living-review` — claims extracted during review are auto-registered
