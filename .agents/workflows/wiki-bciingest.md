---
description: Ingest a source document into the Bicultural Integration Exchange Wiki
---

# /wiki-bciingest — Ingest Document into the Bicultural Integration Wiki

Use this workflow to ingest a document from any related workspace (e.g. DeeperpointBusiness, DeeperPointWiki) into this bicultural wiki.

### How to invoke

> `/wiki-bciingest /Users/mustafauzumeri/Documents/GitHub/DeeperpointBusiness/Analysis/2026-06-18-bicultural-onboarding-prospectus.md`
> `/wiki-bciingest /Users/mustafauzumeri/Documents/GitHub/DeeperpointBusiness/Analysis/2026-06-18-storyboard-competitive-landscape.md`

---

### What the agent will do

#### Step 1 — Classify and Load Source
1. **Determine classification:** Is this stable intellectual/protocol content (→ `source` + concept/protocol/pedagogy pipeline) or volatile delivery content (→ `reference` stub only)?
   - **Ingest path:** cultural protocols, storytelling pedagogies, bicultural matching concepts, design analyses, proposals.
   - **Reference path:** project staffing roadmaps, developer timelines, local directory setups.
2. Load the document content.

#### Step 2 — Plan Edits
Read `wiki/index.md` and existing pages. Identify:
- Which `wiki/pages/concepts/` or `wiki/pages/protocols/` or `wiki/pages/pedagogy/` pages need creating or updating.
- Which `wiki/pages/entities/` or `wiki/pages/initiatives/` pages need creating or updating.
- Whether to create a `source` page, `story` page, or `reference` stub.

Present the JSON plan to the user for confirmation. **Wait for approval before writing.**

#### Step 3 — Execute Updates
Once approved:
1. Create or update the source/story/reference page.
2. Update concept, protocol, pedagogy, and entity pages with inline citations.
3. Handle contradictions: wrap in `### Contradiction` block, set `status: contradicted`.
4. Update `wiki/index.md` and `wiki/log.md`.

   **Semantic Summary Rule:** Every `index.md` entry must describe what the page *knows*, not where it came from. For reference pages: one sentence stating what the linked document covers.
   
   **Culture & Design primacy:** If the ingested document contradicts Treaty 7 storytelling traditions or core Cosolvent-CommonContext integration principles, state this explicitly in a contradiction note.

#### Step 4 — Validate
```bash
python scripts/validate_wiki.py
```
Fix any errors and re-run until clean.

#### Step 5 — Commit
```bash
git add wiki/
git commit -m "WIKI: Ingested <document_name> and compiled pages"
```
