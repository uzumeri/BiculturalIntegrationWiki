<!--Copyright (c) 2026 Mustafa Uzumeri. All rights reserved.-->

# Bicultural Integration Exchange Wiki

This repository contains a local-first knowledge base designed to support the development of a bicultural B2B integration and placement system. It bridges industrial operational standards with First Nations cultural protocols, storytelling pedagogies, and OCAP-compliant governance.

## Folder Structure

*   `wiki/index.md` — The semantic index of all pages in the wiki.
*   `wiki/log.md` — Chronological log of ingestion and edits.
*   `wiki/pages/` — Categories of vault pages:
    *   `protocols/` — Treaty and Nation-specific protocols, calendars, and guidelines.
    *   `pedagogy/` — Narrative translations of industrial SOPs.
    *   `concepts/` — Cosolvent bicultural engine configurations and scheduling models.
    *   `initiatives/` — Specific business models, pilot projects, and startup designs.
    *   `entities/` — Partner organizations, universities (like MRU), and community bodies.
    *   `sources/` — Ingested policy standards (TRC, OCAP).
    *   `stories/` — Scenarios and case studies.

## Tooling & Verification

The wiki includes automated tools to sync source documents and validate integrity:

### 1. Synchronization (`sync_manifest.yaml`)
We sync intellectual files (like bicultural onboarding guides, templates, and analysis papers) from the upstream `DeeperpointBusiness` workspace. To fetch or update source files, run:
```bash
python scripts/sync_sources.py
```
This script will resolve mappings locally within the active workspace first (or download via the GitHub API if offline).

### 2. Ingestion (`/wiki-bciingest`)
Once files are synced into the `sources/` directory, use the custom `/wiki-bciingest` slash command to read, classify, and build/update concepts, protocols, or pedagogy pages:
```
/wiki-bciingest sources/2026-06-18-bicultural-onboarding-prospectus.md
```

### 3. Validation
A local validation script ensures structure, frontmatter schemas, and wikilinks are robust:
```bash
python scripts/validate_wiki.py
```

The wiki is fully compatible with **Obsidian** (open the repository folder as a vault).

---

<!--Copyright (c) 2026 Mustafa Uzumeri. All rights reserved.-->
