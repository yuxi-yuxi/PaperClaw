# Reproducibility Check

## Overview
Evaluates the reproducibility of a paper or the team's own work against established reproducibility standards. Flags missing details, unavailable code/data, and underspecified methods before submission — catching issues reviewers will raise.

## When to Use
- User wants to check a paper before submission for reproducibility gaps
- User asks "can we reproduce [paper]?" before building on its results
- Lab wants to verify their manuscript meets reproducibility requirements of a target venue
- User is reviewing a paper and needs a reproducibility assessment
- Lab is responding to a reviewer concern about reproducibility

## Key Capabilities
- Check paper against venue-specific reproducibility checklists (NeurIPS, ICML, Nature, Science)
- Identify missing elements: random seeds, hyperparameters, dataset splits, hardware specs, compute budget
- Verify code availability claims (check GitHub links, Zenodo, etc.)
- Verify dataset availability (check Hugging Face, UCI, Zenodo, paper appendix)
- Score reproducibility on a structured rubric (0–10)
- Generate a checklist of fixes needed before submission
- Check against ML Reproducibility Challenge standards

## Usage Examples

### Check your own paper before submission
```python
reproducibility_check.check_manuscript(
    manuscript_text="[paste manuscript]",
    target_venue="NeurIPS",
    include_checklist=True
)
```

### Check if an external paper can be reproduced
```python
reproducibility_check.check_external(
    doi="10.48550/arXiv.2310.xxxxx",
    check_code_availability=True,
    check_data_availability=True
)
```

### Generate reproducibility checklist for a venue
```python
reproducibility_check.checklist(
    venue="NeurIPS",
    year=2024,
    format="markdown_checklist"
)
```

### Score reproducibility
```python
reproducibility_check.score(
    doi="10.48550/arXiv.2310.xxxxx",
    rubric="ml_reproducibility_challenge"
)
# Returns: {"score": 6.5/10, "breakdown": {...}, "critical_gaps": [...]}
```

## Output Format
Returns structured checklist with pass/fail per item, critical gaps flagged in red, and an overall reproducibility score. Fix recommendations are actionable: "Add random seed to Section 3.2" not "improve reproducibility."

## Notes
- Code availability is checked by attempting to resolve GitHub/Zenodo links — link rot is flagged
- Dataset availability is verified against known registries (HuggingFace, Zenodo, paperswithcode)
- NeurIPS 2024+ requires a mandatory reproducibility checklist at submission — this skill generates it
- Combine with `experiment-log` — well-logged experiments make reproducibility checks much easier to pass
