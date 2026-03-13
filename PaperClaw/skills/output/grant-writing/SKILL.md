---
name: grant-writing
description: Generates agency-specific grant proposal sections grounded in the team's literature base and research history. Use when the user needs to write NIH Specific Aims, an NSF project description, a Significance or Innovation section, a grant background, preliminary data framing, or a broader impacts statement. Triggers on phrases like "write Specific Aims", "NIH grant", "NSF proposal", "grant background", "significance section", "innovation section", "preliminary data", "broader impacts", "write the approach section", "grant application".
---

# Grant Writing

Generates reviewer-calibrated grant sections grounded in the team's literature base. All claims trace to evidence; hedging language matches evidence grade.

## Agency-Specific Formats

### NIH (R01, R21, R03)

**Page limits**: R01 = 12 pages (Research Strategy); R21 = 6 pages; Specific Aims = 1 page always

**Specific Aims Page** (most important page — reviewers form their opinion here):
```
[Para 1 — Hook, 2–3 sentences]
The long-term goal of [lab/field] is to [broad goal]. [Disease/problem] affects [scale of impact].
Despite [prior progress], [the gap] remains a critical unmet need.

[Para 2 — Gap and opportunity, 3–5 sentences]  
[Establish what is known — consensus-mapping output]. However, [the key gap — gap-detection output].
[Your preliminary data or published work] suggests that [opportunity].

[Para 3 — Hypothesis and aims, 3–4 sentences]
Our central hypothesis is that [specific, testable hypothesis — hypothesis-versioning record].
We will test this hypothesis through three Specific Aims:

Aim 1: [Verb + outcome]. We will [action]. [Expected result].
Aim 2: [Verb + outcome]. We will [action]. [Expected result].  
Aim 3: [Verb + outcome]. We will [action]. [Expected result].

[Para 4 — Impact, 2–3 sentences]
Successful completion of these aims will [advance field / enable application / open new directions].
This work is significant because [patient/scientific/societal impact].
```

**Significance section**:
- Establish the problem's importance with data (statistics on disease burden, scientific importance)
- Show what is known (consensus-mapping → strong consensus statements)
- Show the gap (gap-detection → what hasn't been done)
- Explain why the gap matters (what harm results from the gap existing)
- End: "This application addresses a significant gap..."

**Innovation section**:
- Lead with: "This application is innovative because..."
- List 3–5 specific innovations — be concrete, not vague
- Compare to prior art: "Unlike [prior approaches], our method..."
- Use `claim-tracker` to verify innovation claims are accurate
- Distinguish conceptual innovation (new idea) from technical innovation (new method)

**Approach section**:
- One subsection per Aim
- Each subsection: Rationale → Preliminary Data → Methods → Expected Outcomes → Potential Problems and Alternative Approaches
- Preliminary Data: frames `experiment-log` results as proof-of-concept — use `evidence-grading` to calibrate claims

### NSF (BIO, CISE, MPS)

**Key differences from NIH**:
- No Specific Aims page — fold aims into Project Summary (1 page) + Project Description (15 pages)
- Broader Impacts is a separate required section — reviewers grade it independently
- Intellectual Merit framing: "How does this advance knowledge within the field?"
- NSF values: novelty, rigor, training, community benefit

**Project Summary** (1 page, 3 paragraphs):
1. Overview: what you're doing in plain language
2. Intellectual Merit: how this advances scientific knowledge
3. Broader Impacts: how this benefits society / trains next-gen researchers

**Broader Impacts section**:
- Training: how many students? what career stages? underrepresented groups?
- Dissemination: open-source code, datasets, workshops, curriculum
- Societal benefit: specific downstream application or policy relevance
- Be concrete — "We will train 3 PhD students and 6 undergraduates, prioritizing students from [groups]"

### ERC (Starting Grant, Consolidator, Advanced)

- State of the Art: similar to NIH Significance but more internationally comparative
- Beyond State of the Art: what will you do that nobody has done? (= Innovation)
- Methodology: approach section equivalent
- Ambition and feasibility: explicit risk/reward framing — ERC rewards bold claims

## Hedging Language for Preliminary Data

Use `evidence-grading` grades to calibrate confidence in preliminary results:

- Strong result (replicated, top venue): "Our published work demonstrates..." [cite]
- Single good experiment: "Our preliminary data show..." [cite internal]
- Exploratory experiment: "Initial experiments suggest..." 
- Computational prediction only: "Computational modeling predicts..." with "experimental validation planned in Aim X"

**Never claim preliminary data shows something it doesn't show.** Study sections are expert readers.

## Common Grant-Writing Mistakes to Avoid

- Vague aims: "We will study X" — fix: "We will identify the mechanism by which X does Y using Z"
- Missing alternative approaches: every Aim needs "If [approach fails], we will [alternative]"
- Overclaiming: "We will solve [grand problem]" — fix: "We will advance understanding of..."
- Ignoring page limits: always check current FOA for page limits; they change
- Writing to impress, not to convince: reviewers need to understand, not be impressed

## Integration Notes

- `gap-detection` → Significance section
- `consensus-mapping` → what can be stated as established vs. what needs hedging
- `evidence-grading` → calibrate preliminary data claims
- `hypothesis-versioning` → the central hypothesis statement
- `experiment-log` → preliminary data section
- Have a human expert review all sections before submission — regulatory and funding language evolves
