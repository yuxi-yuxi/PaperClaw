---
name: expertise-mapping
description: Maps and scores research expertise across team members based on their reading history, annotations, and contributions to the knowledge base. Use when the user wants to know who on the team knows the most about a topic, needs to assign an internal reviewer for a draft, wants to see where the team's collective knowledge is strong or weak, or is onboarding a new member and needs to understand what gaps they fill. Triggers on phrases like "who knows about X", "who should review this", "team expertise", "knowledge gaps", "who to ask about", "expertise map", "who's the expert on".
---

# Expertise Mapping

Builds expertise profiles for each team member from their reading and annotation activity, then answers questions like "who knows the most about X?" and "where are our knowledge gaps?"

## Data Sources for Expertise Signals

Expertise is inferred from observable activity — not self-reported. Collect signals from:

| Signal | Weight | Source |
|--------|--------|--------|
| Papers read | 1.0× | `reading-coverage` records |
| Annotations made | 1.5× | `annotation-sharing` records |
| Papers added to library | 1.2× | Zotero sync / manual additions |
| Papers presented at lab meetings | 2.0× | `team-sync` records |
| `living-review` contributions | 1.8× | Review edit history |
| Experiment logs in topic area | 1.5× | `experiment-log` records |

## Building Expertise Profiles

For each team member, compute a topic score vector:

1. Collect all papers they've engaged with (read, annotated, added, presented)
2. Extract topics from those papers using: title keywords + arXiv categories + team tags
3. Build a topic frequency vector: `{topic: weighted_count}`
4. Normalize to 0–1 scale across all team members for each topic

```python
# Pseudocode
for member in team:
    papers = get_engaged_papers(member)
    for paper in papers:
        for topic in paper.topics:
            weight = activity_weights[activity_type]
            expertise[member][topic] += weight

# Normalize per topic
for topic in all_topics:
    max_score = max(expertise[m][topic] for m in team)
    for member in team:
        expertise[member][topic] /= max_score
```

## Finding the Expert on a Topic

When asked "who knows the most about [topic]":
1. Compute semantic similarity between the query and each topic in the expertise map
2. Sum scores for semantically similar topics (not just exact matches)
3. Return top team members with their score and evidence:

```
Query: "variational autoencoders for molecular generation"

Top experts:
1. carol — score: 0.84
   Evidence: read 14 papers tagged #VAE or #generative-models, 
   annotated 47 passages, presented "MolVAE survey" at lab meeting 2024-02

2. david — score: 0.61
   Evidence: read 9 papers tagged #VAE, ran 3 experiments in this area

3. alice — score: 0.31
   Evidence: read 4 papers (peripheral to main focus)
```

## Team Expertise Matrix

When asked for the full team overview, produce a heatmap-style table:

```
              | protein_lm | rl_drug | docking | generative | clinical
---------------------------------------------------------------------------
alice         |    ████    |   ██   |   ███   |    █       |   ████
bob           |    ██      |   ████ |   █     |    ███     |   █
carol         |    ███     |   █    |   ██    |    ████    |   ██
david         |    █       |   ███  |   ████  |    ██      |   ███
```

(Use █ blocks scaled to expertise score 0–4)

## Identifying Knowledge Gaps

When asked "what are we missing?":
1. Compare team's combined expertise against topics present in the corpus
2. Topics with high paper count but low team expertise = gaps
3. Topics with no team member scoring above 0.3 = critical gaps

Output:
```
Knowledge Gaps:
⚠️ quantum_chemistry — 12 papers in corpus, no strong expertise (max team score: 0.18)
⚠️ coarse_grained_simulation — 8 papers in corpus, max score: 0.22 (david, peripheral)
✅ protein_lm — well covered (alice: 0.92, carol: 0.78)
```

## Suggesting a Reviewer

When asked "who should review this draft?":
1. Extract topics from the draft (title, abstract, section headers)
2. Score each team member against those topics
3. Exclude authors of the draft
4. Return top 1–2 suggestions with rationale

```
Draft: "Contrastive Pretraining for Low-Data Protein Fitness Prediction"
Topics: contrastive_learning (0.7), protein_lm (0.8), fitness_prediction (0.9), low_data (0.5)

Suggested reviewer: carol (avg score: 0.79)
  Strong in: protein_lm (0.88), fitness_prediction (0.91)
  Weaker in: contrastive_learning (0.62) — may want to pair with bob (0.81 in contrastive_learning)
```

## Integration Notes

- Feeds from `reading-coverage`, `annotation-sharing`, `team-sync`, and `experiment-log`
- Use `lab-knowledge-handoff` — a departing member's expertise profile is the core of their handoff doc
- Scores update automatically as team members add papers and annotations — recompute weekly
