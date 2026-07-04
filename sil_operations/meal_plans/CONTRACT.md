# Unit Contract — one meal plan

The unit of this pipeline is **one meal plan**: one resident's 28-day Weekly Menu
Planner artifact, editable through a defined lifecycle. This contract defines what
every meal plan must contain and how it may move between states. It is consumed by:

- the **generator** (not yet built) at instantiate time — populates a fresh `draft`
  from a resident's currently-valid option pool;
- the **review UI** (web/HTML, confirmed 2026-07-05) at review time — every dropdown
  and lifecycle control it renders must satisfy this contract;
- the **verifier** (not yet built) — the checklist at the end is its spec.

Reverse-engineered from 3 real Weekly Menu Planner `.docx` files (residence: Earlwood,
provider: Danny Met Sally / DMS, analysed 2026-07-04), then extended by Stuart's design
decisions for the automated mechanism (2026-07-05). See `frame.json` for the frame data
this contract renders, and `../DIMENSIONS.md` for the axes.

## Parameters

A meal plan is rendered from a frame coordinate plus these parameters. Elements are
invariant; **bindings** (which options are available, which constraint blocks appear)
vary with the resident.

| Parameter | Kathryn Briggs (reference) | Varies with |
|---|---|---|
| `organisation` | Danny Met Sally (DMS) | fixed today (one org) |
| `residence` | Earlwood | residence |
| `resident` | Kathryn Briggs | resident |
| `option_pool` | up to 10 options × 5 slots, current quarter's version | resident, and time (quarterly refresh + mid-quarter edits) |
| `constraint_block` | dislikes, portion-guide, rotating SIL-day, `ExtCP` marker, conditional substitution, eat-out placeholder present; running quota absent | resident (0–7 of the 7 block types present; see schema below) |
| `period` | one 28-day cycle (4 weeks) | instance — one plan per resident per period |

The weekly grid (7 days × 5 meal slots) and the four-state lifecycle are invariant
across every resident and residence — swapping the resident swaps the bindings, not
the shape.

## Ownership

Three classes of element, not two — this pipeline has an automated allocator sitting
between the data owner and the reviewer:

- **data-owned** (Debbie) — the option pool itself: built quarterly, time-boxed
  (`start_date`/`end_date`), editable mid-quarter with immediate effect. The contract
  consumes whichever pool version is currently valid for the period being planned; it
  does not define how the pool is built.
- **algorithm-owned** (the allocator) — every grid cell's *initial* dropdown value:
  random, stratified-random (variety across the 28 days), or harmonized (shared across
  a residence when residents' pools overlap for that day/slot).
- **reviewer-owned** (Debbie) — any dropdown she changes during review, and every
  lifecycle transition (`locked`, `shopped`, `closed`, and the two reset paths). Her
  edits are never overridden by the algorithm; there is no re-allocation after a manual
  change.

## Elements

In document order. Every element is required unless marked optional.

| # | Element | Owner | Reference rendering |
|---|---|---|---|
| 1 | `header-info` | machine | Date range · Participant's Name · Created with Support Worker (`TBA` — parked) |
| 2 | `dislikes` | data *(optional)* | free-text food list, one paragraph before the grid |
| 3 | `portion-guide` | data *(optional)* | plate-proportion rules, caps, medical directives; author role stated (Dietitian / Doctor & Dietitian) |
| 4 | `weekly-grid` ×4 | algorithm → reviewer | 7 days × 5 meal slots, one dropdown per cell |
| 5 | `sil-day-flag` | data *(optional, per day)* | marker on the day-column header, not a cell |
| 6 | `community-participation-marker` | data *(optional, per cell)* | inline prefix within a cell's dropdown option, normalised vocabulary (see below) |
| 7 | `conditional-substitution` | data *(optional, per cell)* | prose rule attached to a cell's option ("if X unavailable, substitute Y") |
| 8 | `running-quota` | data *(optional, per cell)* | prose rule tracking a daily/weekly cap, attached to a cell's option |
| 9 | `eat-out-placeholder` | data *(optional, per cell)* | option value delegating the meal to an outing/support worker |
| 10 | `footer-document-control` | machine | Document Name / Version / Document Number / Effective Date (target shape — see Template ruling) |
| 11 | `lifecycle-control` | machine (review UI only) | current state (`draft`/`locked`/`shopped`/`closed`) + the one or two valid transition actions from that state |
| 12 | `savings-summary` *(optional, once shopped)* | machine | harmonized-slot count, residents covered per harmonized slot, individual meals avoided |

### Element specifications

**header-info.** Three fields, machine-populated per instance: the period's date range
(`Mon DD/MM/YY - Sun DD/MM/YY`), the resident's full name, and the support-worker field.
The support-worker field renders the literal placeholder `TBA` — this axis is parked
(see `support_worker_roster` in `frame.json`); do not populate it from any inferred
source until the roster question is revisited.

**dislikes / portion-guide.** Optional per resident, free-text, sourced from the
resident's `constraint_block`. Present or absent exactly as recorded for that resident
— a generator must not synthesise either block when the source data has neither.

**weekly-grid.** The one invariant element. Every cell is a **dropdown** populated with
the resident's currently-valid option pool for that meal slot (up to 10 options). The
cell's initial value is set by the allocator (see Ownership); Debbie may change any
cell independently — changing one cell never changes another, even within a harmonized
slot. A generator must resolve "currently-valid pool" from the option pool's
`start_date`/`end_date`, not assume the most-recently-edited version is the only one.

**sil-day-flag.** A per-day marker, optional and resident-specific: rotating,
fixed-set, or absent entirely (see `constraint_block_schema.sil_day_flag` in
`frame.json` for the three observed patterns). Rendered on the day-column header, never
as a separate grid row.

**community-participation-marker.** Optional per cell, prefixed to that cell's option
text. **Normalise to one vocabulary** in the generator — the three source spellings
(`ExtCP`, `EXTCP - <name>`, `DMS-CP`) are drift on top of one standard template, not
three real conventions (confirmed 2026-07-04). Do not preserve resident-specific
spelling as if it were meaningful.

**conditional-substitution / running-quota / eat-out-placeholder.** All three are
prose attached to specific cells, sourced from the resident's `constraint_block`.
Optional and resident-specific; a generator populates them from data, never invents
one to fill a perceived gap.

**footer-document-control.** **Target one canonical shape** (2 rows × 2 cols: Document
Name / Version / Document Number / Effective Date) — the observed 1×2 variant (Author /
Date of Review / Page) is per-resident drift, not a second real template lineage
(confirmed 2026-07-04). A generator renders the 2×2 shape for every resident; existing
1×2 instances are drift to reconcile, not preserve.

**lifecycle-control.** Rendered only in the interactive review UI, never in a final
printed/exported artifact. Shows the plan's current state and exactly the actions valid
from it:

| Current state | Valid actions |
|---|---|
| `draft` | Lock |
| `locked` | Unlock (→ `draft`) · Generate shopping list (→ `shopped`) |
| `shopped` | Reset (→ `draft`, clears the shopping list) · Close (→ `closed`) |
| `closed` | none — terminal |

A control offering an action not valid from the current state is a contract violation.

**savings-summary.** Optional, appears once a plan reaches `shopped` (harmonization has
run by then). Reports the count of harmonized day/slot combinations and how many
residents each covered — the measured value of automation, not an assumed one. Sketch
only in `frame.json`; no real calculation built yet, so this element may be omitted
entirely until that calculation exists.

## Constraint-block schema

See `constraint_block_schema` in `frame.json` for the authoritative shape of the 7
optional block types (`dislikes`, `portion_guide`, `sil_day_flag`,
`community_participation_marker`, `conditional_substitution`, `running_quota`,
`eat_out_placeholder`). No block is guaranteed present for any resident — a generator
must treat every one as optional, never assumed.

## Technical constraints

- One meal plan = one resident × one 28-day period. A residence with N residents
  produces N independent plan instances per period, linked only by the (optional)
  harmonization pass across their dinner (or any) slot.
- The review UI is a **web/HTML** page (confirmed 2026-07-05); the grid is rendered
  with native `<select>` elements or equivalent, one per cell, never free text.
- Every dropdown's option list is drawn from that resident's **currently-valid** option
  pool version — a pool is time-boxed data (`start_date`, `end_date`, `options[]`), not
  a single static list.
- Harmonization is scoped to one residence at a time; it never reaches across
  residences.
- Lifecycle state travels with the instance (not the resident or the period in the
  abstract) — a resident's next period starts a fresh instance in `draft`.

## Relationship to the frame

The frame (`frame.json`) supplies the coordinate; this contract supplies the shape.

- `residence` → `resident` → the coordinate identifying which option pool and
  constraint block populate the instance.
- `meal_selection.option_pool` → the per-cell dropdown's option list, resolved to the
  version valid for the period's dates.
- `meal_selection.allocation_process` → how each cell's *initial* value is set
  (random / stratified-random / harmonization) before Debbie's review.
- `meal_selection.plan_lifecycle` → the state machine `lifecycle-control` renders and
  enforces.
- `constraint_block_schema` → the optional per-resident blocks (elements 2, 3, 5–9).
- `template_ruling` / `footer_template_variation` → the target shape for
  `footer-document-control`.

## Degrees of freedom

The generator/allocator may, above the floor: choose random or stratified-random
allocation per cell (both are contract-compliant defaults); run harmonization across a
residence's residents; omit `savings-summary` until its calculation is built. It may
not: pre-fill a dropdown with an option outside the resident's currently-valid pool,
run harmonization across residences, render a lifecycle action not valid from the
current state, or synthesise an optional constraint block the resident's data doesn't
have.

The reviewer (Debbie) may, at any point in `draft` or `locked`: change any cell
independently, as much or as little as she wants, with no cascading effect on other
cells. She may not (per the contract, not a UI restriction): edit a `shopped` or
`closed` plan directly — `shopped` must be reset to `draft` first; `closed` cannot be
reopened at all.

## Verify checklist (future `meal-plan-verify` spec)

Mechanical (no judgement):
- [ ] All required elements present, in contract order; machine-owned fields intact
      (`header-info`, `footer-document-control` in target 2×2 shape,
      `lifecycle-control`).
- [ ] Every grid cell's selected value is a member of that resident's currently-valid
      option pool for that slot.
- [ ] Optional blocks (2, 3, 5–9) render if and only if the resident's
      `constraint_block` has that field present.
- [ ] `community-participation-marker` uses the normalised vocabulary, not a
      resident-specific spelling.
- [ ] `lifecycle-control` offers only the actions valid from the plan's current state
      (see table above); no plan in `closed` accepts any further edit.
- [ ] Harmonized cells: every resident sharing a harmonized day/slot has the identical
      option value, unless overridden individually by Debbie.

Judged (agent):
- [ ] `savings-summary` (when present) accurately reflects the plan's harmonized slots.
- [ ] The plan reads as something Debbie would recognise and accept without
      restructuring — variety across the period, no obviously wrong pairing of
      constraint blocks (e.g. an `eat-out-placeholder` cell also carrying a
      `running-quota` note that contradicts it).

## Known open items (not yet blocking, per `frame.json` `open_questions`)

1. How many residents typically live in one SIL home (Earlwood = 3; unconfirmed as
   typical) — affects how much harmonization opportunity a generator should expect per
   residence.
2. Full list of residences/resident counts nationwide — deferred, sticking with
   Earlwood + 4 placeholders (Berala, Burwood, Blacktown, Mascot) for now.
3. Support-worker roster data source — parked; `header-info`'s support-worker field
   stays `TBA` until revisited.

No open questions remain on the meal-selection mechanism or the plan lifecycle
themselves — both are fully specified as of 2026-07-05.
