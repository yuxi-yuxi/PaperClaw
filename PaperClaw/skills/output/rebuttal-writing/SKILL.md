---
name: rebuttal-writing
description: Drafts concise, strategic rebuttals for conference paper reviews under strict word limits. Use when the user has received conference reviews and needs a rebuttal for NeurIPS, ICML, ICLR, ACL, CVPR, or similar venues. This is different from journal review-response — conference rebuttals are word-limited and strategically different. Triggers on phrases like "conference rebuttal", "author response", "NeurIPS rebuttal", "ICML rebuttal", "ICLR rebuttal", "ACL rebuttal", "500 word rebuttal", "how to respond to conference reviews".
---

# Rebuttal Writing

Conference rebuttals are a distinct genre from journal review responses. They are short, time-constrained, and strategically high-stakes. The goal is to move borderline reviewers to accept — not to comprehensively address every comment.

## Conference Word Limits

| Venue | Limit | Notes |
|-------|-------|-------|
| NeurIPS | 500 words | Strict; reviewers read briefly |
| ICML | 500 words | Strict |
| ICLR | Unlimited | Detailed responses expected |
| ACL/EMNLP | 500 words | Strict |
| CVPR/ICCV | 900 words | More space; use it |
| AAAI | 500 words | Strict |

## Step 1: Rebuttal Strategy (Do This First)

Before writing a single word, assess:

**Which reviewers can be moved?**
- Reviewers who raised factual misunderstandings → high chance to move with clarification
- Reviewers with methodological concerns that have quick answers → moveable
- Reviewers who fundamentally disagree with the paper's framing → hard to move

**What are the "fatal flaw" concerns?**
Concerns that, if unaddressed, guarantee rejection. Address these first, no matter what.

**What is the word budget?**
Allocate words by impact:
```
Word budget (500 words):
  R1 fatal flaw (misunderstanding of method): 120 words
  R2 missing comparison (can address quickly): 80 words
  R2 dataset question: 60 words
  R3 minor concerns (batch): 60 words
  R1 R2 R3 shared concern (efficiency): 80 words
  Opening + closing: 50 words
  Buffer: 50 words
  Total: 500 words
```

## Step 2: Addressing Shared Concerns First

If multiple reviewers raise the same concern, address it once and reference it:

```
**Re: [Shared concern — all reviewers]**
[Concise response — 60–80 words]
We address this concern first as it was raised by R1, R2, and R3.
```

## Addressing a Factual Misunderstanding

The fastest path to moving a reviewer:
```
R[N] states that we [mischaracterization]. We clarify: [correct statement]. 
This is described in Section [X], [line/paragraph reference]. 
[Optional: restate the key point in different words for clarity.]
```

## Addressing a Missing Experiment

When a reviewer wants an experiment you have results for:
```
We thank R[N] for this suggestion. We ran [experiment] and report results in 
the supplementary (Table [X]): [result]. [One sentence interpreting the result 
in relation to the concern.]
```

When you don't have the result (be honest):
```
We agree this would strengthen the paper. Due to [compute/time/scope constraints], 
we were unable to run [experiment] during the rebuttal period. We commit to 
including this in the camera-ready if accepted, or will add it as a limitation.
```

## Pushing Back on a Reviewer

Only do this when you're clearly right and can be specific:
```
We respectfully disagree with R[N]'s characterization that [claim]. 
Specifically: [evidence — cite your paper section or external citation]. 
[Prior work X] [cite] uses the same approach, which has been accepted at [venue].
```

**Never**: be sarcastic, condescending, or passive-aggressive. Area chairs read the rebuttal.

## Things NOT to Do in a Conference Rebuttal

- Don't respond to every single comment — you don't have space and it dilutes impact
- Don't use hedging language: "We believe this might possibly..." → "This addresses..."
- Don't repeat what's already in the paper — reviewers read it; point to where it is
- Don't make promises you can't keep in the camera-ready (5-day turnaround typical)
- Don't thank each reviewer individually — wastes word budget; thank once at the top

## Rebuttal Opening (20–30 words)

```
We thank the reviewers for their thorough and constructive feedback. 
We address the major concerns below.
```

That's it. Don't be elaborate.

## Full Rebuttal Template (500 words)

```
We thank the reviewers for their thorough feedback. We address major concerns below.

**[Shared concern — R1, R2, R3]:** [Response — ~80 words]

**R1, Fatal flaw concern:** [Response — ~100–120 words]

**R2, Experiment request:** [Response — ~80 words]

**R2, Additional concern:** [Response — ~60 words]

**R3 (minor concerns):** [Address 2–3 minor points in batch — ~60 words]

**Re: Efficiency/scalability (R1, R2):** [Response — ~60 words]

[Closing if space: "We believe these responses address the core concerns and 
look forward to the discussion phase."]
```

## Integration Notes

- Use `review-response` instead for journal revisions — different genre, no word limit
- Use `evidence-grading` to assess how strongly to push back on a reviewer's empirical claim
- Use `semantic-scholar` to quickly find literature addressing a reviewer's concern
- ICLR rebuttals: unlimited space — use `review-response` format and be comprehensive
