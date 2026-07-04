# Dimensions of the SIL-operations pipeline

The axes of the SIL (Supported Independent Living) meal-plan frame, named so the whole
space can be seen before the detail is infilled. This is Harvest instance #4 (FRAME-LEDGER
row 4) — the first non-office-app domain, promoted from real source artifacts rather than
elicited blind: three residents' actual Weekly Menu Planner `.docx` files (residence:
Earlwood), analysed 2026-07-04. ✅ = populated from source; ⬜ = placeholder, awaiting data.

## The axes

| Dimension | Kind | Values today | Owned by |
|---|---|---|---|
| `organisation` | binding parameter | **Danny Met Sally (DMS)** ✅ — confirmed 2026-07-04; explains the docx creator field `dannymetsally` seen on 2 of 3 source files. Nationwide, ~20–30 homes; sticking with the residences already known rather than chasing the full list | frame — the whole tree sits under one org today |
| `residence` | swappable tree root | Earlwood ✅ (3 residents, source data) · Berala ⬜ · Burwood ⬜ · Blacktown ⬜ · Mascot ⬜ (placeholder, deferred by Stuart's word — not chasing the rest for now) | frame — one SIL home each |
| `resident` | tree leaf, nested in residence | 3 populated (Earlwood: Kathryn Briggs, Teresa, Vanessa Ryan — real names, privacy anonymisation lifted for this internal repo 2026-07-04) + 2 placeholder per unbuilt residence | frame — one participant, one personalisation profile |
| `weekly-grid` | **invariant crosscutting contract** | 7 days × 5 meal slots (Breakfast 8am, Morning Tea 10:30am, Lunch 12:30pm, Afternoon Tea 3:30pm, Dinner 6pm), one 28-day period per resident (confirmed the standard unit) | frame — stable across all 3 source residents; treat as the fixed shape, like the ladder in the AI-training frame |
| `constraint-block` | crosscutting, **optional per resident** | 7 block types observed: dislikes list, portion-guide/clinical paragraph, SIL-day flag, community-participation marker, conditional substitution, running quota, eat-out placeholder | frame — presence/absence and wording vary per resident; none is guaranteed present |
| `dinner-rotation` | **conditional, not a fixed rule** (clarified 2026-07-05) | 28-recipe rotation, identical across all 3 Earlwood residents for the same week/day. Sharing one dinner across a house is only possible when residents' dietary requirements are compatible — where they clash (allergens, texture, medical diets), residents need individual dinners instead. Cadence is arbitrary/manual, not a fixed constraint | frame — now resolved mechanically by `meal-option-pool` × `allocation-process` below, rather than assumed |
| `meal-option-pool` | resident × time-boxed data | up to 10 named meal options per resident, per meal slot. **Built by Debbie, quarterly** (4x/year); each pool version has a start/end date it's valid between; options can be added/removed/altered mid-quarter, taking effect immediately until changed again | frame — a pool is a sequence of time-boxed versions per resident, not one static list |
| `allocation-process` | crosscutting mechanism | three modes, confirmed 2026-07-05: **random** (uniform pick from the resident's currently-valid pool), **stratified random** (stratifies by **variety across the 28-day period** — spread option usage evenly rather than clustering repeats), **manual override** (Debbie can override any automated pick). Plus **harmonization**: detect an option shared across multiple residents' pools in the same house/day/slot and assign it to all of them | frame — the concrete answer to "can this house share a dinner", replacing manual judgement with overlap-detection, with an escape hatch for Debbie's judgement |
| `review-interface` | web/HTML UI, confirmed 2026-07-05 | every resident × meal-slot × day cell is a **dropdown** of that resident's currently-valid option pool, pre-filled by the allocation algorithm's output. Debbie can change **as much or as little as she wants**, cell by cell, independently — no automatic re-harmonization or cascading | frame — the artifact's core interaction shape, fully specified |
| `plan-lifecycle` | **state machine, 2026-07-05** | `draft` (editable) → `locked` (Debbie's explicit action; **hard gate** — cannot shop an unlocked plan; editability after locking unconfirmed) → `shopping_list_generated` (confirmed terminal — cannot be changed further, ever) | frame — one-directional as far as confirmed; open question is whether `locked` alone is already immutable |
| `support-worker-roster` | **parked, 2026-07-05** | single fixed value `TBA` — kept as a dimension so the shape isn't lost, but not pursued as live/volatile data right now | frame — revisit only if worth pursuing later |
| `tier` | deployment | static (docx, current — **fully manual today**, hand-built by Debbie per resident per 28-day period) · live (generated per resident/period — the automation goal) | same frame + contract would serve both |

## How they compose

```
organisation → residence → resident         swappable tree, one home per residence
resident × weekly-grid                       the fixed 7×5 grid, one 28-day period per resident
resident × constraint-block                  the optional personalisation layer (0–7 blocks present)
resident × meal-option-pool                  up to 10 candidate options per resident, per meal slot
option-pool × allocation-process             random pick, or harmonized pick when pools overlap across a house
residence × support-worker-roster            parked - single TBA value, not pursued right now
everything × tier                            static docx today (fully manual), live generation is the goal
```

Not a full cartesian product: `constraint-block` values are **optional and free-text today**,
not a controlled vocabulary — e.g. the community-participation marker alone has three
observed spellings (`ExtCP`, `EXTCP - <name>`, `DMS-CP`) across just 3 residents. A
generator built directly on this frame would need to decide whether to normalise that
vocabulary or preserve resident-specific convention.

## One standard template, not two lineages (resolved 2026-07-04)

The footer/document-control table differs in shape across the 3 source residents:
- **2×2 shape** (Document Name / Version / Document Number / Effective Date) — Kathryn Briggs, Vanessa Ryan
- **1×2 shape** (Document Name / Date Developed / Version, Author / Date of Review / Page) — Teresa

Stuart confirmed the template is standard, company-wide — so this is **not** two real
template versions. It's per-resident variation or drift on top of one canonical template.
The generator should target one footer shape; the 1×2 variant is something to reconcile,
not preserve. Same ruling likely applies to the community-participation marker's three
spellings (`ExtCP` / `EXTCP - <name>` / `DMS-CP`) — treat as drift to normalise, backed by
the support-worker roster, not three real conventions.

## Dinner-sharing: from judgement call to mechanism (2026-07-05)

Earlier drafts read Earlwood's identical dinner-per-resident pattern as a general rule
("dinner is shared, batch-cooked"). Stuart first corrected this to "it's conditional on
dietary compatibility, evaluated per house" — then supplied the concrete mechanism that
makes that evaluation automatic rather than a manual judgement call:

1. **Meal-option pool** — each resident gets up to 10 named options per meal slot,
   already assumed compatible with their own constraint-block (dislikes, portion-guide,
   etc.). **Confirmed 2026-07-05: Debbie builds these, quarterly** (4x/year). Each pool
   version applies between a start date and an end date — so this is time-boxed data,
   not one static list per resident forever. Options can be changed mid-quarter (added,
   removed, altered); a change takes effect **immediately** and stays in effect until
   changed again — the quarterly cadence is the baseline refresh rhythm, the pool itself
   is a living list within its validity window.
2. **Allocation** — three modes, confirmed 2026-07-05: **random** (uniform pick from the
   resident's currently-valid pool version), **stratified random** — stratification
   variable **chosen: variety across the 28-day period**. Rather than sampling each day
   independently (which can by chance cluster repeats of the same option), work through
   the pool's options in shuffled rounds so each gets used a roughly even number of
   times across the period — not zero repetition (a 10-option pool over 28 days still
   repeats each option ~2-3 times), just no clustering. And **manual override** (Debbie
   can override any automated pick for any resident/day/slot — the automation is a
   default, not a constraint on her judgement).
3. **Harmonization** — before allocating individually, check whether an option appears
   in more than one resident's currently-valid pool for the same house, day, and slot.
   If it does, assign that same option to every resident who has it in their pool — one
   cooked meal serves several residents, discovered by overlap rather than assumed as a
   rule. Scoped to one residence at a time; never crosses houses. Residents without a
   shared option fall back to random or stratified-random selection from their own pool.
4. **Savings tracking** — count how many day/slot combinations got harmonized and how
   many residents each one covered, so the time/cost benefit is measured, not assumed.

This replaces "does Debbie judge this house compatible?" with "do these residents'
option pools happen to overlap?" — and the override mode means her judgement is never
locked out even if the mechanism gets something wrong.

## Review interface: the override made concrete (2026-07-05, fully resolved)

The abstract "Debbie can override any automated pick" now has a shape: **every cell in
the resident × meal-slot × day grid is a dropdown**, populated with that resident's
currently-valid option pool (up to 10 named options). The algorithm's output (random,
stratified-random, or harmonization) pre-fills each dropdown's initial value; Debbie
reviews the whole plan and changes any cell's selection directly, cell by cell, as she
goes. This is the concrete review workflow, not just a capability statement.

Both implications from the previous draft are now resolved:
- **Format**: a **web/HTML UI** hosts the interactive review step. (The final,
  signed-off artifact may still render differently once locked — that's a separate
  question from the review surface itself, and not raised as blocking.)
- **Override × harmonization interaction**: there is **no special interaction** — Debbie
  can change as much or as little as she wants, cell by cell, independently. No
  automatic re-harmonization or cascading logic runs when she edits a cell. Whatever
  state she leaves the grid in in the `draft` state is what gets carried forward when
  she locks it.

## Plan lifecycle: draft → locked → shopping list (2026-07-05)

A new state machine governs how long a plan stays editable:

1. **`draft`** — the algorithm has pre-filled every cell; Debbie is reviewing and may
   change any cell, independently, as described above.
2. **`locked`** — Debbie's explicit action (a "Locked" button), not automatic or
   time-based. Her edited state becomes final for this plan at this point. **Confirmed
   2026-07-05 as a hard gate, not just a path**: a plan cannot be used to generate a
   shopping list until it is locked — there's no way to shop an unlocked plan.
   **Open question**: can a locked plan itself be unlocked and edited again before a
   shopping list is generated from it, or does locking already make it immutable? Not
   yet confirmed either way.
3. **`shopping_list_generated`** — confirmed **terminal and immutable**: once a plan has
   been used to create a shopping list, it cannot be changed any further, under any
   circumstances.

Both gates are now confirmed as hard rules, not descriptions of a typical path: (1) no
shopping list without locking first; (2) no changes at all after shopping. The one
remaining gap in the lifecycle is whether `locked` is itself reversible before a
shopping list gets made.

Transition order is one-directional as far as confirmed: `draft → locked →
shopping_list_generated`, with no reopening after shopping-list generation.

## Roster: parked (2026-07-05)

Named support-worker fields (`Created with Support Worker`, the named-CP-marker variant)
looked like static facts in the source docs; then turned out to be **highly volatile** —
staff can be swapped at short notice. Rather than solve live-roster integration now,
Stuart chose to **park this axis**: it stays in the frame as a dimension (so the shape
isn't lost) but is fixed to a single placeholder value, `TBA`, until it's worth
revisiting. The automation value for now comes from the meal-option-pool/harmonization
mechanism above, not roster-awareness.

## Privacy note

This documentation is internal (Stuart, 2026-07-04) — the anonymisation used in the first
draft has been lifted, and residents' real names are now used (Kathryn Briggs, Teresa,
Vanessa Ryan). Re-check this footing before this repo is ever made external or the
generator handles a wider resident set with more sensitive clinical detail.

## Generative prompts (dimension elicitation primitives)

- residence axis: promoted from source docs (Earlwood), not elicited — confirm remaining
  4 residences' resident counts and personalisation profiles with Debbie before filling in.
- constraint-block axis: *"what optional information does this resident's support team
  need on the page that a generic weekly grid wouldn't capture?"*

## Progress map (standard process)

The live progress map is **`sil_operations/dimension-map.html`** — mirrors the standard
process in `ai_training/DIMENSIONS.md`: residence × resident map, the weekly-grid
contract, the constraint-block presence matrix, and the standing open-questions section.
**The file in this repo is the source of truth; the artifact is its deployment.**

Standing artifact URL (always redeploy to this URL, never mint a new one):
https://claude.ai/code/artifact/82db3912-99f7-499e-bdc2-7c9c1aa17c5b

Update at every change to `frame.json` or every milestone (Debbie interview, contract
draft, first sample artifact, privacy footing resolved): refresh the stats bar, the
residence/resident chips, the constraint-block matrix, and the open-questions list, then
redeploy to the URL above (favicon 🥗, same URL every time).

## Beyond this pipeline

This is one instance of the Harvest shape (enumeration-expanded: organisation × residence ×
resident is a finite, growable list). See `/Users/stuartdennon/Documents/studio/FRAME-LEDGER.md`
row 4 for the sibling instances planned on the same frame (Monthly Resident Report, Shift
Duties Checklist) and the cross-portfolio pattern this shares with `ai_training/DIMENSIONS.md`.
