---
name: abstract-writing
description: Drafts venue-appropriate abstracts for papers, conference submissions, and grant applications at multiple word counts and formats. Use when the user needs to write or improve an abstract, needs a structured abstract for a journal, needs a conference submission abstract, or needs a lay summary. Triggers on phrases like "write an abstract", "draft the abstract", "abstract for our paper", "structured abstract", "lay summary", "plain language summary", "improve this abstract", "abstract for submission".
---

# Abstract Writing

The abstract is the most-read part of any paper. It must work as a standalone document — many readers will go no further.

## Abstract Types by Venue

### Unstructured (ML/CS venues: NeurIPS, ICML, ICLR, ACL, CVPR)
- Single continuous paragraph
- 150–250 words
- No section headers
- Lead with the problem, not the history
- Include: problem, approach, key result(s), significance

### Structured (Biomedical journals: Nature, PLOS, NEJM, etc.)
Explicit labeled sections:
- **Background**: 1–2 sentences establishing what is known and the gap
- **Methods**: 2–3 sentences describing what was done (not why)
- **Results**: 2–4 sentences of the key quantitative findings — be specific
- **Conclusions**: 1–2 sentences on what the results mean and their significance

### Extended Abstract (Workshops, symposia)
- 400–600 words
- Structured like a mini-paper: intro → method → results → conclusion
- Often includes 1 key figure or table

### Lay Summary (Public communication, press releases, grant summaries)
- 100–200 words
- No jargon — explain every technical term
- Lead with why it matters to the public, not what was done
- End with the practical implication

## Unstructured Abstract Formula (ML/CS)

```
[1–2 sentences: problem statement — what is hard and why it matters]
[1–2 sentences: prior work limitation — what fails and why]
[1–2 sentences: your approach — what you do differently]
[2–3 sentences: key results — specific numbers, benchmarks, comparisons]
[1 sentence: significance — what this enables]
```

**Example structure** (not content):
> "Predicting protein fitness from sequence is challenging because [difficulty]. Prior methods [limitation]. We propose [approach], which [mechanism]. On [benchmark], our method achieves [metric: number], outperforming [baseline] by [margin]. These results enable [application]."

## Rules for Strong Abstracts

**Do**:
- Lead with the problem, not the history of the field
- Include at least one specific quantitative result
- Use present tense for methods and results ("We propose", "We achieve")
- Make the contribution clear: what is new?
- Be specific: "15% improvement" beats "significant improvement"

**Don't**:
- Start with "In recent years..." or "With the advent of..."
- Use vague language: "good", "better", "improved" without numbers
- Bury the lede — the most important result goes near the end, not the last sentence
- Include citations (abstract should be self-contained)
- Use undefined acronyms on first use

## Improving an Existing Abstract

When given a draft abstract to improve:
1. Identify: what is the problem? contribution? key result? Is each present?
2. Check specificity: are results quantitative?
3. Check structure: does it flow problem → approach → results → significance?
4. Check length: within venue word limit?
5. Check tone: confident but not overclaiming?

Output: revised abstract + brief comment on what was changed and why.

## Multiple Variants

When asked for variants at different lengths or tones:

```
## Variant A (150 words — NeurIPS)
[unstructured, compressed]

## Variant B (250 words — ICML)
[unstructured, fuller]

## Variant C (structured, 200 words — PLOS Biology)
Background: ...
Methods: ...
Results: ...
Conclusions: ...

## Variant D (lay summary, 120 words)
[jargon-free, impact-first]
```

## Integration Notes

- Write the abstract last — after the paper is drafted, the contribution and results are clear
- Use `draft-generation` to produce the full paper first
- Use `evidence-grading` to calibrate result claims: don't overclaim preliminary results in the abstract
- For grants: NIH Specific Aims summary ≠ abstract; use `grant-writing` for that format
