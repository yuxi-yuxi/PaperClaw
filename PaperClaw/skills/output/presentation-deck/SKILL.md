---
name: presentation-deck
description: Generates slide outlines, content, and speaker notes for research presentations including conference talks, lab meetings, thesis defenses, and invited seminars. Use when the user needs to structure a presentation, wants slide-by-slide content for a talk, needs discussion questions for a paper presentation, or wants speaker notes. Triggers on phrases like "help me structure my talk", "slide outline", "conference presentation", "lab meeting slides", "thesis defense", "paper presentation slides", "speaker notes", "15-minute talk", "how many slides".
---

# Presentation Deck

Research presentations are arguments, not recitations. Every slide serves the argument. Every minute is allocated deliberately.

## Slide Count by Duration

| Duration | Slides | Pace |
|----------|--------|------|
| 5 min (lightning) | 5–7 | ~45 sec/slide |
| 10 min (short talk) | 8–10 | ~60 sec/slide |
| 15 min (conference) | 10–13 | ~70 sec/slide |
| 20 min (conference) | 14–18 | ~70 sec/slide |
| 30 min (seminar) | 20–25 | ~75 sec/slide |
| 45 min (invited) | 28–35 | ~80 sec/slide |
| 60 min (thesis/job talk) | 35–45 | ~80 sec/slide |

## Standard Conference Talk Structure (15 min / 12 slides)

```
Slide 1: Title + authors (shown during intro, 0 time)
Slide 2: Motivation — why does this problem matter? (90 sec)
Slide 3: The core difficulty — what makes it hard? (60 sec)
Slide 4: Prior work + gap — what's been tried and where it fails (90 sec)
Slide 5: Our approach — key idea in one sentence + diagram (90 sec)
Slide 6: Method — how it works (diagram-heavy) (90 sec)
Slide 7: Method detail — key technical component (60 sec)
Slide 8: Experimental setup — datasets, baselines, metrics (45 sec)
Slide 9: Main results — the key table or figure (90 sec)
Slide 10: Analysis / ablation — why does it work? (60 sec)
Slide 11: Limitations + future work (45 sec)
Slide 12: Conclusion + takeaways (45 sec) [+ backup slides]
```

Total: ~12 min of content + 3 min Q&A buffer

## Slide Content Rules

**One claim per slide**: Every slide makes exactly one point. State it in the slide title.

**Bad title**: "Experiments"  
**Good title**: "Our method outperforms all baselines on ProteinGym"

**Diagram over text**: If something can be shown, show it. Bullet points are a last resort.

**Key result slide**: Show ONE number prominently. Don't show the full 12-column table.
- Bold or highlight the cells that matter
- Annotate with arrows: "15% improvement over best baseline"

**Readable from the back**: Minimum 24pt font. No full sentences. Max 6 words per bullet.

## Generating a Slide Outline

When asked to generate a talk outline, produce:

```
## Talk Outline: [Title] — [Duration] minutes

**Narrative arc**: [One sentence describing the story the talk tells]

---

Slide 1 — Title
  Content: Title, authors, affiliations, date/venue
  Speaker note: "Good [morning/afternoon]. I'm going to talk about [one sentence summary]."

Slide 2 — Motivation
  Claim: [What makes this problem important and urgent]
  Content: [Striking statistic or visual that establishes stakes]
  Speaker note: [Suggested opening for this slide]

Slide 3 — The Hard Part
  Claim: [The specific technical challenge]
  Content: [Diagram or example showing why it's hard]
  Speaker note: ...

[Continue for all slides]

---

Backup slides (optional):
  - Technical proof / derivation
  - Additional ablation results  
  - Dataset statistics
  - Comparison to additional baselines
```

## Paper Presentation (Lab Meeting)

When asked to present a paper the user hasn't written:

```
## Paper Presentation: [Title] — 20 minutes

Slide 1: Title + your reaction (why are you presenting this?)
Slide 2: Problem + motivation (2 min)
Slide 3: Prior work this builds on (2 min)
Slide 4: Key idea / contribution (2 min)
Slide 5: Method overview (3 min)
Slide 6: Key result (2 min)
Slide 7: Ablation / analysis (2 min)
Slide 8: Limitations — what doesn't this do? (2 min)
Slide 9: Your take + discussion questions (5 min)

Discussion questions (last slide):
  1. [Comprehension question — did we understand the method?]
  2. [Critical question — what's the biggest weakness?]
  3. [Relevance question — how does this affect our work?]
  4. [Extension question — what would you do next?]
```

## Speaker Notes Format

For each slide, produce:
- **What to say**: The spoken version of the slide's claim (2–4 sentences)
- **Transition**: The bridge to the next slide ("So with that context...")
- **Time target**: How long to spend (e.g., "~60 seconds")

## Thesis Defense Structure (45–60 min)

```
1. Introduction + motivation (5 min)
2. Background — prior work (5 min)  
3. Chapter 1 — first contribution (10 min)
4. Chapter 2 — second contribution (10 min)
5. Chapter 3 — third contribution (10 min)
6. Synthesis — how contributions fit together (5 min)
7. Future work (3 min)
8. Conclusion (2 min)
[+ 20–30 min Q&A]
```

Committee questions to prepare for (add to backup slides):
- "Why did you use [method] instead of [alternative]?"
- "How does this generalize beyond your test cases?"
- "What's the most important limitation of your work?"
- "What would you do differently if starting over?"

## Integration Notes

- Use `cross-paper-synthesis` output for the Prior Work + Gap slides
- Use `gap-detection` output for the Motivation slide (what problem exists)
- Use `experiment-log` for the Experimental Setup slide
- Use `evidence-grading` to calibrate result claims in speaker notes
