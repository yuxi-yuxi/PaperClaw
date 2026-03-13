# Reading Coverage

## Overview
Tracks which papers the team has collectively read, who has read what, and what important papers remain unread. Acts as the team's reading dashboard — ensuring critical papers don't fall through the cracks and that reading effort is distributed efficiently.

## When to Use
- User asks "has anyone read [paper]?"
- Lab wants to know the reading coverage across a list of required papers
- User wants to assign unread papers to team members
- PI wants an overview of how well the team is keeping up with the literature
- Lab is preparing for a meeting and wants to confirm everyone has read the key papers

## Key Capabilities
- Track read/unread status per paper per team member
- Compute team-level coverage: % of important papers read by at least one person
- Identify high-priority unread papers (high-citation, recently added, flagged as critical)
- Suggest reading assignments based on workload and expertise fit
- Generate a reading queue for each team member
- Track reading velocity: how many papers per week per person

## Usage Examples

### Check if a paper has been read
```python
reading_coverage.check(
    doi="10.1038/s41586-024-00001-0",
    team=["alice", "bob", "carol"]
)
# Returns: {"alice": True, "bob": False, "carol": False}
```

### Get team coverage summary
```python
reading_coverage.summary(
    corpus=review.get_papers(tag="critical"),
    team=["alice", "bob", "carol"]
)
# Returns: {"coverage": 0.64, "unread_by_anyone": 12, "read_by_one": 8}
```

### Get unread high-priority papers
```python
reading_coverage.unread_priority(
    min_citations=50,
    added_by_team=True,
    unread_by=None  # None = unread by entire team
)
```

### Generate reading assignments
```python
reading_coverage.assign_reading(
    unread_papers=reading_coverage.unread_priority(),
    team=["alice", "bob", "carol"],
    balance_by="workload"  # workload | expertise | random
)
```

## Output Format
Coverage summary returns: total papers, coverage percentage, per-member read counts, and unread priority list. Reading assignments return a per-member list of papers with rationale for the assignment.

## Notes
- "Read" is inferred from: Zotero sync, annotation activity, or explicit marking
- Members can manually mark papers as read via `reading_coverage.mark_read(doi, member)`
- Combine with `expertise-mapping` — reading coverage feeds the expertise scores
