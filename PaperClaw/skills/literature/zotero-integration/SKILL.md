---
name: zotero-integration
description: Connects to a team's Zotero library to read, sync, and write paper collections, annotations, and notes. Use when the user wants to sync PaperClaw with their Zotero library, import an existing paper collection, pull annotations from Zotero, push summaries back to Zotero items, or export a collection to BibTeX. Triggers on phrases like "sync with Zotero", "import from Zotero", "our Zotero library", "pull from Zotero", "export to BibTeX", "Zotero collection".
---

# Zotero Integration

Zotero is the most widely used reference manager in academic research. This skill connects PaperClaw to a team's shared Zotero group library via the Zotero Web API.

**API base**: `https://api.zotero.org`  
**Get API key**: https://www.zotero.org/settings/keys  
**Auth header**: `Zotero-API-Key: {key}`

## Setup Requirements

| Requirement | Where to Get It |
|-------------|----------------|
| API key | https://www.zotero.org/settings/keys — enable library read/write |
| Group ID | Zotero group URL: `zotero.org/groups/{GROUP_ID}/...` |
| User ID | https://www.zotero.org/settings/keys (shown on that page) |

## Reading a Collection

```
GET /groups/{groupID}/collections
GET /groups/{groupID}/collections/{collectionKey}/items?format=json&include=data,bib
```

Returns items with full metadata: title, creators, DOI, abstract, tags, notes, attachments.

## Fetching Annotations

Zotero stores PDF annotations as child items of type `annotation`:

```
GET /groups/{groupID}/items?itemType=annotation&format=json
```

Each annotation has: `annotationText` (highlighted text), `annotationComment` (your note), `annotationColor`, `parentItem` (the paper it belongs to), `annotationPosition` (page + coordinates).

Map annotation colors to types if the team uses a color convention:
- Yellow → key claim
- Red → critique or concern  
- Green → methodology note
- Blue → follow-up or question

## Incremental Sync

Use the `Since-Version` header to fetch only items modified since the last sync:

```
GET /groups/{groupID}/items?since={version}&format=json
```

Store the `Last-Modified-Version` from the response header — use it as `since` next time.

## Writing Back to Zotero

### Add a note to a paper
```
POST /groups/{groupID}/items
Body: {
  "itemType": "note",
  "parentItem": "{itemKey}",
  "note": "<p>PaperClaw summary: ...</p>",
  "tags": [{"tag": "paperclaw-summary"}]
}
```

### Add a tag to an item
```
PATCH /groups/{groupID}/items/{itemKey}
Body: {"tags": [{"tag": "paperclaw-reviewed"}, {"tag": "key-paper"}]}
```

## Exporting BibTeX

```
GET /groups/{groupID}/items?format=bibtex
```

Or for a single collection:
```
GET /groups/{groupID}/collections/{collectionKey}/items?format=bibtex
```

## Finding Duplicates

Zotero doesn't deduplicate automatically. When syncing, check for duplicate DOIs:
1. Build a `{doi: item_key}` map from all items
2. Flag DOIs that appear more than once
3. Report duplicates to the user for manual resolution

## Common Operations

| Task | API Call |
|------|----------|
| List all collections | `GET /groups/{id}/collections` |
| Get items in collection | `GET /groups/{id}/collections/{key}/items` |
| Get all annotations | `GET /groups/{id}/items?itemType=annotation` |
| Add a note | `POST /groups/{id}/items` with `itemType=note` |
| Export BibTeX | `GET /groups/{id}/items?format=bibtex` |
| Get recent items | `GET /groups/{id}/items?sort=dateModified&direction=desc&limit=25` |

## Rate Limits

Zotero API: 10 requests/second. Add delays between bulk operations.

## Integration Notes

- Use `annotation-sharing` after syncing — annotations pulled from Zotero feed into the shared annotation layer
- Use `reading-coverage` — items in Zotero are counted as "read" by the member who added them
- Use `living-review` after sync — new Zotero items can be auto-ingested into the review corpus
