---
name: contradiction-detection
description: Scans a body of papers for conflicting empirical claims, opposing conclusions, or methodological disagreements on the same topic. Use when the user wants to know if papers in their corpus disagree with each other, needs to address conflicting findings in a discussion section, wants to verify a claim before building on it, or is trying to understand why two papers got different results. Triggers on phrases like "do any papers disagree", "conflicting findings", "paper A contradicts paper B", "why do results differ", "conflicting claims", "contradiction in the literature".
---

# Contradiction Detection

Surfaces genuine scientific contradictions — cases where two or more papers make opposing claims on the same empirical question. Knowing where the field disagrees is as important as knowing where it agrees.

## Contradiction Types

| Type | Description | Example |
|------|-------------|---------|
| **Empirical** | Different quantitative results on the same task | Paper A: 85% accuracy; Paper B: 71% on same benchmark |
| **Directional** | Opposite conclusions about the direction of an effect | "X improves Y" vs. "X does not improve Y" |
| **Methodological** | Disagreement on best practice | "Dropout helps" vs. "Dropout hurts in this regime" |
| **Interpretive** | Same data, different explanations | Same results, different proposed mechanism |
| **Replication failure** | Claimed result not reproduced | Follow-up paper reports failure to replicate |

## Detection Process

For each pair of papers covering the same topic:

1. **Extract claims**: Pull key quantitative and qualitative assertions from Results and Conclusions sections
2. **Align claims**: Find claims about the same variable, condition, model, or dataset
3. **Compare**: Check for directional conflict (opposing effect) or quantitative discrepancy (outside confidence intervals)
4. **Score severity**: How contradictory are they? (minor discrepancy vs. fundamental disagreement)
5. **Propose cause**: What experimental difference might explain the contradiction?

## Potential Causes of Contradiction (Check These First)

Before labeling something a genuine contradiction, consider:
- **Different datasets**: Same task name, different actual data → results need not agree
- **Different evaluation protocols**: Metric details, train/test splits, preprocessing
- **Different hyperparameter budgets**: One paper did 10x more tuning
- **Different model sizes**: Results that hold at one scale may not generalize
- **Publication bias**: Positive results published; replications are hard to find

## Output Format

For each detected contradiction:

```
## Contradiction #3: Effect of dropout on transformer training

**Paper A**: "Dropout (p=0.1) consistently improves validation perplexity across all model sizes tested"
  → [Smith et al. 2022, NeurIPS] — n=4 model sizes, GPT-2 architecture

**Paper B**: "We find no significant benefit from dropout in transformer LMs above 1B parameters"
  → [Jones et al. 2023, ICML] — n=6 model sizes, LLaMA architecture

**Contradiction type**: Directional (empirical)
**Severity**: Moderate — results could be explained by model scale threshold
**Possible cause**: Different model sizes tested; Smith et al. tested ≤350M params, Jones et al. ≥1B
**Status**: Potentially reconcilable — threshold effect hypothesis
**Recommended action**: Read both papers' experimental details; check if scale explains the discrepancy
```

## When to Push Back

Some "contradictions" are not real contradictions:
- Different tasks with same name → not a contradiction
- Different populations/domains → expected to differ
- Different metrics → can't directly compare
- One paper is a strict extension of the other

Flag these as "apparent contradictions" with explanation.

## Discussion Section Framing

When asked to frame contradictions for a manuscript discussion:

> "Our results align with [Paper A] but diverge from [Paper B], which reported [X]. This discrepancy may be explained by [proposed cause]. Future work should directly compare [key experimental variable] to resolve this question."

## Integration Notes

- Run after `living-review` to audit the team's knowledge base for internal inconsistencies
- Use `evidence-grading` to determine which side of a contradiction has stronger support
- Use `consensus-mapping` to understand what proportion of the field holds each position
- Contradictions = research gaps → feed into `gap-detection`
