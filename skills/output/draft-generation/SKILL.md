# Draft Generation

## Overview
Generates structured manuscript drafts — or specific sections — grounded in the team's literature base. Unlike generic AI writing, draft generation in PaperClaw is citation-aware, claim-traced, and calibrated to the evidence grades of the underlying papers.

## When to Use
- User asks "write a draft introduction for our paper on [topic]"
- User wants a related work section that synthesizes, not just lists
- User needs a first draft of a methods section based on prior work
- User asks "turn our living review into a manuscript draft"
- Lab wants to generate a first pass at a paper to react to and refine

## Key Capabilities
- Generate full paper sections: introduction, related work, methods, discussion
- Ground all claims in team's literature corpus — no hallucinated citations
- Calibrate claim confidence to evidence grades from `evidence-grading`
- Apply hedging language automatically for preliminary findings
- Match target venue style (NeurIPS, Nature, PNAS, ICML, etc.)
- Insert placeholder tags for figures, tables, and results not yet available
- Generate an outline first and await approval before expanding

## Usage Examples

### Generate a related work section
```python
draft_generation.related_work(
    topic="contrastive learning for protein representation",
    corpus=review.get_papers(),
    target_venue="NeurIPS",
    max_words=800,
    style="synthesizing"  # synthesizing | chronological | thematic
)
```

### Generate introduction from living review
```python
draft_generation.introduction(
    living_review=review.export(),
    research_question="Can self-supervised protein LMs generalize to low-data fitness prediction?",
    target_venue="Nature Methods",
    max_words=600
)
```

### Generate full paper outline
```python
draft_generation.outline(
    title="Proposed title here",
    abstract="Proposed abstract here",
    target_venue="ICML",
    await_approval=True
)
```

## Output Format
All output is structured Markdown with inline citations in the format `[AuthorYear]`. A reference list is appended. Placeholder tags use `[FIGURE: description]` and `[RESULT: metric]` syntax. Evidence grade annotations included in a review mode.

## Notes
- All citations are verified against the team's corpus — no fabricated references
- Always review AI-generated drafts carefully: structure and flow are strong, factual nuance requires human review
- Combine with `cross-paper-synthesis` for the related work section and `gap-detection` for the motivation/novelty framing
