# Abstract Writing

## Overview
Drafts structured, venue-appropriate abstracts for papers, conference submissions, and grant applications. Generates multiple variants calibrated to different audiences, word limits, and structural conventions.

## When to Use
- User asks "write an abstract for our paper"
- User needs a conference submission abstract (NeurIPS, ICML, ICLR, etc.)
- User wants a structured abstract for a journal (Background / Methods / Results / Conclusions)
- User has a draft abstract and wants it improved
- Lab needs a short lay summary or public-facing abstract

## Key Capabilities
- Generate abstracts from: title + bullet points, draft manuscript, or living review summary
- Structured abstract format: Background, Objective, Methods, Results, Conclusions
- Unstructured narrative format for ML/CS venues
- Lay summary format for public communication or press releases
- Generate multiple variants at different word counts (150, 250, 350 words)
- Calibrate technical density to target audience (expert / general / lay)
- Ensure abstract structure follows IMRaD conventions

## Usage Examples

### Generate abstract from key points
```python
abstract_writing.from_bullets(
    title="Self-supervised protein language models for low-data fitness prediction",
    key_points=[
        "Problem: fitness prediction is data-scarce",
        "Method: contrastive pretraining on UniRef90",
        "Result: 15% improvement over fine-tuned ESM-2 on low-data benchmarks",
        "Significance: enables fitness prediction for orphan proteins"
    ],
    target_venue="Nature Methods",
    max_words=250
)
```

### Improve an existing abstract
```python
abstract_writing.improve(
    draft_abstract="[paste current abstract]",
    issues=["too vague on results", "no clear contribution statement"],
    max_words=200
)
```

### Generate lay summary
```python
abstract_writing.lay_summary(
    technical_abstract="[paste abstract]",
    audience="science journalist",
    max_words=150
)
```

## Output Format
Returns abstract text ready to paste. Multiple variants returned as a numbered list when requested. Lay summaries avoid jargon and explain all technical terms.

## Notes
- For structured abstracts: always include quantitative results in the Results field — reviewers expect them
- NeurIPS/ICML/ICLR abstracts: unstructured, emphasize novelty and significance upfront
- Combine with `draft-generation` — abstract should be written last, after the paper draft is complete
