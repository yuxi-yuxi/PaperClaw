# PaperClaw Literature Review Standards

## Project Overview
PaperClaw is used for conducting comprehensive literature reviews using Semantic Scholar API for paper search and Zotero API for reference management.

## Literature Review Quality Standards

### 1. Paper Selection
| User Request | Action Taken |
|--------------|--------------|
| "Too many reviews, focus on original research" | Search specifically for optogenetics, fiber photometry, circuit-level papers with experimental data rather than review articles |
| Added 5 original research papers with circuit mechanisms (Wang 2019, Browne 2018, Miyazaki 2018, Rahaman 2022, Liu 2025) |

**Standard:** Prioritize original research papers over reviews. Organize papers into categories:
- Highly Cited Foundational Papers
- Original Research - Circuit Mechanisms
- Reviews & Synthesis
- Recent Advances

### 2. Citations for Every Statement
| User Request | Action Taken |
|--------------|--------------|
| "Add original research paper reference to each point/statement you summarized" | Added inline citations with DOI links to all claims in all sections |

**Standard:** Every factual claim or mechanism described must have an inline citation linking to the original research paper. Format: `(<a href="DOI_URL" target="_blank">Author et al., Year</a>)`

### 3. DOI Accuracy
| User Request | Action Taken |
|--------------|--------------|
| "The DOI link for Wang et al., 2019 is not correct" | Verified correct DOI via Semantic Scholar API and updated all 7 instances |

**Standard:** Always verify DOIs are correct and functional. Use Semantic Scholar API to confirm paper metadata before adding citations. Test DOI links resolve to the correct paper.

### 4. Shareable Format
| User Request | Action Taken |
|--------------|--------------|
| "Is there a way I can share the report in a more readable way?" | Converted markdown to styled HTML, pushed to GitHub, enabled GitHub Pages |
| "Add links to papers referred in the report" | Added clickable DOI links to all paper references |

**Standard:** Generate HTML reports with:
- Styled, professional layout
- Clickable DOI links for all papers
- Host on GitHub Pages for easy sharing
- Include paper list with citation counts and tags (original, preprint, recent)

### 5. Completeness Check
| User Request | Action Taken |
|--------------|--------------|
| "Why did we miss this paper?" (Yang et al. 2023 bioRxiv) | Explained search limitations (low citations, preprint, query mismatch), then manually added the paper |

**Standard:** After initial search, ask user if there are specific papers they expected to find. Be transparent about search limitations:
- Low-citation papers may be missed
- Preprints indexed differently
- Query terms may not match all relevant papers

## API Configuration
- Semantic Scholar API key: stored in `.env`
- Zotero API key and Group ID: stored in `.env`
- Rate limits: Use API key to avoid 429 errors

## Output Deliverables
1. **HTML Report** - Styled, shareable via GitHub Pages
2. **Markdown Report** - For local reference
3. **Zotero Library** - Papers saved with summaries in notes
4. **DOI Links** - All papers have clickable DOI links

## File Locations
- HTML Report: `literature_review_*.html`
- Markdown Report: `literature_review_*.md`
- API credentials: `.env` (not committed)
