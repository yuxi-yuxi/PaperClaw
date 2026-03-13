# Expertise Mapping

## Overview
Maps the expertise distribution across a research team based on their reading history, annotations, and contributions. Answers "who knows the most about X?" and helps teams route questions, assign reviewers, and identify knowledge gaps that need filling.

## When to Use
- User asks "who on the team knows the most about [topic]?"
- Lab lead wants to understand the team's collective knowledge coverage
- Assigning internal reviewers for a manuscript draft
- Identifying which team member to ask before exploring a new direction
- Onboarding — understanding what gaps a new member fills

## Key Capabilities
- Build expertise profiles per team member from: papers read, annotations made, tags used, papers they added to the library
- Score expertise by topic cluster using TF-IDF and semantic similarity
- Identify the team's strongest and weakest coverage areas
- Suggest which team member to consult for a given question
- Generate a team expertise matrix (members × topics)
- Track how expertise is growing over time as the team reads new work

## Usage Examples

### Find who knows most about a topic
```python
expertise = expertise_mapping.find_expert(
    topic="variational autoencoders for molecular generation",
    team=["alice", "bob", "carol", "david"]
)
# Returns: {"top_expert": "carol", "confidence": 0.82, "evidence": ["read 14 papers", "200+ annotations"]}
```

### Get full team expertise matrix
```python
expertise_mapping.team_matrix(
    topics=["protein_lm", "rl_for_drug_discovery", "docking", "generative_models"],
    normalize=True,
    format="heatmap_data"
)
```

### Find team knowledge gaps
```python
expertise_mapping.gaps(
    required_topics=["quantum_chemistry", "coarse_grained_simulation"],
    team=["alice", "bob", "carol"]
)
# Returns: topics with no strong team coverage
```

### Suggest reviewer for draft
```python
expertise_mapping.suggest_reviewer(
    draft_topics=["contrastive_learning", "protein_fitness"],
    exclude=["alice"]  # exclude author
)
```

## Output Format
Expertise scores are 0–1 normalized per topic. Team matrix returns member × topic grid. Gap analysis returns list of uncovered topics with suggested remediation (papers to read, people to hire/collaborate with).

## Notes
- Expertise scores are based on reading signals, not publication record — someone who reads deeply in an area scores high even without papers on it
- Scores update automatically as team members add papers and annotations
- Combine with `reading-coverage` to understand what the team has collectively read vs. not read
