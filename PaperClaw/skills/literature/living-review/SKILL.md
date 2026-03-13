---
name: living-review
description: Maintains a continuously updated, structured literature review for a research team. Use when the user wants to add papers to a shared review, generate or update a literature review document, summarize what the team has collectively read on a topic, prepare an introduction or related work section, or onboard a new team member with a fast overview of prior work. Triggers on phrases like "update our lit review", "add this paper to the review", "what do we know about X", "summarize the papers on", "generate a related work section".
---

# Living Review

A living literature review is a continuously updated document that synthesizes a team's collective reading into a structured, versioned knowledge base. Unlike a static review written once and forgotten, it evolves as new papers are added, existing understanding is revised, and the field advances.

## How It Works

Papers are ingested from PDFs, DOIs, arXiv IDs, or PubMed IDs. For each paper, extract:
- **Key claims**: The central empirical or theoretical assertions
- **Methods**: What approach was used, on what data, with what evaluation
- **Limitations**: What the authors or reviewers identify as gaps
- **Relation to other work**: How this paper extends, challenges, or replaces prior work

Group papers into thematic clusters and maintain a structured synthesis per cluster.

## Generating the Review Draft

When asked to generate or update a review, produce a structured Markdown document with:

1. **Background** — Foundational concepts and established results
2. **Key Methods** — Dominant methodological approaches and their tradeoffs
3. **Datasets & Benchmarks** — What the community uses to evaluate progress
4. **Contested Points** — Where papers disagree or results conflict
5. **Open Questions** — Gaps, unanswered questions, future directions
6. **Recent Additions** — Papers added since the last version (with dates)

Every claim should be traceable to at least one paper. Use inline citations: `[AuthorYear]`.

## Adding a Paper

When a user provides a paper (PDF, DOI, arXiv ID, URL, or title):
1. Extract or look up: title, authors, year, venue, abstract
2. Identify key claims, methods, datasets, and stated limitations
3. Tag the paper with relevant topics
4. Place it in the appropriate thematic cluster
5. Update the synthesis for that cluster
6. Note who added it and when

## Team Annotations

Preserve all team notes and annotations — never overwrite them during updates. When generating the review, surface annotations inline as callouts:
> 💬 **Alice (2024-03-10):** "This benchmark is saturated — we need a harder evaluation."

## Diffing the Review

When asked what changed since a date or since the last version:
- List newly added papers with one-line summaries
- Highlight any updated claims or shifted consensus
- Flag any papers that were challenged or retracted

## Export Formats

- **Markdown**: Default. Structured sections with inline citations.
- **LaTeX**: Use `\cite{key}` format with a BibTeX block appended.
- **BibTeX only**: Export all papers in BibTeX format for manuscript preparation.

## Integration Notes

- Works best combined with `arxiv-monitor` for automatic new paper discovery
- Use `gap-detection` after generating a review to identify what hasn't been studied
- Use `contradiction-detection` to flag conflicting claims across the corpus
- Use `cross-paper-synthesis` to deepen any thematic cluster into a narrative synthesis
