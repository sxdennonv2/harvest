# Dimensions of the AI-training pipelines

The axes of the course-generation pipelines, named so the whole space can be seen and
expanded before the detail is infilled. **Two pipelines** (Stuart's split, 2026-07-04):
`teach-buying-analyst/` teaches **application functionality**; `communication/` teaches
**writing & communication craft**. Boundary rule: *if the lesson would survive the app
being swapped, it belongs in communication.* ✅ = populated.

## The axes

| Dimension | Kind | Values today | Owned by |
|---|---|---|---|
| `pipeline` | top-level split | app-functionality ✅ (4 courses, 53 pages) · communication ✅ (11 pages, 4 contexts bound) | decision, FRAME-LEDGER; the ladder is invariant **across pipelines** |
| `application` | swappable tree root (functionality pipeline); binding `context` (communication pipeline: email ✅ · document ✅ · slides ✅ · chat ✅ — rebound 2026-07-05 via the context-rebind element) | Excel ✅ 20 · Outlook ✅ 13 · PowerPoint ✅ 10 · Word ✅ 10 — all complete (built 2026-07-04) | frame (one course.json each) — **all four applications now framed**; ladder asserted invariant across all 5 frames |
| `theme` | swappable tree, nested in application | Excel: Source & prepare · Summarise & analyse · Report & visualise · Communicate & present · Automate the repetitive (all ✅) · Outlook: Triage & organise · Find & retrieve · Write & respond · Schedule & coordinate · Automate the repetitive (elicited, 0 lessons) | frame — elicited per app: *"what are the fundamental pillars of functionality within {app}?"* |
| `lesson` | tree leaf, nested in theme (+ subcards; `builds_on` DAG edges) | 223 static pages ✅ (64 authored + 159 persona variants); zero candidates anywhere; `enumerate_permutations.py` computes built/pending from disk | frame |
| `rung` | **invariant crosscutting ladder** | 1 Manual craft · 2 Aldi:GPT · 3 M365 Copilot · 4 GitHub Copilot | org — the GenAI adoption model; swap the org, swap the ladder |
| `element` | invariant crosscutting, within every lesson page | 20 slots: heading, mission-tie, practice-pointer, one-idea, persona-relevance, bad-habit, manual-craft, quiz, try-real, rung-move ×3, … | CONTRACT.md |
| `persona` | binding parameter | buying analyst ✅ (source) · specialist/analyst ✅ · manager/director ✅ · office assistant ✅ — all four families built 2026-07-04 (PRs #23–#25); communication is persona-wide by its MISSION | course — family dir = persona binding; renders element bindings per CONTRACT.md's persona-variant translation ruling |
| `tier` | deployment | static (build-time, host-anywhere) ✅ · live (runtime teacher, cloud) | same frame + contract serve both |

*(History: the pipeline split began life on 2026-07-04 as a latent `competency` axis —
craft vs mechanics — spotted inside the theme dimension. Stuart promoted it to the
top-level `pipeline` split the same day, superseding the rule-of-three deferral: the
survey's dominant demand sat on the craft side, so the third sighting wasn't worth
waiting for.)*

## How they compose

```
pipeline → tree → theme → lesson        functionality: tree root = application
                                        communication: one tree; lessons bind to contexts
lesson × rung                           the ladder climb inside every page (both pipelines)
lesson × element                        the unit contract (page anatomy, both pipelines)
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

## Progress map (standard process)

The estate's live progress map is **`ai_training/dimension-map.html`** — the working
instrument for seeing the whole space at once: stats bar, axes chips, app × theme cards,
theme × rung grid, the `builds_on` DAG, the contract-compliance matrix, the
persona × application grid, and the milestone ledger.

**The file in this repo is the source of truth; the artifact is its deployment.**
Standing artifact URL (Stuart's bookmark — always redeploy to this URL, never mint a new
one): https://claude.ai/code/artifact/cc3747fc-fcfe-4f93-b6d7-4a0fb3d4be1d

Mandatory close of every merged batch or milestone — same standing as running the
verifier; **a batch is not closed until the map shows it**:

1. Refresh the numbers from the instruments: `enumerate_permutations.py`
   (built / pending / total) and `verify_lessons.py` (pass state).
2. Update `dimension-map.html`: the stats bar, any axis chips or grids the batch moved,
   and one new milestone card in § decisions (what merged, which PRs, what it proves).
3. Redeploy the file to the standing artifact URL (favicon 🌾, same URL every time) and
   commit the file change — with the batch's PR or an immediate docs PR.

(History: the map originally lived only in a session scratchpad and was lost when that
session ended — 2026-07-04's persona sweep ran without it until Stuart noticed. Hence
this section.)

## Beyond this pipeline

This file describes one instance of the Harvest shape (enumeration-expanded). A sibling
instance runs stream-expanded (social replies against generated posts). What transfers is
exactly the discipline above: axes as data, one unit per skill invocation, contract as the
floor. See `~/Documents/studio/FRAME-LEDGER.md`.
