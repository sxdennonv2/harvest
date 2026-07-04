# Dimensions of the SIL-operations pipeline

The axes of the SIL (Supported Independent Living) meal-plan frame, named so the whole
space can be seen before the detail is infilled. This is Harvest instance #4 (FRAME-LEDGER
row 4) — the first non-office-app domain, promoted from real source artifacts rather than
elicited blind: three residents' actual Weekly Menu Planner `.docx` files (residence:
Earlwood), analysed 2026-07-04. ✅ = populated from source; ⬜ = placeholder, awaiting data.

## The axes

| Dimension | Kind | Values today | Owned by |
|---|---|---|---|
| `organisation` | binding parameter | one SIL provider (name TBD — Debbie's employer); nationwide, ~20–30 homes | frame — the whole tree sits under one org today |
| `residence` | swappable tree root | Earlwood ✅ (3 residents, source data) · Berala ⬜ · Burwood ⬜ · Blacktown ⬜ · Mascot ⬜ (all placeholder, no source data) | frame — one SIL home each |
| `resident` | tree leaf, nested in residence | 3 populated (Earlwood, placeholder names — see privacy note) + 2 placeholder per unbuilt residence | frame — one participant, one personalisation profile |
| `weekly-grid` | **invariant crosscutting contract** | 7 days × 5 meal slots (Breakfast 8am, Morning Tea 10:30am, Lunch 12:30pm, Afternoon Tea 3:30pm, Dinner 6pm), repeated 4 weeks/cycle | frame — stable across all 3 source residents; treat as the fixed shape, like the ladder in the AI-training frame |
| `constraint-block` | crosscutting, **optional per resident** | 7 block types observed: dislikes list, portion-guide/clinical paragraph, SIL-day flag, community-participation marker, conditional substitution, running quota, eat-out placeholder | frame — presence/absence and wording vary per resident; none is guaranteed present |
| `dinner-rotation` | shared cross-resident constant | 28-recipe rotation, identical across all 3 Earlwood residents for the same week/day | frame — batch-cooked; confirmed shared *within* Earlwood only; unknown across residences |
| `tier` | deployment | static (docx, current — hand-produced by Debbie) · live (generated per resident/week) | same frame + contract would serve both |

## How they compose

```
organisation → residence → resident         swappable tree, one home per residence
resident × weekly-grid                       the fixed 7×5 grid every resident's plan fills
resident × constraint-block                  the optional personalisation layer (0–7 blocks present)
residence × dinner-rotation                  shared batch-cooked constant (scope TBD beyond Earlwood)
everything × tier                            static docx today, live generation is unbuilt
```

Not a full cartesian product: `constraint-block` values are **optional and free-text today**,
not a controlled vocabulary — e.g. the community-participation marker alone has three
observed spellings (`ExtCP`, `EXTCP - <name>`, `DMS-CP`) across just 3 residents. A
generator built directly on this frame would need to decide whether to normalise that
vocabulary or preserve resident-specific convention.

## Two template lineages (real finding, not yet resolved)

The footer/document-control table itself differs in shape across the 3 source residents:
- **Lineage A** (2×2: Document Name / Version / Document Number / Effective Date) — 2 of 3
- **Lineage B** (1×2: Document Name / Date Developed / Version, Author / Date of Review / Page) — 1 of 3

Open question for Debbie: does this reflect two real template versions used across the
company (e.g. per-region or per-era), or a one-off drift in a single document? The frame
tracks both lineages until resolved — see `open_questions` in `meal_plans/frame.json`.

## Privacy note

Real resident names and clinical details (medication timing, weight targets) appear in the
source `.docx` files. Per the FRAME-LEDGER's standing rule ("real-resident data must NOT be
used until a privacy footing is agreed"), this frame uses **placeholder names for all
residents, including Earlwood's three** — the personalisation *shape* is drawn from the
real source, identities are not. Do not paste real names/health specifics into this repo
until that footing exists.

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
