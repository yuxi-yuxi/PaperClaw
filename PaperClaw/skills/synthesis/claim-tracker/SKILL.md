---
name: claim-tracker
description: Tracks specific scientific claims over time — who made them, who replicated or challenged them, and whether they still stand. Use when the user wants to verify a claim before building on it, check if a key result has been replicated, register a central claim from their own work, track whether cited results remain valid, or check if a paper has been retracted. Triggers on phrases like "has this been replicated", "does this claim still hold", "track this result", "verify this finding", "has X been retracted", "provenance of this claim", "register this claim".
---

# Claim Tracker

A provenance system for scientific claims. Every result a team builds on should be tracked — what was claimed, by whom, when, and whether subsequent work has confirmed, challenged, or refuted it.

## Registering a Claim

When a user asks to track or register a claim:

```
Claim: {claim text}
Source: {DOI or arXiv ID}
Authors: {first author et al.}
Year: {year}
Registered by: {team member}
Importance: critical | supporting | background
Status: active
```

Store claims in a local `claims.json` or `claims.md` file in the team's workspace.

## Claim Status Values

| Status | Meaning |
|--------|---------|
| `standing` | No challenges; appears solid |
| `replicated` | Independently confirmed by ≥1 other lab |
| `challenged` | New paper disputes the claim; unresolved |
| `refined` | Claim still holds but with important caveats added |
| `refuted` | Multiple papers or a meta-analysis have overturned it |
| `retracted` | Source paper has been formally retracted |

## Checking if a Claim Still Stands

When asked to verify a claim:

1. **Retraction check**: Query the Retraction Watch database via CrossRef:
   ```
   GET https://api.crossref.org/works/{doi}
   ```
   Look for `update-to` or `relation.is-retracted-by` fields.

2. **Challenge search**: Search Semantic Scholar for papers citing the source that contain challenge-signaling language in their abstract/title:
   - "failure to replicate", "we cannot reproduce", "does not hold", "contradicts", "challenges", "does not generalize"

3. **Replication search**: Search for papers citing the source with replication-signaling language:
   - "we replicate", "consistent with", "we confirm", "reproduces", "validates"

4. **Update search**: Check if the source paper has been updated (arXiv v2+, published erratum, or correction)

## Provenance Trace

When asked for the provenance of a claim, produce a timeline:

```
## Provenance: "Scaling laws hold for code generation models"

2020-01 → [Brown et al.] First reports scaling laws for LMs generally
2021-06 → [Chen et al.] Codex paper — first systematic study of code models, confirms scaling
2022-03 → [Chowdhery et al.] PaLM — code scaling results consistent with [Chen 2021]
2022-11 → [Hoffmann et al.] Chinchilla — revises compute-optimal scaling; applies to code too
2023-09 → [Liu et al.] Questions whether scaling holds for reasoning tasks specifically
2024-02 → [Team] This claim is REFINED: scaling holds for completion but is contested for reasoning

Current status: Refined (active for completion tasks, contested for reasoning tasks)
```

## claims.md Format

Track claims in a flat Markdown file for human readability:

```markdown
## Claim #0042
**Claim**: Contrastive pretraining on evolutionary sequences improves fitness prediction in low-data regimes
**Source**: arXiv:2310.12345 (Zhang et al., 2023)
**Registered**: 2024-01-15 by Alice
**Importance**: critical
**Status**: standing
**Evidence**:
- [2023-11] [Notin et al.] — consistent result on ProteinGym
**Notes**: Only tested on single-domain proteins so far
```

## Alert Conditions

Automatically flag a claim for review when:
- Source paper is retracted (check CrossRef `update-to` field)
- A paper citing the source uses challenge language in its abstract
- The source paper has been updated (new arXiv version or published correction)
- A meta-analysis covering the topic is published that includes the source

## Integration Notes

- Claims marked `critical` should be verified before manuscript submission
- Use `contradiction-detection` — papers flagged as contradictions should be registered as challenges
- Use `evidence-grading` to assess whether a challenge is well-supported enough to downgrade the claim status
- Retracted paper check: https://retractionwatch.com/retraction-watch-database-user-guide/
