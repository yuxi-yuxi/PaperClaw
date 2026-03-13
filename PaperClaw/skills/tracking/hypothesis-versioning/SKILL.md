---
name: hypothesis-versioning
description: Maintains a version-controlled registry of the team's active research hypotheses, tracking how confidence evolves as evidence accumulates. Use when the user wants to register a new hypothesis, update confidence in a hypothesis after new results, review which hypotheses are active or have been refuted, trace what evidence supports or challenges a hypothesis, or document why a hypothesis was abandoned. Triggers on phrases like "register this hypothesis", "our working hypothesis", "update confidence", "track this hypothesis", "which hypotheses are active", "hypothesis log", "what's the evidence for", "why did we abandon".
---

# Hypothesis Versioning

A version-controlled record of every research hypothesis the team has held — what was claimed, when, with what confidence, and how that confidence changed over time. Acts as the team's scientific memory.

## Hypothesis Data Model

```json
{
  "id": "hyp_0017",
  "statement": "Homolog fine-tuning is necessary for generalization to distant protein families",
  "registered_by": "alice",
  "registered_date": "2024-01-10",
  "owner": "carol",
  "status": "active",
  "confidence": 0.65,
  "rationale": "ESM-2 without fine-tuning drops 18% on out-of-family proteins in our pilot",
  "supporting_evidence": [
    {
      "type": "experiment",
      "ref": "exp_0041",
      "description": "Pilot on 3 protein families: fine-tuned model +18% vs. base model",
      "date": "2024-01-08",
      "effect": "+0.10 confidence"
    },
    {
      "type": "paper",
      "ref": "DOI:10.xxxx/...",
      "description": "Rao et al. 2021 show MSA-based fine-tuning helps for remote homologs",
      "effect": "+0.05 confidence"
    }
  ],
  "challenging_evidence": [
    {
      "type": "paper",
      "ref": "arXiv:2401.12345",
      "description": "Su et al. 2024 show zero-shot ESM-2 competitive on ProteinGym families",
      "effect": "-0.08 confidence"
    }
  ],
  "history": [
    {"date": "2024-01-10", "confidence": 0.60, "event": "Registered after pilot experiment"},
    {"date": "2024-02-01", "confidence": 0.70, "event": "Rao et al. paper supports this"},
    {"date": "2024-03-05", "confidence": 0.65, "event": "Su et al. preprint partially challenges this"}
  ],
  "related_hypotheses": ["hyp_0012", "hyp_0019"],
  "experiments_planned": ["exp_0055"]
}
```

Store hypotheses in `hypotheses.json` in the team workspace.

## Registering a New Hypothesis

When a user states a new hypothesis, prompt for:
1. **Statement**: The specific, testable claim (not vague: "X is better" → "X achieves higher Spearman ρ than Y on ProteinGym under low-data conditions")
2. **Rationale**: Why do you believe this? What observation prompted it?
3. **Initial confidence**: 0.0–1.0 scale (0.5 = coin flip; 0.7 = reasonably confident; 0.9 = strong prior evidence)
4. **Owner**: Who is responsible for testing this?
5. **Falsification criteria**: What result would make you abandon this hypothesis?

Create a new hypothesis record and confirm:
```
✅ Registered hyp_0017: "Homolog fine-tuning is necessary for generalization..."
   Owner: carol | Confidence: 0.65 | Status: active
   Falsification: "If zero-shot ESM-2 ≥ fine-tuned model on 5+ protein families"
```

## Updating Confidence

When a user reports new evidence (experiment result or new paper):

1. Add the evidence to `supporting_evidence` or `challenging_evidence`
2. Estimate the confidence delta (ask user or infer from effect size)
3. Update `confidence` and append to `history`
4. If confidence drops below 0.2 → suggest marking as `unlikely`
5. If confidence rises above 0.85 → suggest marking as `confirmed`

```
Updated hyp_0017:
  New evidence: exp_0055 results — fine-tuned model beats zero-shot on 7/8 families
  Confidence: 0.65 → 0.78 (+0.13)
  History entry added: "2024-03-20 — Comprehensive experiment supports hypothesis"
```

## Hypothesis Status Values

| Status | Confidence | Meaning |
|--------|-----------|---------|
| `active` | 0.3–0.85 | Currently being tested; evidence mixed or incomplete |
| `confirmed` | >0.85 | Sufficient evidence to accept; still track |
| `unlikely` | 0.1–0.3 | Evidence leans against; deprioritized |
| `abandoned` | any | Explicitly abandoned with documented reason |
| `refuted` | <0.1 | Clear evidence against; archived |

## Hypothesis Inventory

When asked for the current hypothesis status:

```
## Active Hypotheses — [Date]

🟢 CONFIRMED (confidence >0.85)
  hyp_0009 | Contrastive pretraining improves low-data fitness prediction | 0.88
            Owner: alice | Confirmed: 2024-02-10

🟡 ACTIVE (confidence 0.3–0.85)
  hyp_0017 | Homolog fine-tuning necessary for generalization | 0.78 ↑
            Owner: carol | Next experiment: exp_0061
  hyp_0019 | Evolutionary depth correlates with representation quality | 0.62 →
            Owner: bob | No experiment planned yet

🔴 UNLIKELY / ABANDONED
  hyp_0012 | Dropout improves contrastive LM training | 0.22 ↓
            Abandoned: 2024-01-30 | Reason: exp_0038 showed no effect
```

## Falsification Criteria

Every hypothesis should have a falsification criterion — the result that would cause the team to abandon it. This prevents motivated reasoning and scope creep.

If a hypothesis was registered without falsification criteria, prompt:
> "What result in exp_0055 would make you abandon hyp_0017?"

## Linking to Experiments and Papers

- When running an experiment relevant to a hypothesis → link `exp_id` to the hypothesis
- When reading a paper that bears on a hypothesis → add it to `supporting_evidence` or `challenging_evidence`
- Confidence deltas from papers should be smaller than from experiments (indirect evidence)

## Integration Notes

- Use `experiment-log` to track the experiments that test each hypothesis
- Use `claim-tracker` when a confirmed hypothesis becomes a claim asserted in a paper
- Use `evidence-grading` to weight how much a paper should shift confidence
- Use `grant-writing` — the central hypothesis from `hypothesis-versioning` is the grant's central hypothesis
- Abandoned/refuted hypotheses feed `gap-detection` (you explored that direction; it didn't work)
