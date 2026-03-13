# Grant Writing

## Overview
Generates grant proposal sections grounded in the team's literature base and research history. Produces agency-specific, reviewer-calibrated content for Specific Aims, Significance, Innovation, and Approach sections — with all claims traced to evidence in the team's corpus.

## When to Use
- User asks "help write our NIH Specific Aims"
- User needs a Significance section that establishes the gap in prior work
- User wants an Innovation section that positions the work relative to the literature
- User asks "what's our preliminary evidence?" and needs it packaged for a grant
- Lab is applying to NSF, NIH, ERC, Wellcome, or private foundations

## Key Capabilities
- Generate agency-specific sections: NIH (R01, R21), NSF (BIO/CISE/MPS), ERC, Wellcome, DARPA
- Significance section grounded in team's gap analysis and consensus map
- Innovation section positioned against literature and prior art
- Approach section with milestone timeline and risk/mitigation framing
- Specific Aims page (NIH): 1-page format with hook, gap, hypothesis, aims, significance
- Integrate team's own published work as preliminary evidence
- Calibrate hedging language to evidence grades throughout

## Usage Examples

### Generate NIH Specific Aims page
```python
grant_writing.specific_aims(
    research_question="Develop self-supervised models for low-data protein fitness prediction",
    aims=["Aim 1: ...", "Aim 2: ...", "Aim 3: ..."],
    corpus=review.get_papers(),
    agency="NIH",
    mechanism="R01",
    max_words=600
)
```

### Generate Significance and Innovation sections
```python
grant_writing.significance_innovation(
    topic="federated learning for rare disease genomics",
    gap_analysis=gap_detection.analyze(...),
    consensus_map=consensus_mapping.build(...),
    agency="NIH",
    max_words={"significance": 400, "innovation": 300}
)
```

### Generate NSF broader impacts section
```python
grant_writing.broader_impacts(
    research_description="...",
    team_background="...",
    agency="NSF",
    max_words=300
)
```

## Output Format
All sections output as plain text formatted to agency page limits. NIH sections follow SF424 formatting conventions. Inline citations formatted per agency style. Evidence grades annotated in review mode for PI to verify before submission.

## Notes
- Always have a human expert review grant drafts — regulatory and agency language evolves frequently
- Combine with `gap-detection` for Significance and `evidence-grading` for Approach
- Budget sections, biosketches, and facilities pages are out of scope — draft generation covers scientific narrative only
