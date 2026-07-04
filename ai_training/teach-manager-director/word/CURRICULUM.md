# Curriculum — Word (Buying Analyst, 1x → 10x)

Instance #5 of the pattern. Frame drafted 2026-07-05; no lessons authored yet.
**Rows = task themes** from Word's functional pillars weighted by the NBUY survey;
**columns = the invariant capability ladder**.

## How these themes were derived

Elicitation primitive: *"What are the fundamental pillars of functionality within
Word?"* — checked against the survey (31 respondents):

| Survey cluster | Lands in theme |
|---|---|
| "Preparing submissions for GDM or other audiences" | Review & collaborate · Structure & navigation |
| "Training material"; "external facing documents" | Styles · Templates & consistency |
| "Get ideas on formatting and templates" | Templates & consistency |
| (The dominant "wording documents" cluster) | → **communication pipeline** (document context) |

Theme order follows the life of a document: skeleton → structure → content furniture →
review → reuse. **The boundary rule bites hardest here**: most of the survey's Word
demand is about *wording* — which is the communication pipeline's territory, already
built and waiting to rebind to the **document context**. What remains for this course
is the tool: styles, sections, tables, track changes, templates — the machinery that
makes a GDM submission assemble itself instead of being fought into shape.

## Lessons so far (by theme)

<!-- BEGIN:auto:lessons -->
### Styles: the document's skeleton

- [0001 — Styles, not formatting: fix it once](lessons/styles-not-formatting.html)
- [0002 — The heading hierarchy: one outline, three payoffs](lessons/the-heading-hierarchy.html)

### Structure & navigation

- [0003 — Breaks & sections: why your page numbering fights you](lessons/breaks-and-sections.html)
- [0004 — The table of contents that maintains itself](lessons/the-toc-that-maintains-itself.html)

### Tables & figures

- [0005 — Tables that behave: widths, headers, repeat rows](lessons/tables-that-behave.html)
- [0006 — Figures & captions that stay where you put them](lessons/figures-and-captions.html)

### Review & collaborate

- [0007 — Track changes without fear](lessons/track-changes-without-fear.html)
- [0008 — Comments, versions & compare](lessons/comments-versions-and-compare.html)

### Templates & consistency

- [0009 — Working the document template](lessons/working-the-document-template.html)
- [0010 — Building blocks: the reusable clauses](lessons/building-blocks-reusable-clauses.html)
<!-- END:auto:lessons -->

## The grid

<!-- BEGIN:auto:grid -->
| Theme ↓ / Rung → | 1 · Manual craft (do it well by hand) | 2 · Aldi:GPT (chat, no tool use) | 3 · M365 Copilot (acts in Word) | 4 · GitHub Copilot (builds the document) |
|---|---|---|---|---|
| **Styles: the document's skeleton** | ✅ [0001 Styles, not formatting](lessons/styles-not-formatting.html); ✅ [0002 Heading hierarchy](lessons/the-heading-hierarchy.html); styles over manual formatting; heading hierarchy | Design the style set for the document you describe | Apply consistent styles across this draft, in place | Build a styled document from a plain-text draft |
| **Structure & navigation** | ✅ [0003 Breaks & sections](lessons/breaks-and-sections.html); ✅ [0004 Self-maintaining TOC](lessons/the-toc-that-maintains-itself.html); nav pane, TOC, breaks and sections done right | Plan the section structure for the document you describe | Insert and update the table of contents; reorganise via headings | Restructure a document file to a given outline by script |
| **Tables & figures** | ✅ [0005 Tables that behave](lessons/tables-that-behave.html); ✅ [0006 Figures & captions](lessons/figures-and-captions.html); tables that behave; captions; figures that stay put | Choose table vs figure vs prose for the content you describe | Format this table consistently; add captions throughout | Generate the document's tables from the data files |
| **Review & collaborate** | ✅ [0007 Track changes](lessons/track-changes-without-fear.html); ✅ [0008 Comments & compare](lessons/comments-versions-and-compare.html); track changes, comments, compare — the GDM reality | Triage this list of reviewer comments: accept, push back, or discuss | Summarise what changed in this reviewed document | Build a compare-and-report pass across document versions |
| **Templates & consistency** | ✅ [0009 Document template](lessons/working-the-document-template.html); ✅ [0010 Building blocks](lessons/building-blocks-reusable-clauses.html); document templates; theme fonts/colours; building blocks | Turn the document you describe into a template checklist | Create a new document from the organisation's template | Build the organisation's document template from a brand spec |
<!-- END:auto:grid -->

## Practice artefact (decision pending first lesson)

A **practice document pack**: a deliberately manually-formatted GDM-style submission
(bold-and-font-size masquerading as headings, a TOC typed by hand, a table with
drifting widths, one round of messy tracked changes) plus the clean target — rung 4
rebuilds it from a plain-text draft via python-docx, which the repo's own `docx`
tooling can generate at authoring time. Fictional suppliers shared with the family.

## Notes for the build

- `build_contents.py` runs here unchanged once `index.html` and a first lesson exist.
- Rung 3 honesty: Copilot in Word drafts, rewrites and summarises in the document;
  style application and TOC mechanics are partly native Word features — prompts must
  not attribute native buttons to Copilot.
- Building-blocks candidate is the deliberate sibling of Outlook's Quick Parts —
  same one-idea family, different host; the lessons should cross-reference by slug.
