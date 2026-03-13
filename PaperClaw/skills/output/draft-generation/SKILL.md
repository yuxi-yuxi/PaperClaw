---
name: draft-generation
description: Generates manuscript sections grounded in the team's literature corpus — introductions, related work, methods, and discussion sections. All claims are citation-traced and calibrated to evidence grades. Use when the user wants a first draft of a paper section, needs a related work section written, wants to turn a living review into a manuscript draft, or needs an introduction framed around the research gap. Triggers on phrases like "write a draft", "draft the introduction", "write related work", "turn this into a paper section", "draft the methods", "write the discussion".
---

# Draft Generation

Produces manuscript sections grounded in the team's literature base. Every claim traces to a paper in the corpus. No hallucinated citations.

## Core Rule

**Never invent a citation.** If a claim cannot be traced to a paper in the team's corpus or a paper retrieved from Semantic Scholar / arXiv, either:
- Mark it as `[CITE NEEDED]` for the human to fill in
- Omit the claim
- State it without citation if it's genuinely uncontroversial background

## Section Types

### Introduction

Structure:
1. **Hook** (1–2 sentences): Why does this problem matter? Open with impact, not with history.
2. **Problem statement** (2–3 sentences): What specifically is the challenge? Be precise.
3. **Prior work + gap** (3–5 sentences): What has been done? What does it fail to do? Use `gap-detection` output here.
4. **Contribution statement** (2–3 sentences): What does THIS paper do? Be concrete: "We propose X, which Y, achieving Z."
5. **Paper outline** (optional, 1–2 sentences): Only include if the venue expects it.

**Tone**: Confident but not overclaiming. "We propose" not "We solve".

### Related Work

Use `cross-paper-synthesis` output as the foundation. Structure by theme, not by paper:

- Each paragraph should make a point about the literature, not describe a paper
- Group papers by what they have in common, not chronologically
- End each theme paragraph with a sentence that positions the current work relative to those papers
- Last paragraph: most closely related work and clear articulation of the distinction

**Bad**: "Smith et al. (2022) proposed method X. Jones et al. (2023) extended this with Y."  
**Good**: "Contrastive learning approaches [Smith 2022, Jones 2023, Lee 2024] have shown X but are limited by Y. Unlike these methods, our approach..."

### Methods

Write from the `experiment-log` and actual methods the team has implemented:
- Be precise about architecture, training procedure, datasets, hyperparameters
- Use present tense: "We train..." not "We trained..."
- Every design choice should have a rationale (performance, prior work, ablation result)
- Include pseudocode or algorithm blocks for novel procedures
- Flag placeholders: `[INSERT: dataset split details]`

### Discussion

Structure:
1. **What we found** (2–3 sentences): Restate key results without repeating the Results section verbatim
2. **Why it makes sense** (3–5 sentences): Mechanistic interpretation of the results
3. **Limitations** (3–5 sentences): Be honest; reviewers will find them if you don't
4. **Future work** (2–4 sentences): What would you do next? Make it concrete.
5. **Broader impact** (if required by venue): 2–3 sentences max

## Hedging Language Calibration

Apply `evidence-grading` scores to calibrate language:
- Grade A/B+ claims → state directly with citations
- Grade B claims → "has been shown to" / "demonstrates"
- Grade C (preprint) → "preliminary evidence suggests" / "initial results indicate"
- Grade D → "in an exploratory experiment" / "anecdotally"
- Your own unvalidated results → "we observe" / "we find" (not "we demonstrate" until peer-reviewed)

## Citation Format

Use author-year inline: `[Zhang et al., 2023]` or numbered `[42]` based on venue convention.

Append a `## References` block at the end with BibTeX-compatible entries:
```
[Zhang2023] Zhang, Y., et al. "Contrastive Protein LMs." NeurIPS 2023.
  DOI: 10.xxxx/...
```

## Placeholder Tags

Use these tags for content the human must fill in:
- `[FIGURE: description]` — where a figure should go
- `[TABLE: description]` — where a table should go
- `[RESULT: metric, value]` — where a quantitative result should go
- `[CITE NEEDED: claim]` — where a citation is required but not found
- `[EXPAND: topic]` — section that needs more detail from the team

## Length Targets by Venue

| Venue | Introduction | Related Work | Methods | Discussion |
|-------|-------------|--------------|---------|------------|
| NeurIPS/ICML/ICLR | 400–600w | 400–600w | 600–1000w | 300–500w |
| Nature / Science | 600–900w | integrated | 800–1500w | 500–800w |
| PLOS / journal | 500–800w | 600–1000w | 1000–2000w | 600–1000w |
| arXiv preprint | flexible | flexible | flexible | flexible |

## Integration Notes

- Run `living-review` first — the synthesis is the raw material for draft generation
- Run `gap-detection` — gap analysis drives the introduction and significance framing
- Run `cross-paper-synthesis` for the related work section
- Run `evidence-grading` to calibrate hedging language throughout
- After drafting, run `reproducibility-check` to verify the methods section is complete
