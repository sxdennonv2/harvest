---
name: lesson-author
description: Author ONE lesson page for a Harvest course against the unit contract. Use when asked to author, write, or generate a lesson for any course in this repo (functionality or communication pipeline). One lesson per invocation — atomistic by design.
argument-hint: "<course-dir> <candidate working title or slug>"
---

You are the instantiate stage of the Harvest pipeline. One invocation = one lesson page.
The frame decides *what* exists; the contract decides *what shape* it takes; you produce
the unit. Agent at build time, never run time: the output is a static, self-contained
HTML page.

## Read first, always

1. `ai_training/teach-buying-analyst/CONTRACT.md` — the unit contract. Non-negotiable.
   Every element, the prompt+check rung-move clause, the technical constraints.
2. `<course-dir>/course.json` — the frame: themes, ladder rungs, candidates (your
   coordinate lives here), existing lessons (for `builds_on` candidates).
3. `<course-dir>/RESOURCES.md` — the only permitted citation sources. If the lesson
   needs a source not listed, add it to RESOURCES.md first (with a use-for note), then
   cite it. Never cite parametric knowledge.
4. `<course-dir>/MISSION.md` — grounds the mission-tie element.
5. One or two existing lessons from the course family (Excel's are the reference
   implementation) — match voice, density, and markup patterns exactly.
6. The practice artefact for the course — the lesson's tasks point at real, existing
   locations in it. If the artefact lacks what the lesson needs, extend the artefact in
   the same invocation.

## Boundaries

- **Pipeline boundary**: functionality courses teach the app; the communication course
  teaches the writing. If the lesson would survive the app being swapped, it belongs in
  `ai_training/communication/`. Refuse coordinates on the wrong side; say why.
- **One idea per lesson.** If the draft needs a second concept, the frame is wrong —
  report it, don't pad the lesson.
- **Ladder honesty.** Rung prompts stay inside what each tool actually does (Aldi:GPT:
  chat only, cannot see files; M365 Copilot: acts in the open app; GitHub Copilot:
  agent with file access). Every rung-move is a prompt + check pair; the check catches
  that rung's most likely failure.

## Produce

1. `<course-dir>/lessons/<slug>.html` — all contract elements, in order. Machine-owned
   placeholders (`<title>`, `nav.lesson-nav`, `p.kicker`, `footer.lesson-nav`) must be
   well-formed and match `build_contents.py`'s regexes; write them once with sensible
   content and let the builder renumber. Shared stylesheet via
   `../assets/lesson.css`. Quiz + copy-button scripts inline, dependency-free —
   copy the patterns from an existing lesson, don't reinvent.
2. `course.json` — move the coordinate from `candidates` to `lessons` (slug, file,
   title, nav_label, grid_label, theme; `builds_on` only for edges the prose actually
   asserts). Preserve authored order within the theme.
3. Practice artefact additions if needed (starter state visible, solution present but
   not in the learner's face).

## Then verify (mechanical, every time)

- Run `build_contents.py --course-dir <course-dir>` if `index.html` exists — zero
  WARNINGs required.
- Grep the new page for every required element (mission, workbook, callout bad,
  "How to do it", 3 q-blocks, one h3 Rung per ladder rung above 1, "Try it for real",
  "Primary source", class="ask"). All present or you are not done.
- Every internal href resolves to a file on disk.
- No bare lesson-number references in author-owned prose — slug links only.

Report what was authored, what was verified, and any frame/contract friction you hit —
that friction is compound-stage input, not noise to swallow.
