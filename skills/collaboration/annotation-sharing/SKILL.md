# Annotation Sharing

## Overview
Enables a research team to share, discuss, and collectively build on PDF annotations across papers. Transforms isolated highlights and margin notes into a shared knowledge layer that persists across the team's collective reading history.

## When to Use
- User wants to share highlights or notes on a paper with teammates
- User asks "what did [teammate] think about [paper]?"
- Lab wants a single place to see all annotations on a given paper
- User wants to start a discussion thread on a specific passage
- Onboarding — showing a new member what the lab has already noted about key papers

## Key Capabilities
- Import annotations from PDF readers (Zotero, Hypothesis, Adobe, Apple Books via export)
- Tag annotations by type: key claim, methodology note, critique, question, follow-up needed
- Thread discussions on specific annotations (replies, reactions)
- Surface all annotations on a paper from all team members in a unified view
- Search annotations across the entire team corpus
- Export annotations as structured notes for inclusion in living review

## Usage Examples

### Import annotations from Zotero PDF reader
```python
annotations.import_from_zotero(
    item_key="ABCD1234",
    author="alice",
    tag_by_color=True  # yellow=key_claim, red=critique, green=method
)
```

### Get all team annotations on a paper
```python
annotations.get_paper_annotations(
    doi="10.48550/arXiv.1706.03762",
    team_members=["alice", "bob", "carol"],
    include_threads=True
)
```

### Search team annotations
```python
annotations.search(
    query="attention mechanism limitation",
    scope="all_papers",
    author=None  # None = all team members
)
```

### Start a discussion on an annotation
```python
annotations.reply(
    annotation_id="ann_0567",
    author="bob",
    comment="This limitation was addressed in the follow-up paper (arXiv:2103.xxxxx)"
)
```

## Output Format
Annotations returned with: text excerpt, surrounding context, author, timestamp, tags, and reply thread. Unified paper view groups annotations by passage position.

## Notes
- Hypothesis (hypothes.is) integration supported for web-based annotation workflows
- PDF byte offsets are used to anchor annotations — works across different PDF viewers
- Private annotations supported: team members can mark notes as personal-only
