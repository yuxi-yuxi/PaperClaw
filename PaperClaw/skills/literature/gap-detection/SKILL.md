---
name: gap-detection
description: Identifies research gaps — what hasn't been studied, is underexplored, or remains unresolved — in a body of literature. Use when the user wants to find novel research directions, position their work as a new contribution, write a significance or motivation section for a grant or paper, verify that a proposed contribution is actually novel, or identify what the field is missing. Triggers on phrases like "what hasn't been done", "research gaps", "what's missing", "is this novel", "open questions", "what should we study next", "gap in the literature".
---

# Gap Detection

Identifies what the field has NOT done yet — empirical gaps, methodological blind spots, underexplored populations, and unresolved theoretical questions. This is the foundation of a strong novelty claim.

## Sources of Gap Evidence

The highest-signal sources of research gaps, in order of reliability:

1. **Explicitly stated future work** — "Future work should explore X" in paper conclusions
2. **Explicitly stated limitations** — "This study is limited to Y" implies Y needs to be extended
3. **Methodological monocultures** — If every paper uses the same dataset/model/evaluation, alternatives are unstudied
4. **Coverage asymmetries** — Some conditions, species, languages, or populations are heavily studied; others not
5. **Contradiction zones** — Where papers disagree, the question is unresolved → gap in understanding
6. **Date patterns** — Areas that were active 5+ years ago but have few recent papers may have stalled

## Extraction Process

For each paper in the corpus:

1. Locate the **Conclusion** and **Limitations** sections
2. Extract sentences containing gap-signaling phrases:
   - "future work", "remains to be", "we leave for future", "an open question"
   - "limited to", "does not address", "outside the scope", "we only consider"
   - "one limitation", "a drawback", "a weakness of"
3. Cluster extracted gaps by topic using semantic similarity
4. Count how many papers mention each gap cluster — frequency = importance signal

## Gap Taxonomy

Classify each identified gap by type:

| Type | Description | Example |
|------|-------------|---------|
| **Empirical** | A condition, dataset, or population not yet tested | "Only tested on English; other languages unstudied" |
| **Methodological** | An approach or technique not applied to this problem | "No diffusion model applied to this task" |
| **Theoretical** | An explanation or mechanism not established | "Why scaling helps is not understood" |
| **Applied** | A real-world deployment or use case not addressed | "Clinical deployment not validated" |
| **Replication** | Results not independently verified | "Only one group has reported this finding" |

## Novelty Validation

When a user proposes a contribution and asks "is this novel?":
1. Formulate 3–5 search queries capturing the proposed contribution
2. Search Semantic Scholar and arXiv for papers matching the contribution
3. For each match, assess how closely it overlaps with the proposed work
4. Return: `{status: "novel" | "incremental" | "done", evidence: [...], confidence: 0.0–1.0}`

**Always caveat**: novelty validation is probabilistic. A negative result (no papers found) reduces but does not eliminate the risk of prior work existing.

## Output: Gap Map

Structure gaps into a table or narrative:

```
## Research Gap Map: [Topic]

### Empirical Gaps
1. No study has evaluated [method] on [population/dataset] — mentioned in 8 papers
2. Cross-lingual transfer remains unstudied in [domain] — mentioned in 3 papers

### Methodological Gaps  
1. Diffusion-based approaches have not been applied to [task]
2. No work uses reinforcement learning for [problem]

### Theoretical Gaps
1. The mechanism by which [X] improves [Y] is not understood
2. Scaling behavior in [regime] has not been characterized

### Applied Gaps
1. All studies use synthetic benchmarks — real-world validation is absent
```

## Grant Writing Integration

When asked to generate a gap map for a grant:
- Frame gaps as **unmet needs** rather than omissions
- Lead with the highest-impact gap (patient/societal harm from the gap existing)
- Connect the gap directly to the proposed work
- Cite the papers that establish the gap exists

## Integration Notes

- Run after `living-review` to identify what's missing from the team's topic area
- Combine with `consensus-mapping` — gaps often sit at the boundary of what the field agrees on
- Use `evidence-grading` to assess how strongly established each gap really is
