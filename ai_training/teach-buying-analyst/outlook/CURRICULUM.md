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

| Survey cluster | Mentions | Lands in theme |
|---|---|---|
| Reword / formalise / tighten / tone for leadership / proofread emails | ~14 (dominant) | Write & respond |
| Summarise messages, threads, meeting notes | ~4 | Write & respond · Schedule & coordinate |
| Find old emails, search archives | ~2 | Find & retrieve |
| Meeting notes → minutes / actions | ~2 | Schedule & coordinate |
| General productivity / process prompts | diffuse | Triage & organise · Automate the repetitive |

Theme order follows the working day: triage what arrived → find what you need → write the
answer → coordinate the meeting → automate what repeats. **Write & respond carries the
survey's demand and gets the most lessons**; Triage and Automate are pillar-complete but
demand-light — the grid is the map, not a promise to build every cell.

## Lessons so far (by theme)

<!-- BEGIN:auto:lessons -->
_None authored yet. 15 candidates are enumerated in `course.json` under `candidates`,
each tagged with its survey signal. First up (highest demand): **Reword for tone &
audience** in Write & respond._
<!-- END:auto:lessons -->

## The grid

<!-- BEGIN:auto:grid -->
| Theme ↓ / Rung → | 1 · Manual craft (do it well by hand) | 2 · Aldi:GPT (chat, no tool use) | 3 · M365 Copilot (acts in Outlook) | 4 · GitHub Copilot (builds the artefact) |
|---|---|---|---|---|
| **Triage & organise** | 3 candidates | Suggest a folder-and-rule scheme for the mail you describe | "Summarise this thread — what's asked of me and by when?" | Script the folder + rule deployment from scratch |
| **Find & retrieve** | 2 candidates | Write the search-operator query for what you need | "Find the thread where the supplier confirmed the price change" | Build a mailbox report (senders, volumes, ageing) from an export |
| **Write & respond** | 4 candidates ← survey demand | Reword this draft — tone, length, audience | Draft the reply from the whole thread's context | Generate a reply-template library from your recurring scenarios |
| **Schedule & coordinate** | 3 candidates | Draft the agenda and the invite text | Recap the meeting and draft the follow-up actions | Build the recurring meeting pack (agenda, minutes, invite) from scratch |
| **Automate the repetitive** | 3 candidates | Turn a repeated email into reusable template text | Draft the out-of-office and standing replies in context | Script signature + template deployment from scratch |
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
