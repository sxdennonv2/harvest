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
_None authored yet. 10 candidates enumerated in `course.json`, survey-tagged. First
up by demand: **Align, distribute, group: the tidy slide** (the "refining PPT"
cluster) — or **Excel to slide: paste-link, never screenshot**, which closes a loop
the Excel course opened._
<!-- END:auto:lessons -->

## The grid

<!-- BEGIN:auto:grid -->
| Theme ↓ / Rung → | 1 · Manual craft | 2 · Aldi:GPT | 3 · M365 Copilot | 4 · GitHub Copilot |
|---|---|---|---|---|
| **Build on the master** | 2 candidates | Plan the deck's structure: which layouts, in what order | Create the section skeleton from a prompt or a document | Build the deck skeleton from an outline file, on the right layouts |
| **Arrange & align** | 2 candidates ← survey demand | Diagnose a slide you describe: what makes it look untidy | Apply Designer suggestions — then audit what it changed | Batch-fix alignment and spacing across a deck by script |
| **Charts & visuals** | 2 candidates | Pick the right visual for the point you describe | Create a slide visualising this data, in the deck | Generate the charts into the deck from the data files |
| **Reuse & templates** | 2 candidates | Turn a deck you describe into a reusable template checklist | Create a new deck from the organisation's template | Build the organisation template itself from a brand spec |
| **Present & share** | 2 candidates | Build the pre-presentation checklist for the room you describe | Summarise this deck for the follow-up email | Build the export pack (PDF, handouts, notes pages) by script |
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
