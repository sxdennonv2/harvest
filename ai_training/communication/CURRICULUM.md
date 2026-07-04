# Curriculum — Communication (1x → 10x)

**The second pipeline.** Split out of the AI-training work by decision (Stuart,
2026-07-04): `teach-buying-analyst/` is strictly **application functionality**; this
pipeline owns **writing and communication craft** — rewriting, reframing, revising for
grammar, conciseness, tone and clarity. The boundary rule: *if the lesson would survive
the app being swapped, it belongs here.*

Frame drafted 2026-07-04; no lessons authored yet.

- **Rows = communication themes**, elicited from the pillars of workplace written
  communication and weighted by the NBUY survey.
- **Columns = the same capability ladder** as the functionality pipeline — the ladder is
  the org's GenAI adoption model and is now invariant **across pipelines**, not just
  courses. (Rung 3 binds to whichever app hosts the writing.)
- **A third axis this pipeline adds: `context`** — email · document · slides · chat.
  Communication lessons bind to contexts the way functionality lessons bind to one app.
  Email is the demand centre today; the same lesson retargets to other contexts later.

## How these themes were derived

Elicitation primitive: *"What are the fundamental pillars of effective workplace written
communication?"* — checked against the survey (31 respondents,
`../data/ai_training_survey.csv`):

| Survey cluster | Mentions | Lands in theme |
|---|---|---|
| Reword / rephrase / formalise / professional standard | ~14 (dominant) | Tone & audience |
| Tighten, clarity, conciseness, remove ambiguity | ~4 | Clarity & conciseness |
| Spell check, proofread, grammar | ~4 | Correctness |
| Summarise messages, threads, meeting notes | ~5 | Condense & summarise |
| Formalise bullets/data into prose; submissions for GDM | ~3 | Structure & framing |

Three candidates were **moved here from the Outlook frame** the day it was drafted
(one-ask email, reword for tone & audience, bullets to prose) — the split caught them
before a single lesson was authored, so the move cost nothing.

## Lessons so far (by theme)

<!-- BEGIN:auto:lessons -->
### Clarity & conciseness

- [0001 — Tighten: cut the flab, keep the message](lessons/tighten-cut-the-flab-keep-the-message.html)

### Tone & audience

- [0002 — Reword for tone & audience](lessons/reword-for-tone-and-audience.html)
- [0003 — Writing up: the senior-leadership register](lessons/writing-up-the-senior-leadership-register.html)

### Condense & summarise

- [0004 — Summarise a thread without losing the ask](lessons/summarise-a-thread-without-losing-the-ask.html)
<!-- END:auto:lessons -->

## The grid

<!-- BEGIN:auto:grid -->
| Theme ↓ / Rung → | 1 · Manual craft (do it well by hand) | 2 · Aldi:GPT (chat, no tool use) | 3 · M365 Copilot (acts in the app you write in) | 4 · GitHub Copilot (builds the artefact) |
|---|---|---|---|---|
| **Clarity & conciseness** | ✅ [0001 Tighten](lessons/tighten-cut-the-flab-keep-the-message.html); tighten; remove ambiguity | Tighten this draft — same message, half the words | Rewrite this selection in place: clearer, shorter, same meaning | Batch-rewrite a library of standard texts to the new standard |
| **Tone & audience** | ✅ [0002 Reword for tone & audience](lessons/reword-for-tone-and-audience.html); ✅ [0003 Senior-leadership register](lessons/writing-up-the-senior-leadership-register.html); the survey's dominant cluster — most lessons live here | Reword for the reader — formal, firm, or friendly | Adjust the tone of this draft for its audience, in place | Generate audience-tuned variants of a template set |
| **Structure & framing** | lead with the ask; bullets to prose and back | Restructure this: lead with the ask, turn bullets into prose | Draft the message from these bullet points, in the app | Build skeleton templates for your recurring message types |
| **Correctness** | grammar, spelling, punctuation, house style | Proof this — grammar, spelling, punctuation, house style | Check and correct the draft in place | Build a house-style checklist and apply it across a document set |
| **Condense & summarise** | ✅ [0004 Summarise a thread](lessons/summarise-a-thread-without-losing-the-ask.html); threads, meeting notes, reports — keep every ask and owner | Summarise this thread or these notes — keep every ask and owner | Summarise the thread and draft the minutes, in the app | Build the meeting-pack generator: notes in, minutes + actions out |
<!-- END:auto:grid -->

## Practice artefact (decision pending first lesson)

A **before/after pack**: deliberately flabby drafts (a rambling supplier email, a
buried-ask escalation, wall-of-text meeting notes — fictional suppliers shared with the
functionality courses) for the learner to revise by hand at rung 1, then hand up the
ladder. The reconciliation check that survives every rung: *the revision keeps every
fact, every ask, and every owner from the original.*

## Contract

Reuses the unit contract at `../teach-buying-analyst/CONTRACT.md` — the elements are
pipeline-agnostic (that was the point of elements vs bindings). Two binding changes, to
be formalised when the first lesson is authored: `practice-pointer` targets the
before/after pack, and `persona-relevance` widens beyond the buying analyst (the survey
demand here comes at least as strongly from assistants, admins and managers).

## Notes for the build

- `build_contents.py` runs here unchanged once `index.html` and a first lesson exist —
  the frame schema is identical; auto-region markers are already in place.
- Rung 3 wording stays inside what Copilot actually does in each host app (rewrite
  selection in Word, draft from thread in Outlook, summarise in place).
