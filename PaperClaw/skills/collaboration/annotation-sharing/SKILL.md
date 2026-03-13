---
name: annotation-sharing
description: Shares, surfaces, and discusses PDF annotations across a research team. Use when the user wants to see what teammates highlighted or noted in a paper, share their own annotations with the team, search across all team annotations on a topic, start or reply to a discussion thread on a specific passage, or import annotations from Zotero or Hypothesis. Triggers on phrases like "what did X highlight", "share my annotations", "team notes on this paper", "search annotations", "what did we note about", "annotation thread", "import from Hypothesis".
---

# Annotation Sharing

Transforms isolated PDF highlights and margin notes into a shared knowledge layer across the team. Annotations are stored in a flat JSON structure and queryable by paper, author, topic, or tag.

## Annotation Data Model

```json
{
  "id": "ann_0567",
  "paper_doi": "10.48550/arXiv.1706.03762",
  "author": "alice",
  "timestamp": "2024-03-10T14:22:00Z",
  "type": "highlight",
  "text_excerpt": "Multi-head attention allows the model to jointly attend to information from different representation subspaces",
  "context": "Section 3.2, paragraph 2",
  "page": 4,
  "comment": "This is the key insight — each head learns different attention patterns",
  "tags": ["key-claim", "attention-mechanism"],
  "replies": [
    {
      "id": "reply_0089",
      "author": "bob",
      "timestamp": "2024-03-11T09:15:00Z",
      "comment": "Confirmed by the visualization in Figure 3 — heads really do specialize"
    }
  ]
}
```

Store annotations in `annotations.json` in the team workspace. Index by `paper_doi` and `author` for fast lookup.

## Importing Annotations

### From Zotero PDF Reader
Zotero stores annotations as child items of type `annotation`. Use the Zotero API:
```
GET /groups/{groupID}/items?itemType=annotation&format=json
```
Map color codes to annotation types (team should agree on convention):
- Yellow → `key-claim`
- Red → `critique`
- Green → `methodology`
- Blue → `question`
- Purple → `follow-up`

### From Hypothesis (hypothes.is)
```
GET https://api.hypothes.is/api/search?uri={paper_url}&user=acct:{username}@hypothes.is
Authorization: Bearer {api_token}
```

### From PDF (manual import)
When user pastes annotation text, create a new annotation record with `type: "manual"` and ask for: page number, comment, tags.

## Getting All Team Annotations on a Paper

When asked "what did the team annotate on [paper]":
1. Look up all annotations with matching `paper_doi`
2. Group by page/section order
3. Format as a threaded view:

```
📄 Attention Is All You Need (arXiv:1706.03762)

Page 4 — Section 3.2
  🟡 alice [2024-03-10]: "Multi-head attention allows..."
     💬 "Key insight — each head learns different patterns"
     ↳ bob [2024-03-11]: "Confirmed by Figure 3 visualization"

Page 7 — Section 4
  🔴 carol [2024-03-12]: "We use Adam with β1=0.9..."
     💬 "Why these specific β values? Check warmup schedule too"
```

## Searching Annotations

When asked to search across all annotations:
1. Tokenize the query
2. Match against: `text_excerpt`, `comment`, `tags`, `replies[].comment`
3. Rank by match quality + recency
4. Return top results with paper context

```
Search: "attention mechanism limitation"

[1] ann_0892 — Jones et al. 2022 — alice — "standard attention is O(n²) in sequence length..."
    Comment: "This is why linear attention variants exist"

[2] ann_1203 — Wang et al. 2023 — bob — "cross-attention fails when..."
    Comment: "Known limitation — flagged as future work"
```

## Adding a Reply

When a user wants to reply to an annotation:
1. Locate annotation by ID or by paper + excerpt
2. Append to `replies[]` array with author, timestamp, comment
3. Confirm: "Replied to alice's annotation on [paper]"

## Private vs. Team Annotations

Annotations have a `visibility` field: `team` (default) or `private`.
When generating team views, exclude `private` annotations from other authors.
The annotating user can always see their own private annotations.

## Export

When asked to export annotations for a paper to a document:
- Produce a Markdown summary of all team annotations grouped by section
- Include original text excerpts, comments, and replies
- Tag with author names and dates
- This feeds directly into `living-review` when building thematic notes

## Integration Notes

- Use `zotero-integration` to pull annotations from existing Zotero libraries
- Use `reading-coverage` — annotating a paper marks it as read for that author
- Use `expertise-mapping` — annotation frequency and topic distribution feeds expertise scores
- Use `team-sync` — heavily annotated papers are good candidates for lab meeting discussion
