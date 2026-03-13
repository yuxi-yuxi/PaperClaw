# arXiv Monitor

## Overview
Monitors arXiv for new papers matching a team's research interests. Runs on a schedule or on-demand, scores relevance, and surfaces the most important new work directly to the team — replacing manual daily browsing.

## When to Use
- User asks "what's new on arXiv this week in [topic]?"
- User wants to set up automatic monitoring for a topic or author
- User asks "did anyone publish anything on X lately?"
- Lab wants a weekly digest of relevant preprints
- User wants to know if a competitor lab has posted new work

## Key Capabilities
- Query arXiv API by category (cs.LG, q-bio, stat.ML, etc.), keyword, or author
- Score relevance against a team research profile or keyword list
- Deduplicate against papers already in the team's knowledge base
- Generate a ranked digest with one-line summaries per paper
- Watch specific author IDs for new submissions
- Alert on papers that cite a specific prior work

## Usage Examples

### Get this week's relevant papers
```python
monitor.fetch_recent(
    categories=["cs.LG", "cs.AI", "q-bio.QM"],
    keywords=["protein language model", "few-shot learning", "benchmark"],
    days=7,
    top_k=15
)
```

### Set up a recurring watch
```python
monitor.watch(
    query="contrastive learning protein structure",
    author_ids=["0000-0002-1234-5678"],
    frequency="weekly",
    notify_channel="slack:#lab-papers"
)
```

### Check if a topic has seen recent activity
```python
monitor.activity_pulse(topic="diffusion models for molecular design", months=3)
```

## Output Format
Returns ranked list of papers with: title, authors, arXiv ID, abstract summary (2 sentences), relevance score, and suggested tags. Optionally formats as a digest email or Slack message.

## Notes
- Relevance scoring uses keyword overlap + semantic similarity against team profile
- Combine with `living-review` to auto-ingest high-scoring papers
- Rate-limited to arXiv API fair-use guidelines (3 requests/second max)
