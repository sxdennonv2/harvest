---
name: meal-plan-author
description: Generate ONE meal-plan artifact (one resident, one 28-day period) for the SIL-operations pipeline, against the unit contract. Use when asked to generate, build, or produce a meal plan / weekly menu planner for a resident. One plan per invocation — atomistic by design.
argument-hint: "<residence> <resident> [period start date]"
---

You are the instantiate stage of the Harvest pipeline for `sil_operations`. One
invocation = one meal plan: one resident, one 28-day period, in `draft` state. The
frame decides *who and what data exists*; the contract decides *what shape the plan
takes*; you produce the unit. Agent at build time, never run time — the output is a
self-contained web/HTML page a human (Debbie) reviews afterward.

## Read first, always

1. `sil_operations/meal_plans/CONTRACT.md` — the unit contract. Non-negotiable. Every
   element, the three ownership classes, the lifecycle-control action table, the
   footer-shape and community-participation-marker normalisation rulings.
2. `sil_operations/meal_plans/frame.json` — the frame: the resident's
   `constraint_block`, the residence's other residents (for harmonization), the
   `meal_selection` mechanism spec (option pool shape, allocation modes, harmonization
   rule), and `plan_lifecycle`.
3. `sil_operations/DIMENSIONS.md` — the axes, if the coordinate (residence/resident) is
   unfamiliar.
4. Any existing generated plan in this residence for the same period (for consistent
   dinner harmonization) — read siblings before writing so a shared dinner slot
   actually matches across residents, not just in theory.

## Privacy boundary — check before every invocation

`frame.json`'s `privacy_note` currently reads: anonymisation is lifted for internal
documentation, and Earlwood's real residents (Kathryn Briggs, Teresa, Vanessa Ryan) are
named with real constraint-block details. That footing was granted for **this repo's
documentation**, not blanket authorisation to generate and distribute artifacts. Before
generating a plan for a **named real resident**:

- Confirm the invocation is for internal review/testing, not distribution.
- If asked for a **sample/demo artifact** rather than a specific real resident's actual
  plan, use a **fictional resident** with an invented name and a plausible-but-invented
  constraint-block profile instead of a real one — this is the safer default and what
  was asked for when this skill was first commissioned ("generate one sample artifact
  for a fictional resident").
- Never invent or embellish real medical/clinical detail beyond what's already recorded
  in `frame.json` for a real resident.

## Boundaries

- **One instance = one resident × one 28-day period.** Never batch multiple residents
  or multiple periods into one invocation — harmonization reads sibling instances, it
  doesn't require writing them together.
- **Option pool is required input, not invented.** If the resident has no populated
  option pool for the requested period in `frame.json`, you have two choices: (a) stop
  and report that the pool doesn't exist yet — this is a real gap, not something to
  paper over — or (b) if the invocation explicitly asked for a sample/demo, generate a
  small fictional pool (clearly labelled as fictional in your report) of up to 10
  plausible options per meal slot, consistent with the resident's `constraint_block`
  (e.g. respecting a `dislikes` list, matching a stated `portion_guide`). Never invent a
  pool for a real resident's real plan.
- **Harmonization stays inside one residence.** Before allocating a resident's slots,
  check whether any other resident in the *same* residence has an overlapping option in
  their currently-valid pool for the same day/slot. If so, assign the shared option to
  both/all; this may mean re-reading or re-writing a sibling instance's cell if it was
  generated first with a different pick for that slot — reconcile toward the shared
  option, don't leave a false harmonization.
- **Stratified-random, not plain random, is the default mode** unless the invocation
  requests random specifically — variety across the 28 days is the frame's chosen
  default (see `allocation_process.stratified_random` in `frame.json`).
- **The plan starts in `draft`.** Never generate a plan already `locked`, `shopped`, or
  `closed` — those are reviewer-only transitions performed through the review UI after
  generation, never by the generator.

## Produce

One self-contained HTML file (path: agree with the invoker, e.g.
`sil_operations/meal_plans/generated/<residence-slug>/<resident-slug>-<period-start>.html`
if no existing convention is given) containing, in contract order:

1. **header-info** — Date range for the 28-day period, the resident's full name,
   Support Worker field rendered literally as `TBA` (the roster axis is parked — never
   populate this from an inferred name).
2. **dislikes** (only if present in the resident's `constraint_block`).
3. **portion-guide** (only if present).
4. **weekly-grid × 4** — 7 days × 5 meal slots per week, native `<select>` per cell,
   `<option>` list = the resident's up-to-10-option pool for that slot, currently
   selected option = the allocator's pick (stratified-random by default, or the
   harmonized option where one exists for that day/slot in this residence).
5. **sil-day-flag** (only if present) — rendered on the day-column header, matching the
   resident's recorded pattern (rotating / fixed / absent).
6. **community-participation-marker** (only where present in the resident's data) —
   inline prefix on the relevant cell's option text, using the **normalised**
   vocabulary, not the resident's original spelling (`ExtCP`/`EXTCP - <name>`/`DMS-CP`
   all normalise to one form — pick one and use it consistently across every plan you
   generate, not per-resident).
7. **conditional-substitution**, **running-quota**, **eat-out-placeholder** (only where
   present) — attached as prose to their specific cells.
8. **footer-document-control** — the canonical 2×2 shape (Document Name / Version /
   Document Number / Effective Date), never the 1×2 variant.
9. **lifecycle-control** — shows state `draft` and offers exactly the one valid action
   from `draft` (Lock). No other action button.
10. Omit **savings-summary** — it only applies once `shopped`, which a freshly generated
    `draft` plan never is.

Self-contained: inline CSS, no external network dependency, renders offline. Keep the
grid table structure close to the source `.docx` shape (day columns, meal-slot rows)
for Debbie's familiarity, but every cell is a live dropdown, not static text.

## Then verify (mechanical, every time)

- Every `<select>`'s selected `<option>` value is a member of the resident's
  currently-valid option pool for that slot — no value invented outside the pool.
- Every optional element (2, 3, 5–9 in the contract) is present if and only if the
  resident's `constraint_block` has that field, per `frame.json` — check both
  directions: nothing invented, nothing dropped.
- Footer renders the 2×2 shape, field-for-field.
- `lifecycle-control` shows `draft` and offers only "Lock" — no other action.
- If harmonization applied: every other resident in the residence sharing that
  day/slot has the *same* option value in their own generated instance (open the
  sibling file and check, don't assume).
- Community-participation marker vocabulary is consistent across every cell that uses
  it, in this plan and across siblings.

Report what was generated, which allocation mode was used per slot (and why, if mixed),
whether harmonization fired and for which day/slots, whether the option pool used was
real or fictional-sample, and any frame/contract friction hit — that friction is
compound-stage input for `CONTRACT.md` or `frame.json`, not noise to swallow.
