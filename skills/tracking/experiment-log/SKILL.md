# Experiment Log

## Overview
Maintains a structured, searchable log of experiments — linking each run to the hypothesis it tests, the papers that motivated it, and the conclusions it produced. Provides a lightweight scientific notebook layer that integrates with PaperClaw's literature base.

## When to Use
- User wants to log an experiment and its results
- User asks "what experiments have we run on [hypothesis]?"
- User wants to link an experiment result to the papers that motivated it
- Lab is preparing a methods section and needs a log of what was actually run
- PI wants an overview of experimental progress on a project

## Key Capabilities
- Log experiments with: hypothesis ID, method description, config snapshot, results, and conclusions
- Link experiments to motivating papers and hypotheses
- Query experiments by outcome (positive / negative / inconclusive), hypothesis, or date range
- Generate a structured methods section from experiment log entries
- Flag experiments that contradict each other (same setup, different results)
- Export experiment log as a supplementary methods table

## Usage Examples

### Log a new experiment
```python
experiment_log.add(
    name="Contrastive Pretraining - UniRef50 Baseline",
    hypothesis_id="hyp_0042",
    method="ESM-2 650M with NT-Xent loss on UniRef50, evaluated on ProteinGym",
    config={"lr": 1e-4, "batch_size": 256, "epochs": 10, "temperature": 0.07},
    results={"spearman_rho": 0.61, "top10_recall": 0.43},
    conclusion="Modest improvement over ESM-2 baseline (0.58). Suggests pretraining helps.",
    run_by="bob",
    motivated_by=["DOI:10.1101/...", "hyp_0042"]
)
```

### Query experiments for a hypothesis
```python
experiment_log.query(
    hypothesis_id="hyp_0042",
    outcome="all",
    sort_by="date"
)
```

### Generate methods section from log
```python
experiment_log.to_methods(
    experiment_ids=["exp_001", "exp_003", "exp_007"],
    format="manuscript",
    include_ablations=True
)
```

### Find contradictory experiments
```python
experiment_log.find_contradictions(project="protein_fitness")
```

## Output Format
Experiment records contain: ID, name, date, hypothesis link, method description, config, results dict, conclusion, and run_by. Methods section output is structured prose. Contradictions report lists experiment pairs with conflicting results.

## Notes
- Config snapshots are stored as JSON — nested configs supported
- Results dict accepts any key-value pairs — no schema enforced
- For deep ML experiment tracking (GPU stats, loss curves, artifact versioning), use Weights & Biases or MLflow — this skill handles the scientific narrative layer, not the infrastructure layer
