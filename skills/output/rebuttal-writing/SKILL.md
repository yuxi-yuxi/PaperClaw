# Rebuttal Writing

## Overview
Drafts concise, strategic rebuttals for conference paper reviews under tight word limits. Optimized for the specific constraints of ML/CS conference rebuttal periods (NeurIPS, ICML, ICLR, ACL, etc.) where brevity, clarity, and prioritization are critical.

## When to Use
- User has received conference reviews and needs a rebuttal draft
- User asks "how do I respond to this reviewer in 500 words?"
- User wants to prioritize which concerns to address in a rebuttal
- Lab is preparing for NeurIPS / ICML / ICLR author response period
- User needs help deciding what can be addressed vs. what requires new experiments

## Key Capabilities
- Parse and rank reviewer concerns by impact on accept/reject decision
- Draft concise point responses within strict word budgets (NeurIPS: 500 words, ICLR: unlimited, etc.)
- Identify "fatal flaw" concerns that must be addressed vs. minor concerns to acknowledge briefly
- Suggest which concerns to push back on vs. accept
- Draft responses that promise specific additions to the paper revision
- Generate a strategy document before drafting: "here's how we recommend allocating your word budget"

## Usage Examples

### Draft a full conference rebuttal
```python
rebuttal_writing.draft(
    reviews={"R1": "...", "R2": "...", "R3": "..."},
    paper_abstract="...",
    conference="NeurIPS",
    word_limit=500,
    strategy="address_fatal_flaws_first"
)
```

### Generate rebuttal strategy first
```python
rebuttal_writing.strategy(
    reviews={"R1": "...", "R2": "...", "R3": "..."},
    conference="ICML",
    output=["concern_ranking", "word_budget_recommendation", "pushback_opportunities"]
)
```

### Draft response to a single critical concern
```python
rebuttal_writing.single_response(
    concern="The comparison to baseline X is unfair because different hyperparameter budgets were used",
    response_budget=80,  # words
    supporting_evidence="We used the same compute budget as reported in [BaselineX paper] Appendix B"
)
```

## Output Format
Strategy document is a prioritized table with: concern, severity, recommended response type, word budget. Rebuttal draft is plain text respecting word limits, structured as numbered responses. Each response is ≤ allocated word budget.

## Notes
- NeurIPS/ICML rebuttals: prioritize fatal flaws, be extremely concise, promise specific revisions
- ICLR rebuttals: more space for detailed responses, engage with all substantive concerns
- Do NOT promise experiments in the rebuttal that cannot realistically be completed before the camera-ready deadline
- Combine with `review-response` for the full revision cycle after acceptance
