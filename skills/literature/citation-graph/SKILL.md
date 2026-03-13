# Citation Graph

## Overview
Builds and analyzes citation networks around a body of papers. Reveals foundational works, emerging clusters, and the intellectual lineage of a research area. Helps teams understand the structure of a field, not just individual papers.

## When to Use
- User asks "what are the most influential papers in this area?"
- User wants to trace the origin of an idea or method
- User asks "what papers does everyone cite in this subfield?"
- Preparing a grant or manuscript and need to justify research positioning
- User wants to identify under-cited but highly relevant work

## Key Capabilities
- Build citation graph from a seed set of papers using Semantic Scholar or OpenAlex API
- Compute centrality metrics (betweenness, PageRank, in-degree) to surface key nodes
- Detect citation clusters / research communities via graph partitioning
- Identify "bridge" papers connecting two research communities
- Visualize citation graph as interactive network (JSON or Graphviz)
- Find papers the team should read but hasn't based on citation overlap

## Usage Examples

### Build citation graph from seed papers
```python
graph = citation_graph.build(
    seed_dois=["10.48550/arXiv.1706.03762", "10.1101/2020.07.15.204321"],
    depth=2,
    min_citations=10
)
```

### Find the most central papers
```python
graph.rank_by_centrality(metric="pagerank", top_k=20)
```

### Detect research communities
```python
graph.detect_communities(algorithm="louvain", min_cluster_size=5)
```

### Find gaps in team reading
```python
graph.coverage_gap(team_library=review.get_all_dois(), top_k=10)
```

## Output Format
Returns node/edge list with metadata, centrality scores per paper, community assignments, and optional visual layout coordinates. Exports to JSON, CSV, or Gephi format.

## Notes
- Uses Semantic Scholar Academic Graph API (free, no key required for basic use)
- OpenAlex as fallback for papers not indexed in S2
- Depth >3 can return very large graphs — use `min_citations` filter to prune
