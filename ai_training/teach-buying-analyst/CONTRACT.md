# Unit Contract — one lesson page

The unit of this pipeline is **one lesson page**: a single self-contained HTML file that
teaches one tightly-scoped thing four ways, climbing the GenAI ladder. This contract defines
what every lesson page must contain. It is consumed by:

- the **generator** (`lesson-author`) at build time — static tier;
- the **live teacher** at run time — every dynamically produced lesson must satisfy the
  same floor before the learner moves on;
- the **verifier** (`lesson-verify`) at both tiers — the checklist at the end is its spec.

Reverse-engineered from the 19 pages of the Excel reference instance
(`excel/lessons/*.html`, built 2026-07-02). The Excel course is the worked example of every
clause; deviations found during extraction are listed at the end.

## Parameters

A lesson page is rendered from a frame coordinate plus these course-level parameters.
Elements are invariant; **bindings** (headings, voice, artefact kind) vary with parameters.

| Parameter | Excel reference value | Varies with |
|---|---|---|
| `application` | Excel | course |
| `persona` | buying analyst (NBUY, sources via SQL, reports to director) | course/org |
| `ladder` | 1 Manual craft · 2 Aldi:GPT · 3 M365 Copilot · 4 GitHub Copilot | org (shared across courses) |
| `practice_artefact` | shared workbook, one starter tab + hidden soln tab per lesson | application |
| `kicker_prefix` | "Excel to a High Standard" | course |

The ladder is the org's GenAI adoption model. Rung 1 is always the manual craft; every rung
above it is an AI tool with a stated capability boundary (chat-only → acts-in-app →
builds-from-scratch). Swapping the org swaps the ladder, nothing else.

## Ownership

Two classes of element:

- **machine-owned** — written and rewritten by `build_contents.py` from `course.json`.
  Authors emit a well-formed placeholder once; never hand-edit afterwards.
- **author-owned** — produced by the generator (or live teacher) against this contract.

## Elements

In page order. Every element is required unless marked optional.

| # | Element | Owner | Excel binding (reference rendering) |
|---|---|---|---|
| 1 | `title-tag` | machine | `<title>Lesson NNNN — {title}</title>` |
| 2 | `lesson-nav` | machine | Prev / Contents (+cheat sheet) / Next bar |
| 3 | `theme-nav` | machine | "Sections" bar linking each theme's first lesson |
| 4 | `kicker` | machine | "Excel to a High Standard · Lesson NNNN" |
| 5 | `heading` | author | `<h1>` — lesson title, verb-led, one idea only |
| 6 | `mission-tie` | author | `p.mission` — "Tied to your mission: …" |
| 7 | `practice-pointer` | author | `div.workbook` — link to workbook + named tab |
| 8 | `one-idea` | author | `<h2>The one idea</h2>` |
| 9 | `persona-relevance` | author | `<h2>Why it matters to a buyer</h2>` |
| 10 | `bad-habit` | author | `div.callout.bad` — "The bad habit this undoes" |
| 11 | `manual-craft` | author | `<h2>How to do it</h2>` — rung 1, on the practice artefact |
| 12 | `quiz` | author | `<h2>Check yourself</h2>` — 3 questions, instant feedback |
| 13 | `try-real` | author | `<h2>Try it for real</h2>` — task + reconciliation check |
| 14 | `ladder-intro` | author | `<h2>The AI moves — climbing the ladder</h2>` |
| 15 | `rung-move` ×(N−1) | author | `<h3>Rung k · {tool} — {capability}</h3>` + prompt + check |
| 16 | `ladder-point` | author | `div.callout` — "The point of the ladder" |
| 17 | `primary-source` | author | `div.callout` — cited sources + trust-the-source clause |
| 18 | `ask-teacher` | author | `div.ask` — invitation with a concrete retargeting offer |
| 19 | `footer-nav` | machine | duplicate of `lesson-nav` |
| 20 | `behaviours` | author | inline `<script>` — quiz feedback + copy-prompt buttons |

### Element specifications

**heading / one-idea.** One lesson teaches exactly one idea. If the one-idea section needs a
second concept to make sense, the frame is wrong (split the lesson), not the prose. Two short
paragraphs maximum; state the mental model ("sum this range, where that range equals this"),
then the concrete instance.

**mission-tie.** Opens the page by connecting this lesson to the persona's mission — why
*this learner* needs *this skill now*. Written to the persona, not about it.

**practice-pointer.** Names the exact artefact location (tab, file, folder) and what the
learner will find there ("the flat sales list is on the left… waiting for its totals").
The practice artefact always ships **set up but undone**: starter state visible, solution
present but hidden. Never ask the learner to build scaffolding before the lesson starts.

**persona-relevance.** The business case in the persona's world, concrete to their weekly
reality (reports on a director's desk, refresh cycles). Binding heading names the persona.

**bad-habit.** Every lesson names the inherited habit it replaces, and why the habit fails
silently. This is the wedge that motivates relearning something the learner "already does".

**manual-craft.** Rung 1. Exact cells/clicks/keystrokes on the practice artefact — the
learner must be able to complete it from this text alone. Where the technique depends on an
earlier lesson, say so inline ("*Builds on Lesson NNNN:* …") and mirror that edge in the
frame's `builds_on` (see below). Reference lessons by slug-derived link, never by bare
number — numbers are machine-assigned and shift when the frame reorders.

**quiz.** Exactly 3 multiple-choice questions, 4 options each, instant client-side feedback,
no page reload, no tracking. Questions test the mental model, not recall of the prose.

**try-real.** A do-it-now task on the practice artefact **plus a self-verification** the
learner can run without the teacher — the reconciliation pattern ("the four category totals
must sum to a plain SUM of the whole column"). This check is the spine of the page: the
ladder below reuses it verbatim.

**ladder-intro.** Restates the task and declares the invariant check that survives every
rung. One short paragraph.

**rung-move (the load-bearing clause).** One per ladder rung above manual craft. Each is an
inseparable **prompt + check pair**:

- a one-line statement of the tool's capability boundary at this rung ("can't see your
  workbook, so it writes the formula; you place and verify it");
- a **copyable, self-contained prompt** (`textarea` + copy button) — includes all context
  the tool lacks (column meanings, ranges, sheet names), because the prompt travels alone;
- a **check** the learner performs on the output ("click J2 and confirm it's a real SUMIFS
  formula, not a pasted number"), reusing the try-real reconciliation where possible, and
  pre-empting the most likely near-miss ("if it hands you SUMIF (no S)…").

A rung-move without a check is a contract violation, not a style choice. The check is what
makes the ladder safe to climb.

**ladder-point.** Closes the ladder: same deliverable at every rung, the check is what
protects you, craft first so you can supervise.

**primary-source.** 1–3 citations drawn from `RESOURCES.md` (never parametric knowledge),
plus the standing clause: *if this page disagrees with the source, trust the source and tell
me.*

**ask-teacher.** Invites follow-up and makes one **concrete, personalised offer** tied to
this lesson ("send a sanitised extract and I'll retarget this lesson to it"). On the live
tier this is a real capability; on the static tier it routes to the human teacher.

**behaviours.** Everything client-side and dependency-free: quiz feedback and copy buttons
as inline script. No frameworks, no network calls, no analytics.

## Technical constraints

- One lesson = one HTML file at `lessons/{slug}.html`; slug is a stable, opaque identifier —
  filenames never change when the course reorders.
- Self-contained: renders fully offline from the course folder. Only shared course assets
  may be referenced (`../assets/lesson.css`, the practice artefact, `../reference/*`).
  No external network dependency at view time. Print-friendly.
- Machine-owned elements must match `build_contents.py`'s patterns exactly
  (`<nav class="lesson-nav">…</nav>`, `<p class="kicker">…</p>`, `<title>…</title>`,
  `<footer class="lesson-nav">…</footer>`); the builder rewrites them in place and warns on
  any it cannot find.

## Relationship to the frame

The frame (`course.json`) supplies the coordinate; the contract supplies the shape.

- `theme` → which section the lesson belongs to; drives numbering and nav.
- `builds_on: [slug, …]` → prerequisite edges, a DAG over lessons. Encoded from explicit
  dependencies asserted in `manual-craft`/`one-idea` prose. Consumed two ways:
  - **static tier**: the authored order should be a valid topological order of the DAG
    (verify flags violations);
  - **live tier**: the teacher chooses each next lesson freely from the frame — guided by
    the learner's records, **never** ahead of an unmet `builds_on` edge.
- Subcards inherit their parent as an implicit prerequisite.

## Degrees of freedom (live tier)

The live teacher may, above the floor: retarget examples and practice data to the learner's
real (sanitised) extracts; add remediation or stretch sections; re-sequence within the DAG;
rewrite persona bindings to the individual. It may not: drop or merge required elements,
emit a rung-move without its check, skip an unmet prerequisite edge, or cite outside
`RESOURCES.md` without adding the source there first.

## Verify checklist (`lesson-verify` spec)

Mechanical (no judgement):
- [ ] All required elements present, in contract order; machine-owned patterns intact.
- [ ] Every internal link resolves (lessons, assets, artefact, reference pages).
- [ ] Quiz: exactly 3 questions, each with a `data-answer` in range and feedback element.
- [ ] One `rung-move` per ladder rung above rung 1, each containing a `textarea` prompt and
      a check paragraph.
- [ ] No bare lesson-number references in author-owned prose (numbers are machine-owned).
- [ ] Frame: `builds_on` edges acyclic; authored order topologically valid (static tier).

Judged (agent):
- [ ] The page teaches exactly one idea; quiz tests the model, not the wording.
- [ ] Each prompt is self-contained: would work pasted into the named tool by someone with
      only the practice artefact open.
- [ ] Each check would actually catch the most likely failure of its rung.
- [ ] Persona voice consistent; bad-habit is a real habit, concretely stated.
- [ ] Citations exist in `RESOURCES.md` and support the claims they anchor.

## Known deviations in the Excel reference instance (2026-07-04)

1. `relative-and-absolute-references.html` has no `manual-craft` ("How to do it") section —
   predates the contract's final shape. Backfill or formally exempt.
2. ~~Stale bare-number cross-references from the pre-reorder sequence.~~ **Resolved
   2026-07-04**: all ten replaced with slug links or "this lesson".
3. ~~Frame order violates `builds_on`.~~ **Resolved 2026-07-04**: References moved into
   *Source & prepare* as lesson 0001 (its original position); order is now a valid
   topological sort of the DAG. A second, soft violation found during visualisation
   (SUMIFS 0009 leaning on PivotTables 0012 in its opening contrast) was resolved by
   rewording the contrast as a neutral forward link and dropping the edge — the prose
   was the edge's only evidence, and it was a contrast, not a technique prerequisite.
