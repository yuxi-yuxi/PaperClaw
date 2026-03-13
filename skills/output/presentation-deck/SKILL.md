# Presentation Deck

## Overview
Generates structured slide outlines and content for research presentations — conference talks, lab meetings, thesis defenses, and invited seminars. Produces a narrative arc, slide-by-slide breakdown, and speaker notes grounded in the team's research and literature.

## When to Use
- User asks "help me structure my NeurIPS talk"
- User needs a 15-minute conference presentation outline
- User is preparing a thesis defense and needs slide structure
- User asks "what should I cover in a 30-minute seminar?"
- Lab member needs a presentation for a lab meeting on a paper or project

## Key Capabilities
- Generate a slide-by-slide outline calibrated to presentation duration (5 / 15 / 30 / 45 min)
- Identify the narrative arc: motivation → gap → contribution → method → results → impact
- Suggest which figures and tables to include and where
- Generate speaker notes for each slide
- Adapt structure to presentation type: conference talk, seminar, thesis defense, lab meeting
- Identify which literature to cite in the talk and where
- Generate a "story-first" version vs. "methods-first" version of the same content

## Usage Examples

### Generate conference talk outline
```python
presentation_deck.outline(
    paper_abstract="...",
    duration_minutes=15,
    conference="NeurIPS",
    style="story_first",
    include_speaker_notes=True
)
```

### Generate full slide content
```python
presentation_deck.generate(
    outline=presentation_deck.outline(...),
    paper_draft="[paste manuscript]",
    format="markdown_slides",  # markdown_slides | pptx_outline | beamer_latex
    include_figure_suggestions=True
)
```

### Generate lab meeting paper presentation
```python
presentation_deck.paper_talk(
    doi="10.48550/arXiv.1706.03762",
    duration_minutes=20,
    audience="own_lab",
    focus="critical_analysis"  # critical_analysis | overview | methods_deep_dive
)
```

## Output Format
Outlines are structured Markdown with slide titles, bullet points (3–5 per slide), and speaker notes. PPTX outline format is compatible with PowerPoint slide import. Beamer output is LaTeX-ready. Figure suggestions include slide number and description.

## Notes
- 15-minute conference talk: ~12 slides (1 min 15 sec/slide)
- 30-minute seminar: ~20–25 slides
- For paper presentations: always include a "what I'd do differently" or open questions slide — it drives discussion
- Combine with `cross-paper-synthesis` for related work slides and `gap-detection` for motivation slides
