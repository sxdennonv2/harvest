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
| `dinner-rotation` | **conditional, not a fixed rule** (clarified 2026-07-05) | 28-recipe rotation, identical across all 3 Earlwood residents for the same week/day. Sharing one dinner across a house is only possible when residents' dietary requirements are compatible — where they clash (allergens, texture, medical diets), residents need individual dinners instead. Cadence is arbitrary/manual, not a fixed constraint | frame — evaluated per house, per period, driven by each resident's constraint-block profile, not assumed either way |
| `support-worker-roster` | **new axis, 2026-07-04; volatile (clarified 2026-07-05)** | support workers rostered on/off shift by day/week/month, and named staff can change at **short notice** | frame — the real scale bottleneck; a plan that bakes in a specific support worker's name can go stale fast, so the generator needs a near-real-time roster lookup, not a one-time import |
| `tier` | deployment | static (docx, current — **fully manual today**, hand-built by Debbie per resident per 28-day period) · live (generated per resident/period — the automation goal) | same frame + contract would serve both |

## How they compose

```
organisation → residence → resident         swappable tree, one home per residence
resident × weekly-grid                       the fixed 7×5 grid, one 28-day period per resident
resident × constraint-block                  the optional personalisation layer (0–7 blocks present)
residence × dinner-rotation                  conditional on dietary compatibility across the house's residents, not a fixed rule
residence × support-worker-roster            shift-based staffing that changes at short notice - the generator must read it live, not assume it
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

## Dinner-sharing is conditional, not universal (clarified 2026-07-05)

Earlier drafts read Earlwood's identical dinner-per-resident pattern as a general rule
("dinner is shared, batch-cooked"). Stuart corrected this: whether a house's residents
can share one dinner depends entirely on whether their **dietary requirements are
compatible**. Earlwood's 3 residents happen to be compatible enough to share. In a house
where residents have clashing needs — allergens, texture modification, a medical diet —
a shared dinner is impracticable, and each resident needs their own. So the generator
can't assume "one dinner per house" or "one dinner per resident" as a default; it has to
evaluate compatibility per house, per period, from each resident's constraint-block
profile (see `dislikes`, `portion_guide` in the schema above). Still open: how that
compatibility judgement is made today (Debbie, presumably by eye) and whether it can be
captured as structured data.

## Roster volatility (clarified 2026-07-05)

Named support-worker fields (`Created with Support Worker`, the named-CP-marker variant)
looked like static facts in the source docs, but the actual roster is **highly
changeable — staff can be swapped at short notice**. A generated plan that hard-codes a
support worker's name for a given day is liable to be wrong by the time it's used. This
pushes the automation goal toward the **live tier**, not the static one: whatever reads
the roster needs to do so close to when the plan is actually needed, not once at
generation time and then treat it as fixed. Still open: where that roster data lives.

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
