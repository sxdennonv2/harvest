# Curriculum — PowerPoint (Buying Analyst, 1x → 10x)

Instance #4 of the pattern. Frame drafted 2026-07-05; no lessons authored yet. Same two
axes as the siblings: **rows = task themes** from PowerPoint's functional pillars
weighted by the NBUY survey; **columns = the invariant capability ladder**.

## How these themes were derived

Elicitation primitive: *"What are the fundamental pillars of functionality within
PowerPoint?"* — checked against the survey (31 respondents):

| Survey cluster | Lands in theme |
|---|---|
| "Refining PPT or training material"; "formatting" | Arrange & align · Build on the master |
| "Creating graphs or images for reporting" | Charts & visuals |
| "Get ideas on formatting and templates" | Reuse & templates · Build on the master |
| "Preparing presentations or external facing documents" | Present & share |

Theme order follows the making of a deck: foundations → tidy → visuals → reuse →
present. **The pipeline boundary applies here with force:** what a slide *says* — one
message per slide, the narrative arc, the headline — is communication craft, and the
communication course's lessons will rebind to the **slides context** for exactly that.
This course teaches the deck as an artifact: masters, alignment, the Excel seam,
templates, the last mile.

## Lessons so far (by theme)

<!-- BEGIN:auto:lessons -->
### Build on the master

- [0001 — Masters & layouts: fix it once, fix it everywhere](lessons/masters-and-layouts-fix-it-once.html)
- [0002 — Placeholders, not text boxes](lessons/placeholders-not-text-boxes.html)

### Arrange & align

- [0003 — Align, distribute, group: the tidy slide](lessons/align-distribute-group.html)
- [0004 — Whitespace & hierarchy: less on the slide](lessons/whitespace-and-hierarchy.html)

### Charts & visuals

- [0005 — Excel to slide: paste-link, never screenshot](lessons/excel-to-slide-paste-link.html)
- [0006 — One chart, one point](lessons/one-chart-one-point.html)

### Reuse & templates

- [0007 — Working the corporate template (not against it)](lessons/working-the-corporate-template.html)
- [0008 — Reusable slides: steal from yourself](lessons/reusable-slides-steal-from-yourself.html)

### Present & share

- [0009 — Presenter view & rehearse](lessons/presenter-view-and-rehearse.html)
- [0010 — Export & share: PDF, handouts, the deck that travels](lessons/export-and-share.html)
<!-- END:auto:lessons -->

## The grid

<!-- BEGIN:auto:grid -->
| Theme ↓ / Rung → | 1 · Manual craft (do it well by hand) | 2 · Aldi:GPT (chat, no tool use) | 3 · M365 Copilot (acts in PowerPoint) | 4 · GitHub Copilot (builds the deck) |
|---|---|---|---|---|
| **Build on the master** | ✅ [0001 Masters & layouts](lessons/masters-and-layouts-fix-it-once.html); ✅ [0002 Placeholders](lessons/placeholders-not-text-boxes.html); slide masters, layouts, placeholders — the deck's skeleton | Plan the deck's structure: which layouts, in what order | Create the section skeleton from a prompt or a document | Build the deck skeleton from an outline file, on the right layouts |
| **Arrange & align** | ✅ [0003 Align & distribute](lessons/align-distribute-group.html); ✅ [0004 Whitespace & hierarchy](lessons/whitespace-and-hierarchy.html); guides, distribute, grouping — the formatting demand | Diagnose a slide you describe: what makes it look untidy | Apply Designer suggestions — then audit what it changed | Batch-fix alignment and spacing across a deck by script |
| **Charts & visuals** | ✅ [0005 Excel to slide](lessons/excel-to-slide-paste-link.html); ✅ [0006 One chart, one point](lessons/one-chart-one-point.html); data onto slides; the Excel seam (paste-link, not screenshot) | Pick the right visual for the point you describe | Create a slide visualising this data, in the deck | Generate the charts into the deck from the data files |
| **Reuse & templates** | ✅ [0007 Corporate template](lessons/working-the-corporate-template.html); ✅ [0008 Reusable slides](lessons/reusable-slides-steal-from-yourself.html); the corporate template; theme colours/fonts; reusable slides | Turn a deck you describe into a reusable template checklist | Create a new deck from the organisation's template | Build the organisation template itself from a brand spec |
| **Present & share** | ✅ [0009 Presenter view](lessons/presenter-view-and-rehearse.html); ✅ [0010 Export & share](lessons/export-and-share.html); presenter view, rehearse, export — the last mile | Build the pre-presentation checklist for the room you describe | Summarise this deck for the follow-up email | Build the export pack (PDF, handouts, notes pages) by script |
<!-- END:auto:grid -->

## Practice artefact (decision pending first lesson)

A **practice deck**: deliberately untidy slides (misaligned blocks, a screenshot where
a linked chart should be, text boxes fighting placeholders) built on a recognisable
mock-corporate master — rung 4 rebuilds it from scratch via python-pptx, which the
repo's own `pptx` tooling can generate at authoring time. Fictional suppliers shared
with the course family.

## Notes for the build

- `build_contents.py` runs here unchanged once `index.html` and a first lesson exist.
- Rung 3 honesty: Copilot in PowerPoint creates slides/decks from prompts and files
  and applies Designer suggestions; it does not reliably restyle an existing deck to a
  corporate master — keep prompts inside what it does.
- Rung 4 is unusually strong in this course: python-pptx makes "builds the deck" a
  literal, verifiable claim.
