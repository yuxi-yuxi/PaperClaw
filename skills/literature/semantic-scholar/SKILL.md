# Semantic Scholar

## Overview
Queries the Semantic Scholar Academic Graph API for paper metadata, citations, references, author profiles, and semantic search. High-coverage index of 200M+ papers across all scientific fields with structured, machine-readable data.

## When to Use
- User wants paper metadata (abstract, authors, year, venue, citation count) by title or DOI
- User asks for papers citing or referenced by a specific work
- User wants to find papers by a specific author or lab
- Semantic search over a topic when PubMed/arXiv coverage is insufficient
- Need structured data for building citation graphs or lit review databases

## Key Capabilities
- Search by keyword, title, author, or fieldsOfStudy
- Retrieve full citation and reference lists per paper
- Author profiles with h-index, citation count, affiliated institution
- Batch lookups by DOI, arXiv ID, or S2 paper ID
- Semantic similarity search (embedding-based, not just keyword)
- Open access PDF links where available
- TLDRs: auto-generated 1–2 sentence summaries per paper

## Usage Examples

### Search for papers on a topic
```python
s2.search(
    query="few-shot learning protein structure prediction",
    fields=["title", "authors", "year", "citationCount", "tldr"],
    limit=20
)
```

### Get papers citing a specific work
```python
s2.get_citations(
    paper_id="arXiv:1706.03762",
    fields=["title", "year", "authors"],
    limit=50
)
```

### Author profile lookup
```python
s2.get_author(
    name="Yoshua Bengio",
    fields=["hIndex", "citationCount", "papers"]
)
```

### Batch DOI lookup
```python
s2.batch_lookup(
    ids=["DOI:10.1038/...", "DOI:10.1101/..."],
    fields=["title", "abstract", "tldr", "openAccessPdf"]
)
```

## Output Format
Returns structured JSON with paper metadata. TLDRs are available for most papers published after 2018. OpenAccessPdf field provides direct PDF URL when available.

## Notes
- API key optional but recommended for higher rate limits (100 req/5min vs 10 req/5min)
- Register free at https://www.semanticscholar.org/product/api
- fieldsOfStudy filter supports: "Computer Science", "Biology", "Medicine", "Physics", etc.
- For bulk exports >10k papers, use the S2 Dataset releases instead of API
