# Team Sync

## Overview
Generates structured lab meeting agendas and paper discussion summaries based on recent team reading activity, new literature, and open questions. Turns the chaos of "what should we discuss this week?" into a focused, evidence-driven meeting agenda.

## When to Use
- User asks "generate an agenda for our lab meeting"
- Lab wants a digest of what the team has been reading this week
- User asks "what open questions should we discuss based on recent papers?"
- PI wants a summary of team research activity before a check-in
- Lab meeting is approaching and the team needs a structured discussion plan

## Key Capabilities
- Generate a weekly or bi-weekly lab meeting agenda from recent team activity
- Summarize newly added papers since last meeting with 2-sentence abstracts
- Surface open questions and unresolved contradictions for team discussion
- Include a "paper of the week" recommendation with discussion prompts
- Generate discussion questions for a specific paper the team is presenting
- Summarize what was discussed and decided in a meeting (from notes input)

## Usage Examples

### Generate this week's lab meeting agenda
```python
team_sync.generate_agenda(
    team=["alice", "bob", "carol", "david"],
    since="last_meeting",
    include_new_papers=True,
    include_open_questions=True,
    include_paper_of_week=True,
    duration_minutes=60
)
```

### Generate discussion questions for a paper presentation
```python
team_sync.paper_discussion_questions(
    doi="10.48550/arXiv.2310.xxxxx",
    presenter="bob",
    audience_expertise="intermediate",
    num_questions=8
)
```

### Summarize meeting notes into action items
```python
team_sync.summarize_meeting(
    raw_notes="[paste meeting notes here]",
    extract_action_items=True,
    extract_decisions=True,
    format="structured_markdown"
)
```

## Output Format
Agendas are structured Markdown with timed sections. Discussion questions are numbered, grouped by paper section (intro, methods, results, discussion). Meeting summaries include: key decisions, action items with owners, and papers to follow up on.

## Notes
- Agenda timing is calibrated to the specified duration (default: 60 minutes)
- "Paper of the week" is selected based on citation velocity, novelty, and relevance to active projects
- Combine with `reading-coverage` to flag unread critical papers as agenda items
