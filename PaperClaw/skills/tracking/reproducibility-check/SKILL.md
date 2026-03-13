---
name: reproducibility-check
description: Runs a reproducibility checklist against a manuscript or experiment log before submission, verifying that methods are described sufficiently for replication and that results meet venue-specific reproducibility requirements. Use when the user is preparing a paper for submission and wants to verify reproducibility, when a reviewer has raised reproducibility concerns, or when the team wants to audit their experiment logs. Triggers on phrases like "reproducibility check", "submission checklist", "can someone reproduce this", "NeurIPS checklist", "ML reproducibility", "are our methods complete", "reviewer raised reproducibility", "methods section complete".
---

# Reproducibility Check

Verifies that a manuscript and its supporting materials meet reproducibility standards before submission. Catches gaps that reviewers and readers will find.

## Venue-Specific Checklists

### NeurIPS / ICML / ICLR (ML Reproducibility Checklist)

Required to be answered at submission. Run through each item:

**Claims:**
- [ ] All claims in the paper are supported by results in the paper or cited prior work
- [ ] Experimental results that cannot be reproduced by the provided code/data are clearly labeled as such
- [ ] For each theoretical claim, is there a proof or a clear pointer to a proof in the appendix?

**Experiments:**
- [ ] Are all datasets used publicly available OR is the data release plan specified?
- [ ] Are all baselines cited with the exact version/checkpoint used?
- [ ] Are hyperparameters reported for all experiments (not just the best-performing ones)?
- [ ] Is the number of random seeds reported, and are error bars / confidence intervals included?
- [ ] Is compute used (GPU type, GPU-hours, wall clock time) reported?
- [ ] If applicable: are training curves provided?

**Code:**
- [ ] Is code released or is a release date specified?
- [ ] Does released code include model checkpoints, or instructions to reproduce them?
- [ ] Is there a README with instructions to reproduce the main results?

**Human subjects / Ethics:**
- [ ] If human subjects are involved, is IRB approval stated?
- [ ] Are potential negative impacts or dual-use risks discussed?

### Nature / Nature Methods / Nature Machine Intelligence

**Data availability:**
- [ ] All data used in the study is deposited in a public repository OR a clear exception is stated
- [ ] Data DOIs or accession numbers are provided inline (not "available upon request")
- [ ] All processed data needed to reproduce figures is provided

**Code availability:**
- [ ] Analysis code is deposited in a public repository with a DOI or permanent link
- [ ] Exact software versions (including all dependencies) are specified

**Statistics:**
- [ ] Statistical tests are named and justified
- [ ] Sample sizes are reported with justification for adequacy (power analysis if applicable)
- [ ] Multiple comparison corrections are applied where needed and documented
- [ ] Effect sizes are reported, not just p-values

**Methods completeness:**
- [ ] Methods section is sufficient for an expert to reproduce the key experiment without contacting the authors
- [ ] Reagents, software, or equipment with potential ambiguity are identified with vendor + catalog number / version

### PLOS Computational Biology

- [ ] Software source code and documentation available under open license
- [ ] All datasets deposited in appropriate public repository
- [ ] Workflow can be reproduced from provided materials

## Methods Section Completeness Audit

When asked to audit a methods section, check each experiment for:

```
Experiment: [name]

✅ Model/algorithm specified with version or citation
✅ Dataset specified with source, size, train/val/test split
⚠️ Hyperparameters: learning rate reported, but weight decay missing
❌ Random seeds: not reported — add "We used seed 42 for all experiments"
⚠️ Compute: GPU type reported, but training time missing
✅ Baseline implementation: cited with code URL
❌ Evaluation metric: Spearman ρ described but aggregation across families not specified

Issues to fix before submission: 3 (2 warnings, 2 missing)
```

## Common Reproducibility Gaps

| Gap | How to Fix |
|-----|-----------|
| Missing hyperparameters | Add full hyperparameter table to appendix; all experiments, not just best |
| "Results may vary" | Report error bars: run ≥3 seeds, report mean ± std |
| "Available upon request" | Deposit in Zenodo, GitHub, or institutional repository before submission |
| Ambiguous baseline | Specify: "We use the official implementation at [URL], commit [hash]" |
| Missing compute | Report: GPU type × count × hours for each major experiment |
| Vague dataset split | Report exact N for train/val/test; if randomly split, report seed |
| Missing ablation details | Each ablation should have its own hyperparameter specification |

## Error Bars and Significance

Minimum standard for empirical ML papers (2024+):
- Report results over ≥3 random seeds
- Report mean ± standard deviation (or 95% CI)
- For small datasets: report over cross-validation folds
- For very expensive experiments (single run only): acknowledge this explicitly as a limitation

```
Bad: "Our method achieves 85.3% accuracy"
Good: "Our method achieves 85.3 ± 1.4% accuracy (mean ± std over 5 seeds)"
```

## Output: Reproducibility Report

```
## Reproducibility Check Report
Paper: [Title] | Target venue: NeurIPS 2024 | Date: [Date]

### Status: ⚠️ Not ready — 4 issues to fix

### Critical (must fix before submission)
❌ Random seeds not reported for Tables 2 and 3
❌ Dataset split for ProteinGym evaluation not specified (train/val/test proportions)

### Recommended (strongly encouraged by venue)
⚠️ Compute budget not reported — add GPU-hours for main experiments
⚠️ Code: repository exists but no README with reproduction instructions

### Passes
✅ All baselines cited with code and version
✅ Hyperparameters reported for all main experiments (Table A1)
✅ Dataset publicly available (ProteinGym — cite Notin et al. 2022)
✅ All claims traceable to results in the paper or cited work
```

## Integration Notes

- Run after `draft-generation` before submission — catches issues while revision is still easy
- Pull experiment metadata from `experiment-log` — reproducibility fields should already be logged there
- Address any `review-response` reproducibility concerns using this checklist
- For NeurIPS/ICML/ICLR: the checklist is mandatory at submission — run this early, not the night before
