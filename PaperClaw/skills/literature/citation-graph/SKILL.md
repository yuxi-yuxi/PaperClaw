---
name: citation-graph
description: Builds and analyzes citation networks around a set of papers. Use when the user wants to find the most influential papers in an area, trace the intellectual lineage of a research direction, identify foundational works, find "bridge" papers between research communities, visualize how a field is structured, or discover important papers the team hasn't read yet. Triggers on phrases like "citation graph", "most cited papers", "foundational works", "how is this field structured", "who does everyone cite", "what papers connect X and Y".
---

# Citation Graph

Builds citation networks from a seed set of papers and analyzes their structure to reveal the intellectual architecture of a research area.

## Building the Graph

Use the Semantic Scholar Academic Graph API (free, no key required for basic use):

```
GET https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations?fields=title,authors,year,citationCount&limit=500
GET https://api.semanticscholar.org/graph/v1/paper/{paper_id}/references?fields=title,authors,year,citationCount&limit=500
```

Supported `paper_id` formats: `DOI:10.xxxx/...`, `arXiv:2103.xxxxx`, `S2:{s2_id}`

### Expansion Strategy

Starting from seed papers, expand the graph to depth N:
- **Depth 1**: Direct citations and references of seed papers
- **Depth 2**: Citations of citations (can get large — apply `min_citations` filter)
- **Depth 3+**: Use sparingly; prune aggressively by citation count

Recommended: depth=2, min_citations=20 for most use cases.

## Computing Centrality

Once the graph is built (nodes = papers, edges = citation relationships), compute:

- **In-degree**: How many papers cite this paper — proxy for raw influence
- **PageRank**: Recursive influence — being cited by highly-cited papers counts more
- **Betweenness centrality**: Papers that sit on many shortest paths — "bridge" papers between communities

Use `networkx` in Python:
```python
import networkx as nx
G = nx.DiGraph()
# add nodes and edges from API results
pagerank = nx.pagerank(G, alpha=0.85)
betweenness = nx.betweenness_centrality(G)
```

## Detecting Communities

Use the Louvain algorithm for community detection:
```python
import community as community_louvain
G_undirected = G.to_undirected()
partition = community_louvain.best_partition(G_undirected)
```

Each community typically corresponds to a research sub-community or methodological school.

## Output Format

### Top Papers by Centrality
```
Rank | Title | Authors | Year | Citations | PageRank | Community
1    | Attention Is All You Need | Vaswani et al. | 2017 | 98,432 | 0.0412 | A
2    | BERT | Devlin et al. | 2019 | 71,209 | 0.0298 | A
...
```

### Community Summary
```
Community A (Transformer Architectures): 47 papers, anchored by [Vaswani 2017], [Devlin 2019]
Community B (Protein LMs): 31 papers, anchored by [Rives 2021], [Lin 2023]
Community C (Fitness Prediction): 18 papers, anchored by [Dallago 2021], [Notin 2022]
```

### Coverage Gap (Papers Team Hasn't Read)
List top-ranked papers by PageRank that are not in the team's library, sorted by centrality score.

## Export Formats

- **JSON**: Node/edge list with all metadata — for custom visualization
- **CSV**: Flat table of papers with centrality scores
- **Gephi**: GEXF format for interactive visualization in Gephi
- **Graphviz DOT**: For static diagram generation

## Integration Notes

- Use `semantic-scholar` skill to fetch paper metadata before building the graph
- Use `reading-coverage` to identify which high-centrality papers the team hasn't read
- Use `gap-detection` after community detection — community boundaries often reveal research gaps
