---
name: semantic-scholar
description: Searches and retrieves paper metadata, citations, references, and author profiles from the Semantic Scholar Academic Graph (200M+ papers). Use when the user needs paper metadata by title or DOI, wants papers citing or referenced by a specific work, needs an author's publication list or h-index, wants to do a semantic search over a topic, or needs structured paper data for building a literature database. Triggers on phrases like "look up this paper", "find papers on", "who cites", "references of", "author profile", "h-index", "semantic scholar".
---

# Semantic Scholar

The Semantic Scholar Academic Graph API provides structured, machine-readable access to 200M+ papers across all scientific fields. Free to use; register for an API key for higher rate limits.

**API base**: `https://api.semanticscholar.org/graph/v1/`  
**Rate limits**: 1 req/sec (unauthenticated), 10 req/sec (with API key)  
**Register**: https://www.semanticscholar.org/product/api

## Paper Search

```
GET /paper/search?query={query}&fields=title,authors,year,venue,citationCount,tldr,openAccessPdf&limit=20
```

Returns papers ranked by relevance. `tldr` field contains a 1–2 sentence AI-generated summary (available for most papers post-2018).

## Paper Lookup by ID

Supported ID formats:
- `DOI:10.1038/s41586-024-00001-0`
- `arXiv:2310.12345`
- `PMID:12345678`
- `S2:{semantic_scholar_id}`

```
GET /paper/{paper_id}?fields=title,authors,year,venue,citationCount,abstract,tldr,openAccessPdf,references,citations
```

## Batch Lookup

```
POST /paper/batch
Body: {"ids": ["DOI:10.xxxx/...", "arXiv:2103.xxxxx"], "fields": "title,abstract,tldr"}
```

Supports up to 500 IDs per request.

## Citation and Reference Lists

```
GET /paper/{paper_id}/citations?fields=title,authors,year,citationCount&limit=100
GET /paper/{paper_id}/references?fields=title,authors,year,citationCount&limit=100
```

## Author Profiles

```
GET /author/search?query={author_name}&fields=name,hIndex,citationCount,paperCount,affiliations
GET /author/{author_id}/papers?fields=title,year,venue,citationCount&limit=50
```

## Key Fields Reference

| Field | Description |
|-------|-------------|
| `title` | Paper title |
| `authors` | List of `{authorId, name}` |
| `year` | Publication year |
| `venue` | Conference or journal name |
| `citationCount` | Total incoming citations |
| `tldr` | AI-generated 1–2 sentence summary |
| `openAccessPdf` | `{url, status}` — direct PDF link if available |
| `fieldsOfStudy` | e.g., `["Computer Science", "Biology"]` |
| `publicationTypes` | e.g., `["JournalArticle", "Conference"]` |

## Semantic Search (Embedding-Based)

For topic-based discovery beyond keyword matching, use the `/paper/search` endpoint with natural language queries. S2's search uses learned embeddings, not just BF-IDF. Example:

```
GET /paper/search?query=self-supervised+learning+protein+structure&fields=title,tldr,year,citationCount&limit=25
```

## Handling "Not Found" Cases

Some papers — especially very recent, obscure, or not-yet-indexed — may not be in S2. In these cases:
1. Try alternative IDs (DOI → arXiv → title search)
2. Fall back to OpenAlex API: `https://api.openalex.org/works?filter=doi:{doi}`
3. Note in the output that the paper could not be verified

## Integration Notes

- Use as the primary data source when building citation graphs (`citation-graph` skill)
- Use `tldr` field to generate quick summaries for reading digests
- Combine with `arxiv-monitor` — arXiv IDs can be looked up directly in S2 for citation data
- For biomedical literature specifically, also check PubMed (NCBI E-utilities API)
