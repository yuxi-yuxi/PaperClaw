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
| "DOI link is not corresponding to the paper" | Ran DOI verification script, found 4 mismatches (peters2021, dedeurwaerdere2021, azizi2020, bailey2018), corrected all |

**Standard:** Always verify DOIs are correct and functional. Use Semantic Scholar API to confirm paper metadata before adding citations. Test DOI links resolve to the correct paper.

**DOI Verification Workflow:**
1. Before adding a paper, verify the DOI resolves to the correct paper via Semantic Scholar API:
   ```
   GET https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=title,authors,year
   ```
2. Compare the returned title with the expected title using **Jaccard similarity (word overlap)**:
   - Normalize both titles: lowercase, remove punctuation, collapse whitespace
   - Calculate word intersection / word union ratio
   - Require >50% word overlap to consider a match
   - **WARNING:** Do NOT use prefix matching (e.g., comparing first 20 characters) — this is unreliable and will miss mismatches where titles share common starting words

3. For living reviews, run periodic verification:
   ```bash
   python reviews/monoamine-interactions/update_review.py --verify
   ```

4. Common DOI issues to watch for:
   - DOI copied from wrong paper in search results
   - DOI changed during journal transfer
   - Preprint DOI vs published DOI mismatch
   - Character encoding issues in DOI strings

**Lesson Learned (2026-04-11):** Prefix-based title matching failed to detect mismatches like "An Update on the Role of Serotonin..." vs "The interplay of serotonin..." because both started with common words. Jaccard similarity is more robust because it considers the full title content.

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
- Design system: `DESIGN.MD` (Apple-inspired styling)

## Design System (DESIGN.MD)
For HTML report visualization, follow the Apple-inspired design system in `DESIGN.MD`:

### Key Design Principles
- **Typography**: SF Pro Display (20px+) for headings, SF Pro Text (<20px) for body
- **Colors**: Binary light/dark section rhythm (#000000 ↔ #f5f5f7), Apple Blue (#0071e3) only for interactive elements
- **Line heights**: Tight for headlines (1.07-1.14), comfortable for body (1.47)
- **Letter spacing**: Negative tracking at all sizes (-0.28px at 56px, -0.374px at 17px)
- **CTAs**: Pill-shaped buttons (980px radius) for primary actions
- **Shadows**: Soft, diffused (`rgba(0,0,0,0.22) 3px 5px 30px`) or none
- **Sections**: Alternating dark/light backgrounds for cinematic pacing
- **Max width**: 980px container for content

### Section Layout
- Hero: Black background, centered title, meta pills, key finding card
- Content sections: Alternate between white (#fff), light gray (#f5f5f7), and black (#000)
- Tables: Rounded corners (12px), dark header (#1d1d1f), subtle shadows
- Cards: White background, 12px radius, soft shadow
