---
name: consensus-mapping
description: Maps what the scientific field broadly agrees on versus what remains contested or debated. Use when the user wants to establish prior art for a grant or paper, needs to know which claims can be stated as settled versus hedged, wants to understand the "state of the field", or is writing a background section and needs to distinguish established knowledge from open questions. Triggers on phrases like "what does the field agree on", "is this well-established", "settled science", "state of the field", "what's consensus on X", "is X debated", "background section".
---

# Consensus Mapping

Produces a structured "state of knowledge" map — separating what the field has settled from what remains actively debated. Essential for writing credible grant backgrounds and manuscript introductions.

## Consensus Levels

| Level | Agreement Rate | Label | Usage |
|-------|---------------|-------|-------|
| **Strong consensus** | ≥85% of papers agree | "It is established that..." | State as fact; cite 2–3 papers |
| **Emerging consensus** | 65–84% | "Evidence suggests..." | State with moderate confidence |
| **Contested** | 40–64% | "Results are mixed..." | Present both sides |
| **No consensus** | <40% or actively debated | "It remains unclear..." | Acknowledge debate |
| **Settled by meta-analysis** | Supported by systematic review | "Meta-analyses confirm..." | Highest confidence |

## Measurement Approach

For a given claim across N papers covering the topic:
1. Count how many papers assert the claim (P), negate it (N), or are neutral/silent (S)
2. Agreement rate = P / (P + N), excluding neutral/silent
3. Weight by: recency (newer papers count more), citation count, venue prestige
4. If a meta-analysis or systematic review exists → override individual paper scores

## Recency Weighting

Fields move fast. A claim that was contested in 2020 may be settled in 2024, or vice versa:
- Papers from the last 2 years: weight × 1.5
- Papers from 3–5 years ago: weight × 1.0  
- Papers 6–10 years old: weight × 0.7
- Papers >10 years old: weight × 0.4 (unless foundational/seminal)

## Output: Consensus Map

```
## Consensus Map: Self-supervised Learning for Protein Representation

### Strong Consensus (≥85%)
✅ Pre-training on large protein sequence databases improves downstream task performance
   → Agreement: 91% (31/34 papers) | Evidence: [Rives 2021, Lin 2023, +29]

✅ Larger protein LMs generally learn better representations than smaller ones
   → Agreement: 87% (26/30 papers) | Evidence: [Elnaggar 2021, Lin 2023, +24]

### Emerging Consensus (65–84%)
🔶 Evolutionary information (MSA) improves structure-related tasks over sequence-only models
   → Agreement: 74% (20/27 papers) | Evidence: [Rao 2021, +19] | Dissent: [Su 2023, +6]

### Contested (40–64%)
⚔️ Contrastive pretraining outperforms masked language modeling for fitness prediction
   → Agreement: 52% (11/21 papers) | Evidence split; likely task/regime dependent

### No Consensus / Open Question
❓ Whether protein LMs "understand" physical chemistry or merely statistical patterns
   → Empirical evidence exists on both sides; mechanistic understanding lacking
```

## Generating Background Section Prose

When asked to write a background for a grant or paper, convert the consensus map to prose:

**Strong consensus** → state as established fact with 1–2 citations  
**Emerging consensus** → "A growing body of evidence suggests..." with caveats  
**Contested** → "Results are mixed: [Side A, citations] while [Side B, citations]"  
**Open question** → use to motivate the proposed work: "It remains unclear whether..."

## Identifying Temporal Shifts

When a claim's consensus status has shifted over time, flag it:
> "⚠️ This was considered settled in 2020 (8/8 papers agreed) but has been contested since 2022 following [Paper X]. Current status: Contested."

## Integration Notes

- Run after `living-review` builds the corpus — consensus analysis requires a reasonable sample of papers
- Use `contradiction-detection` to find the specific papers on each side of contested claims
- Use `evidence-grading` to assess quality of papers on each side
- Output feeds directly into `grant-writing` and `draft-generation` background sections
