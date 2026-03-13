---
name: review-response
description: Drafts structured, evidence-backed responses to peer reviewer comments for journal revisions. Use when the user has received reviewer feedback and needs help drafting a point-by-point response, wants to triage reviewer concerns by impact, needs to find literature addressing a reviewer's concern, or needs to write the cover letter for a resubmission. Triggers on phrases like "respond to reviewers", "reviewer comments", "point-by-point response", "revise and resubmit", "address reviewer", "reviewer 2 says", "write the rebuttal letter", "revision response".
---

# Review Response

Journal revision responses are a distinct writing genre. The goal is not to argue — it is to satisfy reviewers that their concerns have been addressed thoroughly and professionally.

## Step 1: Triage Reviewer Comments

Before drafting, classify each comment:

| Type | Description | Strategy |
|------|-------------|----------|
| **Fatal flaw (must fix)** | Methodological error, missing control, unjustified claim | Accept and address fully |
| **Missing citation** | Reviewer wants a paper cited | Add it; brief response |
| **Scope request** | Reviewer wants more experiments | Negotiate: do some, defer others |
| **Clarity issue** | Reviewer misunderstood something | Rewrite the section; don't blame reviewer |
| **Disagreement** | Reviewer holds a different opinion | Push back respectfully with evidence |
| **Minor** | Typos, formatting, small suggestions | Accept and thank |

Produce a triage table first, then draft responses in priority order.

## Response Structure

Each response follows the same format:

```
**Reviewer [N], Comment [M]:**
> [Quote the reviewer comment exactly]

**Response:**
[Your response here]

**Changes to manuscript:**
[Exactly what you changed, with page/line references: "We added [X] to Section 3.2, lines 142–158."]
```

**Always quote the reviewer comment exactly** — reviewers often forget what they wrote and appreciate seeing it.

## Response Tone

- **Never defensive**: Don't start with "We disagree" without something more — "We thank the reviewer for this important point. While we see the concern differently, we have..."
- **Never dismissive**: Even for comments you're not acting on, explain why
- **Always thank**: Start each response with a one-line acknowledgment
- **Be specific**: "We revised Section 3" is not enough. "We added a paragraph to Section 3.2 (lines 145–158) clarifying X" is correct

## Pushing Back Respectfully

When a reviewer is wrong or making an unfair request:

```
We thank the reviewer for this comment. While we understand the concern, 
we respectfully maintain our original framing for the following reasons:

1. [Factual reason with citation if possible]
2. [Methodological reason]

We note that [prior work] has used the same approach [cite], which [journal] 
has published previously. We have added a clarifying note in Section X 
(lines Y–Z) to make this reasoning explicit for readers.
```

**Only push back when you're clearly right and can cite evidence.** 
Picking unnecessary fights with reviewers reduces acceptance chances.

## Finding Literature for Reviewer Concerns

When a reviewer says "the authors ignore work on X":
1. Search Semantic Scholar: `GET /paper/search?query={topic}`
2. Search arXiv for recent preprints
3. For each relevant paper found:
   - If it's directly relevant: cite it and address how your work relates
   - If it's not directly relevant: cite it briefly and explain the distinction
   - If it actually does contradict your work: address the contradiction head-on

## Experiments You Can't Do

When a reviewer requests an experiment that is infeasible (resource, time, or scope):

```
We thank the reviewer for this suggestion. We agree that [experiment] would 
strengthen the paper and have added it to our future work (Section X, line Y).

For the current revision, this experiment falls outside our current scope 
because [specific reason: time, computational cost, data access, etc.]. 
We have added a limitation statement to Section X (lines Y–Z) explicitly 
acknowledging this as a direction for future work.
```

## Cover Letter (Resubmission)

```
Dear [Editor name / "Editor"],

We thank the reviewers for their thorough and constructive feedback on our 
manuscript "[Title]" (Manuscript ID: [ID]). We have revised the manuscript 
substantially in response to all reviewer comments.

The major changes are:
1. [Major change 1 — what you did and why]
2. [Major change 2]
3. [Major change 3]

We believe the revised manuscript is significantly stronger and addresses 
all concerns raised. A point-by-point response to each reviewer comment 
is included below.

Sincerely,
[Author names]
```

## Formatting the Full Response Document

```
---
Manuscript: [Title]
Journal: [Journal]
Submission ID: [ID]
Authors: [Names]
Date: [Date]
---

We thank the editors and reviewers for their thorough evaluation. 
We have addressed all comments in the point-by-point responses below.
Reviewer comments are shown in italics; our responses follow.

---

## Reviewer 1

[All R1 responses]

---

## Reviewer 2

[All R2 responses]

---

## Editor Comments (if any)

[Editor responses]
```

## Integration Notes

- Use `evidence-grading` to assess whether a reviewer's concern has strong literature support
- Use `semantic-scholar` and `arxiv-monitor` to find papers addressing reviewer's cited concerns
- Use `rebuttal-writing` instead for conference rebuttals (word-limited, different genre)
- After revision, use `reproducibility-check` if reviewer raised reproducibility concerns
