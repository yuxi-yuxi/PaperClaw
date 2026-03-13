---
name: team-sync
description: Generates structured lab meeting agendas, paper discussion guides, and meeting summaries based on recent team activity and open questions. Use when the user needs to prepare for a lab meeting, wants to generate discussion questions for a paper presentation, needs to summarize what was discussed and decided in a meeting, or wants a digest of team reading activity for the week. Triggers on phrases like "lab meeting agenda", "discussion questions for this paper", "summarize our meeting", "what should we discuss", "weekly digest", "paper presentation", "meeting notes".
---

# Team Sync

Turns the recurring overhead of lab meetings into structured, evidence-driven sessions. Generates agendas from real team activity — not from scratch.

## Generating a Lab Meeting Agenda

When asked to generate an agenda, pull from:
- `reading-coverage`: papers added or read this week
- `annotation-sharing`: heavily annotated papers or active discussion threads
- `claim-tracker`: claims recently challenged or updated
- `hypothesis-versioning`: hypotheses recently revised
- `arxiv-monitor`: high-relevance new papers from the past week

Structure a 60-minute meeting as:

```
## Lab Meeting Agenda — [Date]

**Attendees**: Alice, Bob, Carol, David

---

### 1. Paper of the Week (20 min)
[Paper title] — presented by [member who added it / knows it best]
"[One sentence on why this matters to the group]"

Discussion questions:
  - [3 targeted questions generated from the paper]

### 2. New Papers Digest (10 min)
Papers added this week — quick round-robin, 1 min each:
  - [Title] — added by [member] — "[one-line summary]"
  - [Title] — added by [member] — "[one-line summary]"
  [up to 5 papers]

### 3. Open Questions (20 min)
Active threads that need group input:
  - claim_0042: "Contrastive pretraining vs MLM" — alice has new data, needs group read
  - hyp_0017: "Homolog fine-tuning hypothesis" — no experiment yet; assign owner?

### 4. Action Items from Last Week (10 min)
  ☑ Bob: read Notin et al. — done
  ☐ Carol: run baseline on ProteinGym — not done, moved to this week

---

**This week's action items** (fill in during meeting):
  [ ] ...
```

## Generating Paper Discussion Questions

When asked for discussion questions for a specific paper:

1. Fetch or use the provided abstract and key sections
2. Generate questions across categories:

**Comprehension**: Does everyone understand the method?
> "Walk us through the training objective in Section 3 — what exactly is being optimized and why?"

**Critical**: What are the weaknesses?
> "The baselines are all from 2021 — are there stronger recent comparisons missing?"
> "How sensitive are results to the hyperparameter choices in Table 2?"

**Relevance**: How does this connect to our work?
> "If we applied their evaluation protocol to our current method, would our results hold?"
> "Their dataset is 10× larger than ours — is this comparison fair?"

**Extension**: What would you do next?
> "What's the most obvious experiment they didn't run that we could run?"
> "Does this finding change how we're thinking about [our current hypothesis]?"

Generate 6–10 questions, mixed across categories. Weight toward critical and relevance.

## Summarizing a Meeting

When the user provides meeting notes (free text), extract:

```
## Meeting Summary — [Date]

### Key Decisions
- [Decision 1]: [context and rationale]
- [Decision 2]: ...

### New Action Items
  ☐ [Person]: [task] — due [date]
  ☐ [Person]: [task] — due [date]

### Papers to Follow Up
- [Paper] — [why / who should read it]

### Open Questions Raised (not resolved)
- [Question] — [context]

### Notes / Discussion Points Worth Saving
- [Insight or observation from discussion]
```

## Weekly Reading Digest

When asked for a digest of team activity:

```
## Weekly Reading Digest — Week of [Date]

📚 Papers read this week: 14 total
  alice: 4 | bob: 3 | carol: 5 | david: 2

🆕 Papers added to library: 7
  Highlights:
  - [Paper A] — added by carol — "New SOTA on ProteinGym; directly relevant to Aim 2"
  - [Paper B] — added by alice — "Challenges our core hypothesis — READ ASAP"

💬 Active annotation threads (need responses):
  - ann_0892 — alice's question about dropout on [Jones 2022] — unanswered 5 days

📡 arXiv highlights this week:
  - arXiv:2403.12345 — Relevance: 0.91 — "Contrastive Protein LMs" — 🔥 high priority
```

## Integration Notes

- Pull agenda inputs from `reading-coverage`, `arxiv-monitor`, `claim-tracker`, `hypothesis-versioning`
- Log paper presentations in `reading-coverage` (presenter counts as "read")
- Log action items to a persistent `action_items.md` in the team workspace
- Discussion questions feed `annotation-sharing` — save good questions as annotations on the paper
