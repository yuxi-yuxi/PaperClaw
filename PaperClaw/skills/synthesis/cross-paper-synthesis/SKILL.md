---
name: cross-paper-synthesis
description: Synthesizes findings across multiple papers into a coherent narrative, structured comparison table, or temporal evolution story. Use when the user wants the "big picture" across a set of papers, needs a related work section that synthesizes rather than lists, wants to compare methods/models across papers in a table, or wants to understand how a field's thinking has evolved over time. Triggers on phrases like "synthesize these papers", "big picture", "how has this evolved", "compare these methods", "related work section", "what's the through line", "narrative synthesis".
---

# Cross-Paper Synthesis

Goes beyond summarizing individual papers to produce genuine synthesis — insights that only emerge from reading across the corpus as a whole. This is what distinguishes a great related work section from a list of paper descriptions.

## Synthesis Modes

### 1. Narrative Synthesis
A flowing prose account of what the literature says, organized by theme or argument — not by paper.

**Structure**:
- Open with what the field is trying to accomplish and why it's hard
- Trace the progression of approaches: what was tried first, what it revealed, what came next
- Identify the "through line" — the central insight that different papers keep rediscovering
- End with the current frontier and what remains open

**Avoid**: "Paper A does X. Then Paper B does Y. Paper C extends B by..."  
**Aim for**: "The field initially approached this as [framing]. This revealed [insight], prompting a shift toward [new framing]. The key advance came with [development], which established [principle]..."

### 2. Structured Comparison Table
A matrix of papers × dimensions — essential for methods sections and benchmarking papers.

**Useful dimensions**:
- Method / architecture
- Training data (size, source, modality)
- Evaluation benchmark(s) and metric(s)
- Key result(s)
- Limitations stated
- Code available? (Y/N + URL)

Output as Markdown table:
```
| Paper | Method | Data | Benchmark | Metric | Result | Code |
|-------|--------|------|-----------|--------|--------|------|
| Zhang et al. 2023 | Contrastive LM | UniRef50 (250M) | ProteinGym | Spearman ρ | 0.61 | ✅ |
| Jones et al. 2022 | Masked LM | UniRef90 (90M) | ProteinGym | Spearman ρ | 0.58 | ✅ |
```

### 3. Temporal Evolution
Shows how the field's understanding has progressed year by year. Useful for grant backgrounds and thesis introductions.

**Structure**:
```
[2019–2020] Foundational period
  Key papers: [X, Y]
  State of knowledge: ...
  Limiting assumption: ...

[2021–2022] Scaling era  
  Key papers: [A, B, C]
  Key advance: ...
  What changed: ...

[2023–present] Current frontier
  Key papers: [M, N]
  Open questions: ...
```

### 4. Cross-Domain Synthesis
Finds connections between papers from different fields that are solving related problems. Surfaces analogies, shared principles, and opportunities for cross-pollination.

## Identifying the "Through Line"

The through line is the single insight that unifies disparate work in a corpus. To find it:
1. List the main finding of each paper in one sentence
2. Look for the common thread — what principle, mechanism, or phenomenon do they all reveal?
3. Test it: does framing the synthesis around this principle make all the papers make more sense?

Example through line: "Across methods and domains, the papers collectively establish that structural information outperforms sequence-alone approaches for tasks requiring physical reasoning."

## Writing Style Rules

- Cite papers inline: `[Zhang et al., 2023]` or `[Zhang2023]`
- Never start a sentence with "This paper..." — start with the finding or argument
- Use present tense for claims: "Jones et al. show that..." not "showed"
- Vary sentence structure; avoid repetitive "X et al. found that..." constructions
- Every paragraph should make a point, not just report

## Length Guidelines

| Use case | Target length |
|----------|--------------|
| Related work section (conference) | 400–700 words |
| Related work section (journal) | 800–1500 words |
| Grant background | 200–400 words |
| Review article section | 1000–3000 words |

## Integration Notes

- Use `living-review` to build the paper corpus first
- Use `consensus-mapping` to distinguish what can be stated as settled vs. hedged
- Use `contradiction-detection` to correctly represent disagreements in the synthesis
- Output feeds directly into `draft-generation` for manuscript writing
