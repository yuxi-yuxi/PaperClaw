---
name: experiment-log
description: Records, structures, and retrieves experiment logs — what was run, why, what happened, and what was learned. Use when the user wants to log an experiment, look up a past result, understand why a previous experiment was run, compile preliminary data for a grant, or reproduce a past experiment. Triggers on phrases like "log this experiment", "what did exp X show", "past results on", "preliminary data", "compile our results", "what have we tried", "reproduce this experiment", "experiment failed", "record these results".
---

# Experiment Log

A structured, persistent record of every experiment the team runs. The log is the team's scientific memory — raw results, why they were run, what was learned, and how they connect to hypotheses.

## Experiment Record Format

```json
{
  "id": "exp_0055",
  "title": "Fine-tuning vs. zero-shot ESM-2 on 8 protein families",
  "hypothesis": "hyp_0017",
  "run_by": "carol",
  "date": "2024-03-18",
  "status": "completed",
  "purpose": "Test whether homolog fine-tuning is necessary for generalization to distant families",
  "setup": {
    "model": "ESM-2 (650M)",
    "dataset": "ProteinGym substitutions — 8 DMS assays, diverse families",
    "baselines": ["zero-shot ESM-2", "EVE (Notin 2022)"],
    "metric": "Spearman ρ (fitness vs. predicted score)",
    "compute": "4× A100 80GB, 18 hours"
  },
  "results": {
    "fine_tuned_esm2": {"mean_spearman": 0.61, "std": 0.08, "n_families": 8},
    "zero_shot_esm2": {"mean_spearman": 0.49, "std": 0.11, "n_families": 8},
    "eve_baseline": {"mean_spearman": 0.58, "std": 0.09, "n_families": 8}
  },
  "findings": "Fine-tuned ESM-2 outperforms zero-shot on 7/8 families (mean +0.12 Spearman). Exception: GFP family where zero-shot is competitive (likely due to overrepresentation in pre-training data).",
  "lessons_learned": "Fine-tuning helps for distant families but may not be necessary for well-represented families. GFP anomaly worth investigating.",
  "next_steps": ["Investigate GFP pre-training data overlap", "Run exp_0061: multi-family fine-tuning"],
  "hypothesis_update": "hyp_0017 confidence: 0.65 → 0.78",
  "artifacts": ["results/exp_0055/", "notebooks/exp_0055_analysis.ipynb"],
  "tags": ["fine-tuning", "protein-fitness", "generalization", "ESM-2"]
}
```

Store all experiments in `experiments.json` in the team workspace.

## Logging a New Experiment

When a user says "log this experiment" or provides results:

Ask for (or infer from context):
1. **Title**: What was tested?
2. **Hypothesis**: Which hypothesis does this test? (link to `hypothesis-versioning`)
3. **Purpose**: Why was this run? (1–2 sentences)
4. **Setup**: Model, dataset, baselines, metric, compute
5. **Results**: The numbers — be specific
6. **Findings**: What do the results mean? (interpretation, not just numbers)
7. **Lessons learned**: What would you do differently? What does this tell the team?
8. **Next steps**: What does this experiment suggest running next?

Create the record, confirm the ID, and ask if the linked hypothesis confidence should be updated.

## Looking Up Past Results

When asked "what did we find on X" or "have we tried Y":

1. Search experiments by: title keywords, tags, hypothesis link, date range, run_by
2. Return matching experiments sorted by relevance then recency
3. Format as a brief summary:

```
Matching experiments for "ESM-2 fine-tuning":

exp_0055 (2024-03-18, carol) — "Fine-tuning vs. zero-shot on 8 families"
  Result: Fine-tuned +0.12 Spearman vs. zero-shot; works on 7/8 families
  Key finding: GFP family is an exception — investigate data overlap

exp_0041 (2024-01-08, carol) — "Pilot fine-tuning on 3 families"
  Result: Fine-tuned +0.18 vs. base on pilot set
  Key finding: Initial signal — prompted hyp_0017

exp_0038 (2024-01-25, bob) — "Dropout ablation on contrastive LM"
  Result: No significant effect (Δ < 0.01) — led to abandoning hyp_0012
```

## Compiling Preliminary Data

When asked to compile preliminary data for a grant or paper:

1. Collect all experiments tagged as relevant (by hypothesis, tag, or date range)
2. Select the strongest, most complete results
3. Format as a preliminary data narrative:

```
## Preliminary Data: Protein Fitness Prediction

**Experiment 1** (exp_0041, January 2024): In an initial pilot across 3 protein families, 
homolog-fine-tuned ESM-2 outperformed the zero-shot baseline by 18% in Spearman correlation 
(0.61 vs. 0.43), suggesting that fine-tuning improves generalization to distant families.

**Experiment 2** (exp_0055, March 2024): In a more comprehensive evaluation across 8 DMS 
assays spanning diverse protein families, fine-tuned ESM-2 achieved mean Spearman ρ = 0.61 
(±0.08), outperforming zero-shot ESM-2 (0.49 ± 0.11) on 7 of 8 families and matching EVE 
[Notin et al., 2022] (0.58 ± 0.09) as the prior state-of-the-art.

Together, these results provide initial evidence that [hypothesis statement — from hyp_0017], 
motivating the proposed systematic investigation in Aim 2.
```

## Experiment Status Values

| Status | Meaning |
|--------|---------|
| `planned` | Queued; not yet run |
| `running` | Currently in progress |
| `completed` | Finished; results logged |
| `failed` | Experiment failed (infrastructure, bug, etc.) — log the failure reason |
| `abandoned` | Decided not to run — log the reason |

**Log failures** — "what didn't work" is as valuable as "what worked." A failed experiment is not a failed scientist.

## Reproducibility Fields

Every completed experiment should record:
- Exact model checkpoint or version
- Random seed(s) used
- Full hyperparameter set (not just the interesting ones)
- Environment: OS, GPU, library versions
- Path to artifacts: notebooks, scripts, raw outputs

This enables exact reproduction — by teammates, by future-you, and by reviewers.

## Integration Notes

- Link every experiment to a `hypothesis-versioning` record — experiments without hypotheses are data collection, not science
- Use `reproducibility-check` before manuscript submission to verify logs are complete
- Use `grant-writing` — preliminary data section pulls directly from `experiment-log`
- Use `claim-tracker` — strong experimental results that become paper claims should be registered there
