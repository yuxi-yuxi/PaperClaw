# Zotero Integration

## Overview
Connects to a team's Zotero library via the Zotero Web API. Reads, writes, and syncs paper collections, annotations, and notes. Acts as the bridge between a team's existing reference management workflow and PaperClaw's collaborative synthesis layer.

## When to Use
- User says "pull from our Zotero library" or "sync with Zotero"
- User wants to import an existing team collection into PaperClaw
- User wants to push PaperClaw summaries or tags back into Zotero
- User asks "what's in our Zotero folder on [topic]?"
- Setting up PaperClaw for a lab that already uses Zotero

## Key Capabilities
- Read collections, subcollections, and items from a Zotero group library
- Extract notes and annotations attached to items
- Write tags, notes, and linked files back to Zotero
- Sync team library incrementally (only new/changed items since last sync)
- Export collection to BibTeX, RIS, or CSL-JSON
- Resolve DOIs and arXiv IDs from existing Zotero records
- Detect duplicate entries in the library

## Usage Examples

### Sync team Zotero library into PaperClaw
```python
zotero.sync(
    group_id="12345678",
    api_key=os.environ["ZOTERO_API_KEY"],
    collection="Protein Folding Papers",
    since_version=None  # None = full sync
)
```

### Read all items in a collection
```python
items = zotero.get_collection(
    group_id="12345678",
    collection_name="Active Reading",
    include_notes=True,
    include_tags=True
)
```

### Push PaperClaw-generated summary back to Zotero item
```python
zotero.add_note(
    item_key="ABCD1234",
    note_content=summary_text,
    tag="paperclaw-summary"
)
```

### Export collection as BibTeX
```python
zotero.export(
    collection="Main Library",
    format="bibtex",
    output_path="./references.bib"
)
```

## Output Format
Returns structured item list with: Zotero key, title, authors, DOI, abstract, tags, notes, and collection path. Sync operations return a diff of added/modified/deleted items.

## Notes
- Requires a Zotero API key — generate at https://www.zotero.org/settings/keys
- Group libraries require the group ID from the Zotero group settings page
- Write operations require an API key with write permissions
- For large libraries (>5k items), use incremental sync with `since_version` parameter
