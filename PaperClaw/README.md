# PaperClaw

**A production-ready OpenClaw skill library for academic research teams**

[![Skills](https://img.shields.io/badge/skills-27-blue?style=flat-square)](./skills)
[![Literature](https://img.shields.io/badge/📚_literature-6-purple?style=flat-square)](./skills/literature)
[![Synthesis](https://img.shields.io/badge/🔬_synthesis-5-green?style=flat-square)](./skills/synthesis)
[![Collaboration](https://img.shields.io/badge/🤝_collaboration-5-orange?style=flat-square)](./skills/collaboration)
[![Output](https://img.shields.io/badge/✍️_output-6-red?style=flat-square)](./skills/output)
[![Tracking](https://img.shields.io/badge/📊_tracking-5-teal?style=flat-square)](./skills/tracking)
[![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)](./LICENSE)

PaperClaw packages **27 production-ready `SKILL.md` files** for academic knowledge management and research collaboration workflows. Each skill teaches an OpenClaw-compatible agent **when** to invoke a capability, **how** to execute it, and **what** to produce — grounded in real APIs, formats, and academic conventions.

> **PaperClaw is the knowledge management complement to [LabClaw](https://github.com/wu-yc/LabClaw).** Where LabClaw equips agents to execute biomedical experiments (bioinformatics pipelines, molecular docking, clinical data), PaperClaw equips teams to manage what they know — tracking literature, synthesizing findings, coordinating reading, and writing outputs.

---

## At a Glance

| Domain | Skills | Focus |
|--------|--------|-------|
| [📚 Literature](#-literature--6-skills) | **6** | Paper discovery, monitoring, citation networks, database search |
| [🔬 Synthesis](#-synthesis--5-skills) | **5** | Contradiction detection, consensus mapping, cross-paper synthesis, evidence grading |
| [🤝 Collaboration](#-collaboration--5-skills) | **5** | Annotation sharing, reading coverage, expertise mapping, knowledge handoffs |
| [✍️ Output](#️-output--6-skills) | **6** | Draft generation, grant writing, review responses, abstracts, rebuttals |
| [📊 Tracking](#-tracking--5-skills) | **5** | Hypothesis versioning, experiment logging, reproducibility, preprint and citation monitoring |

---

## Quick Start

OpenClaw loads workspace skills from `<workspace>/skills`. Install PaperClaw:

```bash
git clone https://github.com/YOUR_USERNAME/PaperClaw.git
mkdir -p ~/.openclaw/workspace/skills
cp -R PaperClaw/skills/* ~/.openclaw/workspace/skills/
```

Then start a new OpenClaw session. The agent discovers the skill folders and indexes them automatically.

Install alongside LabClaw if you want both research execution and knowledge management:

```bash
cp -R LabClaw/skills/* ~/.openclaw/workspace/skills/
cp -R PaperClaw/skills/* ~/.openclaw/workspace/skills/
```

---

## Representative Workflows

| Workflow | Skills used |
|----------|------------|
| Start a new research area | `arxiv-monitor` → `living-review` → `gap-detection` → `hypothesis-versioning` |
| Write a paper | `cross-paper-synthesis` → `draft-generation` → `abstract-writing` → `reproducibility-check` |
| Respond to reviewers | `review-response` → `evidence-grading` → `rebuttal-writing` |
| Prepare a lab meeting | `reading-coverage` → `team-sync` → `annotation-sharing` |
| Offboard a team member | `expertise-mapping` → `reading-coverage` → `lab-knowledge-handoff` |
| Write a grant | `gap-detection` → `consensus-mapping` → `grant-writing` |
| Track competitor work | `preprint-watch` → `citation-alert` → `contradiction-detection` |
| Verify a claim before building on it | `claim-tracker` → `evidence-grading` → `semantic-scholar` |

---

## Skill Catalog

### 📚 Literature — 6 skills

Skills for discovering, fetching, and structuring the academic literature.

| Skill | Description |
|-------|-------------|
| [`living-review`](./skills/literature/living-review/SKILL.md) | Maintains a continuously updated, versioned synthesis of the team's collective reading. Ingest papers, generate structured reviews, diff what changed. |
| [`arxiv-monitor`](./skills/literature/arxiv-monitor/SKILL.md) | Monitors arXiv by topic, author, or category. Relevance scoring, weekly digests, competitor activity alerts. |
| [`citation-graph`](./skills/literature/citation-graph/SKILL.md) | Builds citation networks from a seed paper set. Community detection, centrality metrics, coverage gap identification. |
| [`gap-detection`](./skills/literature/gap-detection/SKILL.md) | Finds what the field hasn't studied. Classifies gaps as empirical, methodological, theoretical, applied, or replication failures. Validates novelty of proposed contributions. |
| [`semantic-scholar`](./skills/literature/semantic-scholar/SKILL.md) | Searches and retrieves paper metadata, citations, references, and author profiles from Semantic Scholar (200M+ papers). Batch DOI/arXiv lookups, TLDR summaries, author h-index. |
| [`zotero-integration`](./skills/literature/zotero-integration/SKILL.md) | Connects to team Zotero group libraries via the Zotero Web API. Import collections and annotations, sync reading status, export BibTeX, write summaries back to Zotero items. |

### 🔬 Synthesis — 5 skills

Skills for extracting understanding across multiple papers.

| Skill | Description |
|-------|-------------|
| [`contradiction-detection`](./skills/synthesis/contradiction-detection/SKILL.md) | Scans a corpus for conflicting empirical claims. Classifies contradictions by type and severity. Proposes causes and flags for discussion. |
| [`consensus-mapping`](./skills/synthesis/consensus-mapping/SKILL.md) | Maps settled vs. contested science with agreement rates, recency weighting, and meta-analysis override. Generates calibrated prose for grant backgrounds. |
| [`claim-tracker`](./skills/synthesis/claim-tracker/SKILL.md) | Version-controlled registry of scientific claims with provenance traces. Retraction Watch integration. Tracks status: standing, challenged, refined, refuted. |
| [`cross-paper-synthesis`](./skills/synthesis/cross-paper-synthesis/SKILL.md) | Synthesizes across 5–100 papers in four modes: narrative synthesis, structured comparison tables, temporal evolution, and cross-domain synthesis. |
| [`evidence-grading`](./skills/synthesis/evidence-grading/SKILL.md) | Grades evidence strength from A (widely replicated) to F (retracted). Maps grades to hedging language. Supports both ML/CS and biomedical grading schemas. |

### 🤝 Collaboration — 5 skills

Skills for team knowledge coordination.

| Skill | Description |
|-------|-------------|
| [`annotation-sharing`](./skills/collaboration/annotation-sharing/SKILL.md) | Shares PDF annotations across the team. Threaded discussions, color-coded annotation types, search across all team notes. Hypothesis import from Zotero and Hypothesis. |
| [`expertise-mapping`](./skills/collaboration/expertise-mapping/SKILL.md) | Builds expertise profiles from reading history and annotation activity. Answers "who knows most about X" and "who should review this draft". Identifies team knowledge gaps. |
| [`lab-knowledge-handoff`](./skills/collaboration/lab-knowledge-handoff/SKILL.md) | Packages a departing member's knowledge into a structured handoff document: expertise portrait, open threads, tacit knowledge interview template, successor onboarding guide. |
| [`reading-coverage`](./skills/collaboration/reading-coverage/SKILL.md) | Tracks who has read what across the team's corpus. Identifies single-reader papers (handoff risk), generates reading assignments weighted by expertise and workload. |
| [`team-sync`](./skills/collaboration/team-sync/SKILL.md) | Generates lab meeting agendas from real team activity. Paper discussion questions across comprehension, critical, relevance, and extension categories. Meeting summary extraction. |

### ✍️ Output — 6 skills

Skills for producing research artifacts.

| Skill | Description |
|-------|-------------|
| [`draft-generation`](./skills/output/draft-generation/SKILL.md) | Generates manuscript sections grounded in the team's literature corpus. Introductions, related work, methods, discussion. All claims citation-traced. Hedging calibrated to evidence grades. |
| [`grant-writing`](./skills/output/grant-writing/SKILL.md) | Agency-specific grant sections: NIH Specific Aims, Significance, Innovation, Approach; NSF Intellectual Merit and Broader Impacts; ERC formats. Preliminary data framing from experiment logs. |
| [`review-response`](./skills/output/review-response/SKILL.md) | Drafts point-by-point journal revision responses. Triages reviewer comments by type and impact. Formats cover letters. Finds literature to address reviewer concerns. |
| [`abstract-writing`](./skills/output/abstract-writing/SKILL.md) | Drafts venue-appropriate abstracts: unstructured (ML conferences), structured (biomedical journals), extended abstracts, and lay summaries. Multiple word counts and variants. |
| [`rebuttal-writing`](./skills/output/rebuttal-writing/SKILL.md) | Drafts word-budget-aware conference rebuttals for NeurIPS, ICML, ICLR, ACL, CVPR. Strategic triage, shared concern handling, and respectful pushback templates. |
| [`presentation-deck`](./skills/output/presentation-deck/SKILL.md) | Slide outlines and speaker notes for conference talks, lab meetings, thesis defenses, and invited seminars. Slide counts by duration. Paper presentation discussion guides. |

### 📊 Tracking — 5 skills

Skills for maintaining research state over time.

| Skill | Description |
|-------|-------------|
| [`hypothesis-versioning`](./skills/tracking/hypothesis-versioning/SKILL.md) | Version-controlled hypothesis registry with confidence scores, evidence chains, and falsification criteria. Tracks status from active through confirmed, refined, or refuted. |
| [`experiment-log`](./skills/tracking/experiment-log/SKILL.md) | Structured experiment records with full setup, results, findings, and lessons learned. Linked to hypotheses. Compiles preliminary data narratives for grants. |
| [`reproducibility-check`](./skills/tracking/reproducibility-check/SKILL.md) | Pre-submission reproducibility audit against venue-specific checklists: NeurIPS/ICML/ICLR ML Reproducibility Checklist, Nature data/code availability requirements, PLOS standards. |
| [`preprint-watch`](./skills/tracking/preprint-watch/SKILL.md) | Monitors tracked preprints for new versions, journal publication, and citation milestones. Version diff summaries. Alerts when competitor preprints are substantially revised. |
| [`citation-alert`](./skills/tracking/citation-alert/SKILL.md) | Monitors incoming citations to team publications. Classifies by type: extension, comparison, supporting, challenging, background. Citation velocity tracking and community analysis. |

---

## Repository Layout

```
PaperClaw/
├── README.md
└── skills/
    ├── literature/     # 6 skills: discovery, monitoring, search, citation graphs
    ├── synthesis/      # 5 skills: contradiction, consensus, claim tracking, synthesis
    ├── collaboration/  # 5 skills: annotations, coverage, expertise, handoffs, sync
    ├── output/         # 6 skills: drafts, grants, reviews, abstracts, presentations
    └── tracking/       # 5 skills: hypotheses, experiments, reproducibility, monitoring
```

## Skill Format

Every `SKILL.md` follows the OpenClaw skill specification:

```
---
name: skill-name
description: Trigger description — what the skill does and when to use it.
             The agent reads ONLY this field to decide whether to invoke the skill.
             Include trigger phrases and use cases.
---

# Skill Name

[Markdown body — actual agent instructions. Only loaded after the skill triggers.
Includes: API endpoints, data formats, decision logic, output templates.]
```

## Related Repositories

| Repository | Relationship |
|------------|-------------|
| [`wu-yc/LabClaw`](https://github.com/wu-yc/LabClaw) | Sister library — 211 biomedical execution skills (bioinformatics, drug discovery, clinical). PaperClaw is the knowledge management complement. |
| [`openclaw/openclaw`](https://github.com/openclaw/openclaw) | The runtime that loads and invokes skills. Both LabClaw and PaperClaw target this agent. |
| [`openclaw/clawhub`](https://github.com/openclaw/clawhub) | Public skill registry. Individual PaperClaw skills can be published here separately. |
| [`mims-harvard/ToolUniverse`](https://github.com/mims-harvard/ToolUniverse) | Biomedical tool ecosystem. LabClaw wraps many ToolUniverse tools; PaperClaw skills complement them at the knowledge layer. |

## License

[MIT License](./LICENSE)
