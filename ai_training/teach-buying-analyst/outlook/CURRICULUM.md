# Curriculum — Outlook (Buying Analyst, 1x → 10x)

Instance #3 of the pattern (Excel ✓, LWHC ✓, Outlook = this). Frame drafted 2026-07-04;
no lessons authored yet. Same two axes as Excel:

- **Rows = task themes**, elicited from Outlook's functional pillars and weighted by the
  NBUY survey's expressed needs.
- **Columns = the capability ladder** — the same task, climbing from hand-craft to GenAI.
  The ladder is invariant across the course family.

## How these themes were derived

Elicitation primitive (recorded in `../../DIMENSIONS.md`): *"What are the fundamental
pillars of functionality within Outlook?"* — then each pillar checked against the survey
(31 respondents, `../../data/ai_training_survey.csv`):

| Survey cluster | Mentions | Lands in |
|---|---|---|
| Reword / formalise / tighten / tone for leadership / proofread emails | ~14 (dominant) | → **communication pipeline** (`../../communication/`) |
| Summarise messages, threads, meeting notes | ~5 | → **communication pipeline** (Condense & summarise) |
| Find old emails, search archives | ~2 | Find & retrieve |
| Meeting notes → minutes / actions | ~2 | Schedule & coordinate (mechanics) · communication (writing) |
| General productivity / process prompts | diffuse | Triage & organise · Automate the repetitive |

Theme order follows the working day: triage what arrived → find what you need → write the
answer → coordinate the meeting → automate what repeats. The grid is the map, not a
promise to build every cell.

**The pipeline boundary (Stuart, 2026-07-04):** most of the survey's email demand —
reword, reframe, revise for grammar, conciseness, tone, clarity — is *communication
craft*, not Outlook functionality. By decision, this pipeline is strictly **application
functionality**; writing craft moved to the **communication pipeline**
(`../../communication/`), taking three candidates with it (one-ask email, reword for
tone & audience, bullets to prose) before any lesson was authored. *Write & respond*
here is scoped to mechanics: threading, attachments, formatting, using Copilot's
draft-from-thread. The boundary rule: **if the lesson would survive the app being
swapped, it belongs in communication.**

## Lessons so far (by theme)

<!-- BEGIN:auto:lessons -->
### Triage & organise

- [0001 — Folders, categories & flags: one home per mail](lessons/folders-categories-and-flags.html)

### Find & retrieve

- [0002 — Search operators: describe the mail, don't scroll](lessons/search-operators.html)

### Write & respond

- [0003 — Threading hygiene: reply, reply-all, forward](lessons/threading-hygiene-reply-reply-all-forward.html)

### Schedule & coordinate

- [0004 — Invites that get accepted: the agenda is the meeting](lessons/invites-that-get-accepted.html)

### Automate the repetitive

- [0005 — Quick Steps: one click, three actions](lessons/quick-steps-one-click-three-actions.html)
<!-- END:auto:lessons -->

## The grid

<!-- BEGIN:auto:grid -->
| Theme ↓ / Rung → | 1 · Manual craft (do it well by hand) | 2 · Aldi:GPT (chat, no tool use) | 3 · M365 Copilot (acts in Outlook) | 4 · GitHub Copilot (builds the artefact) |
|---|---|---|---|---|
| **Triage & organise** | ✅ [0001 Folders, categories & flags](lessons/folders-categories-and-flags.html); folders vs categories vs flags; rules on arrival | Suggest a folder-and-rule scheme for the mail you describe | "Summarise this thread — what's asked of me and by when?" | Script the folder + rule deployment from scratch |
| **Find & retrieve** | ✅ [0002 Search operators](lessons/search-operators.html); search operators; Search Folders | Write the search-operator query for what you need | "Find the thread where the supplier confirmed the price change" | Build a mailbox report (senders, volumes, ageing) from an export |
| **Write & respond** | ✅ [0003 Threading hygiene](lessons/threading-hygiene-reply-reply-all-forward.html); mechanics only — writing craft lives in the communication pipeline | "What is this thread asking of me, and who owes the reply?" | Draft the reply from the whole thread's context | Generate a reply-template library from your recurring scenarios |
| **Schedule & coordinate** | ✅ [0004 Invites that get accepted](lessons/invites-that-get-accepted.html); invites, Scheduling Assistant, notes-to-actions | Draft the agenda and the invite text | Recap the meeting and draft the follow-up actions | Build the recurring meeting pack (agenda, minutes, invite) from scratch |
| **Automate the repetitive** | ✅ [0005 Quick Steps](lessons/quick-steps-one-click-three-actions.html); signatures, Quick Parts, Quick Steps, out-of-office | Turn a repeated email into reusable template text | Draft the out-of-office and standing replies in context | Script signature + template deployment from scratch |
<!-- END:auto:grid -->

## Practice artefact (decision pending first lesson)

Excel's shared workbook becomes, for Outlook, a **practice pack**: a folder of realistic
sample emails (supplier price change, promo query, internal escalation — fictional
suppliers reused from the Excel course data) the learner drags into a practice folder,
plus a scenario sheet. Rung 4 builds these artefacts from scratch. To be specified
against CONTRACT.md's `practice-pointer` element when the first lesson is authored.

## Notes for the build

- `build_contents.py` is not runnable here until `index.html` and a first lesson exist;
  the auto-region markers above are already in place for when it is.
- Ladder rung 3 wording: Copilot in Outlook drafts/summarises in context but cannot set
  rules or create folders — rung 3 prompts stay inside what the tool actually does.
- This frame is data. Reorder themes or candidates here (and in `course.json`), and the
  numbering, nav and grid follow — same shuffle-and-renumber contract as Excel.
