---
name: lab-knowledge-handoff
description: Packages a departing team member's knowledge — reading history, annotations, expertise, and open threads — into a structured handoff document for the lab. Use when a student is graduating, a postdoc is moving on, a collaborator is leaving a project, or a PI wants to archive what a team member knew before they go. Also use when onboarding someone new to a project previously owned by another person. Triggers on phrases like "X is leaving", "graduating soon", "knowledge handoff", "offboarding", "onboarding to X's project", "what did X know", "archive before they leave".
---

# Lab Knowledge Handoff

Prevents institutional knowledge loss when team members leave. Produces a comprehensive, structured handoff package that the lab retains permanently.

## When to Run

Run this skill **2–4 weeks before** the member departs — early enough to allow gaps to be addressed in conversation before they leave.

## Handoff Package Contents

A complete handoff package contains:

1. **Expertise Portrait** — What topics they knew deeply, from `expertise-mapping`
2. **Reading Summary** — Papers they read that no one else has, from `reading-coverage`
3. **Annotation Archive** — Their annotations and discussion threads, from `annotation-sharing`
4. **Open Threads** — Unresolved questions they were tracking, from `claim-tracker` and `hypothesis-versioning`
5. **Experiment Log Summary** — Experiments they ran and what was learned, from `experiment-log`
6. **Tacit Knowledge Interview** — A structured questionnaire to capture what's not written down
7. **Successor Onboarding Guide** — A curated reading list and orientation for their successor

## Step 1: Expertise Portrait

Pull from `expertise-mapping`:
- Top 5 topics by expertise score with evidence
- Unique papers they added to the library that others didn't read
- Annotations and discussion threads they initiated

```
## Alice's Expertise Portrait

Top areas:
  1. Protein fitness prediction (score: 0.92) — 31 papers, 180+ annotations
  2. Contrastive learning (score: 0.78) — 22 papers, 94 annotations
  3. Low-data learning (score: 0.71) — 18 papers, 67 annotations

Unique papers (only Alice has read):
  - [Notin et al. 2023] EVE model for fitness prediction — HIGH PRIORITY for others to read
  - [Trinquier et al. 2021] Efficient generative modeling of protein sequences
  - [+12 more papers]
```

## Step 2: Open Threads

Pull unresolved items from:
- `claim-tracker`: claims registered by this member still marked `standing` or `challenged`
- `hypothesis-versioning`: hypotheses they owned still marked `active`
- `annotation-sharing`: annotation threads with no resolution

Format as an action list for the PI and successor:

```
## Open Threads Alice Leaves Behind

Claims to monitor:
  ☐ claim_0042 — "Contrastive pretraining outperforms MLM for fitness" — currently STANDING
    → Alice was tracking follow-up papers; assign to Carol

Hypotheses:
  ☐ hyp_0017 — "Homolog fine-tuning is necessary for generalization" — ACTIVE, confidence 0.65
    → No experiment run yet; Alice planned to test this in Q2

Unanswered annotation threads:
  ☐ ann_0892 — Alice asked "why does dropout hurt here?" on [Jones 2022] — no reply
    → Worth discussing in next lab meeting
```

## Step 3: Tacit Knowledge Interview

Generate a structured questionnaire for the PI to conduct with the departing member (in person):

```
## Tacit Knowledge Interview: Alice

1. What's the most important thing you know about protein fitness prediction 
   that isn't written down anywhere in the lab's documents?

2. Which of the papers you read do you think we're most likely to overlook 
   or underestimate? Why?

3. What approaches did you try that didn't work, and why didn't they work? 
   (Things that aren't in any experiment log)

4. What's the biggest mistake you made on this project that we should avoid?

5. Who outside this lab should we be talking to about [topic]? 
   What are their names and why are they relevant?

6. What would you do next on this project if you were staying?

7. What's the one paper that changed how you think about this problem most?
```

## Step 4: Successor Onboarding Guide

Produce a curated reading and orientation guide for whoever takes over:

```
## Onboarding Guide for Alice's Successor

### Week 1: Foundation Papers (read in this order)
1. [Rives et al. 2021] ESM — the baseline protein LM; everything builds on this
2. [Notin et al. 2022] EVE — the key competing approach we're trying to beat
3. [Dallago et al. 2021] ProteinGym — the benchmark we use; understand it deeply

### Week 2: Methods Papers
[5 papers with 2-sentence rationale each]

### Key People to Meet
- Bob (this lab) — knows the evaluation pipeline inside out
- [External collaborator] at [institution] — they have access to wet lab validation

### Current Project State
[Summary of where Alice left the project]

### First Recommended Experiment
[Concrete suggestion for what to do first]
```

## Export

Produce the full handoff package as:
- A single Markdown document (`{member}_handoff_{date}.md`)
- A ZIP archive including: the Markdown doc + exported annotations JSON + BibTeX of their unique papers

## Integration Notes

- Run `expertise-mapping` first to get the expertise portrait
- Run `reading-coverage` to find single-reader papers
- Pull from `claim-tracker`, `hypothesis-versioning`, `experiment-log` for open threads
- The tacit knowledge interview must be conducted in person — this skill only generates the questions
