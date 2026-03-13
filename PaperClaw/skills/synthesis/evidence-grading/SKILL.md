---
name: evidence-grading
description: Evaluates and grades the strength of evidence behind scientific claims based on study design, replication status, sample size, venue quality, and recency. Use when the user wants to know how much to trust a finding, needs to calibrate hedging language for a manuscript, wants to grade preliminary evidence for a grant, or needs to rank a set of papers by evidentiary weight. Triggers on phrases like "how strong is the evidence", "can we trust this result", "how preliminary is this", "grade this paper", "how confident should we be", "is this well-supported", "calibrate our claim".
---

# Evidence Grading

Not all evidence is equal. This skill grades the strength of evidence behind claims so the team can calibrate how confidently to build on, cite, or assert results.

## Grading Schema

### ML / Computer Science (empirical results)

| Grade | Label | Criteria |
|-------|-------|----------|
| A | Widely replicated | Result reproduced by ≥3 independent groups; consistent across model families |
| B+ | Replicated | Independently reproduced by ≥1 other group on different setup |
| B | Single strong study | Single paper; top venue (NeurIPS/ICML/ICLR/Nature/Science); thorough ablations |
| B- | Single decent study | Top-3 venue; limited ablations; small-scale experiments |
| C | Preprint / workshop | Not peer-reviewed; or peer-reviewed but narrow scope |
| D | Preliminary | Single experiment; no ablations; anecdotal; n=1 |
| F | Retracted / disputed | Formally retracted or majority of follow-up work contradicts |

### Biomedical / Clinical

Adapt Oxford Centre for Evidence-Based Medicine (CEBM) levels:

| Level | Type |
|-------|------|
| 1 | Systematic review of RCTs or n-of-1 trials |
| 2 | RCT or observational study with dramatic effect |
| 3 | Cohort study, non-randomized controlled trial |
| 4 | Case-control study, case series |
| 5 | Expert opinion, mechanistic reasoning |

## Grading a Single Paper

Assess each dimension, then combine into an overall grade:

| Dimension | Questions to ask |
|-----------|-----------------|
| **Study design** | Is it an RCT? Observational? Ablation study? Synthetic benchmark? |
| **Sample size** | N large enough to detect the effect size claimed? |
| **Replication** | Has anyone else tried this? Did it work? |
| **Venue** | Peer-reviewed top venue vs. preprint vs. workshop? |
| **Recency** | Is this still the state-of-the-art or 5 years old? |
| **Ablations** | Are controls adequate? Are baselines fair? |
| **Conflicts** | Industry funding? Incentive to show positive results? |

## Grading a Claim Across Multiple Papers

When a claim is supported by multiple papers:
1. Grade each paper individually
2. Weight by: grade, recency, independence (same lab = correlated, not independent)
3. Overall claim grade = weighted average, penalized if any paper is retracted or F-graded

## Generating Hedging Language

Map grade to appropriate language for manuscripts and grants:

| Grade | Language |
|-------|---------|
| A | "It is established that..." / "Consistent with the well-replicated finding that..." |
| B+ | "Evidence from multiple groups suggests..." |
| B | "Recent work has shown..." / "[Author] demonstrated that..." |
| B- | "Preliminary evidence indicates..." / "[Author] reported..." |
| C | "Initial results suggest..." / "A preprint by [Author] proposes..." |
| D | "In an exploratory experiment, [Author] observed..." |

**Rules**:
- Never use "It is known that..." for anything below grade B
- Never use "demonstrated" for preprints (grade C or below)
- Always use hedging for grade C or below: "suggests", "indicates", "preliminary", "may"

## Output Format

```
## Evidence Grade: "Contrastive pretraining improves protein fitness prediction"

Overall grade: B (Single strong study; top venue; no independent replication yet)

Supporting evidence:
  [B] Zhang et al. 2023, NeurIPS — "Contrastive Protein LMs" — thorough ablations, competitive baselines
  [C] Liu et al. 2024, bioRxiv — preprint, consistent results but not yet peer-reviewed
  
Caveats:
  - Both papers are from the same research group → not independent replication
  - Tested on ProteinGym only; generalization to other fitness landscapes unknown
  
Recommended language: "Recent work has shown that contrastive pretraining improves fitness 
prediction in low-data regimes [Zhang et al., 2023], though independent replication is ongoing."
```

## Integration Notes

- Use `claim-tracker` to register claims and store their evidence grades
- Use `consensus-mapping` — consensus level maps to evidence grade for a field-wide claim
- Use in `review-response` to assess whether reviewer concerns have strong evidential basis
- Use in `grant-writing` to calibrate confidence levels in preliminary data sections
