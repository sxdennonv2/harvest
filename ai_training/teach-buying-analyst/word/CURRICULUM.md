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
_None authored yet. 10 candidates enumerated in `course.json`, survey-tagged. First up
by demand: **Styles, not formatting: fix it once** — the foundation every other theme
hangs off (nav pane, TOC, and template consistency all inherit from the heading
hierarchy)._
<!-- END:auto:lessons -->

## The grid

<!-- BEGIN:auto:grid -->
| Theme ↓ / Rung → | 1 · Manual craft | 2 · Aldi:GPT | 3 · M365 Copilot | 4 · GitHub Copilot |
|---|---|---|---|---|
| **Styles: the document's skeleton** | 2 candidates | Design the style set for the document you describe | Apply consistent styles across this draft, in place | Build a styled document from a plain-text draft |
| **Structure & navigation** | 2 candidates | Plan the section structure for the document you describe | Insert and update the table of contents; reorganise via headings | Restructure a document file to a given outline by script |
| **Tables & figures** | 2 candidates | Choose table vs figure vs prose for the content you describe | Format this table consistently; add captions throughout | Generate the document's tables from the data files |
| **Review & collaborate** | 2 candidates ← GDM reality | Triage this list of reviewer comments: accept, push back, or discuss | Summarise what changed in this reviewed document | Build a compare-and-report pass across document versions |
| **Templates & consistency** | 2 candidates | Turn the document you describe into a template checklist | Create a new document from the organisation's template | Build the organisation's document template from a brand spec |
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
