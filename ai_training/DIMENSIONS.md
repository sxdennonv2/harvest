# Dimensions of the AI-training pipeline

The axes of the course-generation pipeline, named so the whole space can be seen and
expanded before the detail is infilled. One instance (Excel) is fully built; the rest of
the space is addressable but empty. ✅ = populated.

## The axes

| Dimension | Kind | Values today | Owned by |
|---|---|---|---|
| `application` | swappable tree root | Excel ✅ · Outlook (frame drafted 2026-07-04) · PowerPoint · Word | frame (one course.json each) |
| `theme` | swappable tree, nested in application | Excel: Source & prepare · Summarise & analyse · Report & visualise · Communicate & present · Automate the repetitive (all ✅) · Outlook: Triage & organise · Find & retrieve · Write & respond · Schedule & coordinate · Automate the repetitive (elicited, 0 lessons) | frame — elicited per app: *"what are the fundamental pillars of functionality within {app}?"* |
| `lesson` | tree leaf, nested in theme (+ subcards; `builds_on` DAG edges) | Excel: 19 ✅ · Outlook: 15 candidates enumerated, survey-tagged | frame |
| `rung` | **invariant crosscutting ladder** | 1 Manual craft · 2 Aldi:GPT · 3 M365 Copilot · 4 GitHub Copilot | org — the GenAI adoption model; swap the org, swap the ladder |
| `element` | invariant crosscutting, within every lesson page | 20 slots: heading, mission-tie, practice-pointer, one-idea, persona-relevance, bad-habit, manual-craft, quiz, try-real, rung-move ×3, … | CONTRACT.md |
| `persona` | binding parameter | buying analyst ✅ (others latent in the survey: office assistant, manager/director, specialist) | course — renders element bindings ("Why it matters to a **buyer**") |
| `tier` | deployment | static (build-time, host-anywhere) ✅ · live (runtime teacher, cloud) | same frame + contract serve both |

## How they compose

```
application → theme → lesson            the swappable domain tree (frame, data)
lesson × rung                           the ladder climb inside every page
lesson × element                        the unit contract (page anatomy)
element × persona                       the voice/binding layer
everything × tier                       static export or live teacher
```

Not a full cartesian product — nesting prunes it. The projections worth *looking at*:

- **theme × rung** — the course grid (already rendered in CURRICULUM.md / index.html);
- **application × theme** — the four-course map; only Excel's column exists;
- **lesson × element** — the contract compliance matrix (verify's output);
- **persona × application** — the retargeting space (who else buys this).

## The generative prompts (dimension elicitation primitives)

- theme axis: *"What are the fundamental pillars of functionality within {application}?"*
- lesson axis: expand each theme against the survey's expressed needs.
- These prompts are pipeline assets — the frame is reproducible, not hand-curated.

## Beyond this pipeline

This file describes one instance of the Harvest shape (enumeration-expanded). A sibling
instance runs stream-expanded (social replies against generated posts). What transfers is
exactly the discipline above: axes as data, one unit per skill invocation, contract as the
floor. See `~/Documents/studio/FRAME-LEDGER.md`.
