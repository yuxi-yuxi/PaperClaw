---
name: reading-coverage
description: Tracks which papers the team has collectively read, who has read what, and which important papers remain unread. Use when the user wants to know if anyone has read a specific paper, wants an overview of team reading coverage, needs to assign unread papers to team members, or wants to generate a reading queue. Triggers on phrases like "has anyone read", "who read this paper", "reading coverage", "unread papers", "reading assignments", "what haven't we read", "reading queue", "assign papers to".
---

# Reading Coverage

Acts as the team's reading dashboard — tracking what's been read, by whom, and what still needs attention.

## Tracking "Read" Status

A paper is counted as read by a member when any of these is true:
1. They annotated it in `annotation-sharing` (any annotation = read signal)
2. They added it to the team library via Zotero or manually
3. They presented it at a lab meeting (`team-sync` record)
4. They manually marked it: `reading-coverage mark-read {doi} {member}`
5. They wrote a note on it in `living-review`

Store read status in `reading_log.json`:
```json
{
  "10.48550/arXiv.1706.03762": {
    "alice": {"read": true, "date": "2024-01-15", "source": "annotation"},
    "bob": {"read": true, "date": "2024-02-03", "source": "manual"},
    "carol": {"read": false}
  }
}
```

## Checking if a Paper Has Been Read

When asked "has anyone read [paper]?":
1. Resolve the paper to a DOI or arXiv ID
2. Look up in `reading_log.json`
3. Return: who has read it, when, and how (signal source)

```
arXiv:1706.03762 — "Attention Is All You Need"
  ✅ alice — read 2024-01-15 (via annotation)
  ✅ bob — read 2024-02-03 (via manual mark)
  ❌ carol — not read
  ❌ david — not read
```

## Team Coverage Summary

When asked for a coverage overview:

```
## Team Reading Coverage — Critical Papers

Total: 47 papers | At least 1 person read: 38 (81%) | No one has read: 9 (19%)

Read by everyone: 12 papers (26%)
Read by 3/4: 14 papers (30%)
Read by 2/4: 12 papers (26%)
Read by 1/4: 9 papers (19%) ← single points of failure
Read by 0/4: 9 papers (19%) ← critical gaps

Single-reader papers (only 1 person has read — at risk if they leave):
  - [Notin et al. 2023] EVE model — only alice has read this
  - [Trinquier et al. 2021] — only alice
  - [+7 more]
```

## Priority Unread Papers

When asked for unread papers that should be prioritized:

Rank unread papers by:
1. Citation count (higher = more important to the field)
2. Team tags (tagged `critical` or `must-read` = high priority)
3. Recency (papers added recently by a team member = implied importance)
4. Centrality in citation graph (if `citation-graph` data available)

```
Top Unread Papers (priority order):
1. [Lin et al. 2023] ESM-2 — 4,200 citations | tagged: critical | unread by: carol, david
2. [Jumper et al. 2021] AlphaFold2 — 18,900 citations | unread by: david
3. [Notin et al. 2022] EVE — 890 citations | tagged: key-competitor | unread by: bob, carol, david
```

## Generating Reading Assignments

When asked to assign unread papers:

Balance by:
- **Expertise fit**: assign papers in someone's core area to them
- **Workload**: spread evenly if no expertise signal
- **Gap filling**: assign single-reader papers to a second person for coverage

```
Reading Assignments (this week):

bob:
  - [Notin et al. 2023] EVE — you're closest to this topic (fitness_prediction: 0.71)
  - [Trinquier et al. 2021] — only alice has read this; coverage gap

carol:
  - [Lin et al. 2023] ESM-2 — core to your protein_lm work
  - [Su et al. 2023] — contradicts a claim you cited; should read before submission

david:
  - [Jumper et al. 2021] AlphaFold2 — foundational; everyone should have read this
```

## Reading Velocity

When asked about team reading pace:

```
Reading velocity (last 30 days):
  alice: 8 papers (2.0/week)
  bob: 5 papers (1.25/week)
  carol: 11 papers (2.75/week) ← most active
  david: 3 papers (0.75/week) ← lightest load

Team total: 27 papers in 30 days
Corpus growth: +34 papers added in same period
Coverage trend: falling behind — team reading < papers added
```

## Integration Notes

- Feeds into `expertise-mapping` — reading history is the primary expertise signal
- Feeds into `lab-knowledge-handoff` — single-reader papers are handoff risks
- Use `team-sync` — unread high-priority papers make good lab meeting agenda items
- Use `arxiv-monitor` to understand why the corpus is growing faster than the team can read
