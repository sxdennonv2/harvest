# The Harvest Estate — pipeline register

Estate-level dimensions: every pipeline in this repo (built, building, or sketched),
expanded into the six containers Harvest persists in — **frame** (domain tree as data),
**contract** (unit anatomy + verify checklist), **skills** (agentic stages), **deterministic
tools** (render/verify/enumerate), **grounding** (MISSION/RESOURCES/packs), and **git**
(the compound ledger). Per-pipeline detail lives in each pipeline's own `DIMENSIONS.md`;
this file is the shape of the whole. Sketched 2026-07-05.

## The two expansion modes

Every Harvest pipeline expands its frame one of two ways, and the choice drives everything
downstream (cadence, verify mode, feedback liquidity):

- **Enumeration** — the frame's coordinates form a finite, listable set; a manifest is
  generated and units are produced in batches (courses, risk assessments, meal plans).
- **Stream** — coordinates arrive on a clock or as events; units are produced one at a
  time, forever (social posts on a calendar tick; replies on an inbound comment).

## Pipeline register

| Pipeline | Client/org | Expansion | Unit(s) | Cadence | Verify mode | Feedback liquidity | State |
|---|---|---|---|---|---|---|---|
| `ai_training/` | ALDI (workplace) | enumeration | lesson page | on demand | script + judged sample | low (colleague feedback) | **BUILT** — 223/223 static |
| `sil_operations/` | Danny Met Sally | enumeration | meal plan · shift-duty checklist · resident report | monthly (plans, reports) · per-shift | deterministic constraint checks + human review (Debbie) | low, warm access | **BUILDING** — meal_plans contract+skill+first drafts; other two lines latent |
| `risk_governance/` | LWHC (+referrals) | enumeration | Whole-of-Centre RA · Workshop RA · quarterly report · monthly maintenance log | annual · quarterly · monthly | **human sign-off** (priced/liability — what the $15k buys) | very low, monetised | **SKETCH** — proven manually (delivered engagement); generator skill exists at portfolio level (`risk-assessment-generator`); frame not yet in-repo |
| `punditry/` | public (7 named + 3 TBA channels) | **stream** | post (calendar tick) · reply (event) | daily per channel · event | **automated judges** (the liquid line) + human slow-loop over metrics (anti-Goodhart) | HIGH — the laboratory | **SKETCH, plan-only** — BOb runtime exists (studio) and launches independently; Harvest extraction deferred by Stuart's word (2026-07-08) |

## Per-pipeline expansion into the six containers

### 1. `ai_training/` (built — reference instance)
See `ai_training/DIMENSIONS.md`. Frames: 7 course.json families. Contract:
`teach-buying-analyst/CONTRACT.md`. Skills: `lesson-author`, `lesson-verify`.
Deterministic: `build_contents.py`, `verify_lessons.py`, `enumerate_permutations.py`.

### 2. `sil_operations/` (building)
See `sil_operations/DIMENSIONS.md` for meal_plans (frame.json, CONTRACT.md,
`meal-plan-author` skill, generated/ first drafts). Two latent product lines, both
promote-from-instance (analyse Debbie's real artifacts first, like meal plans did):

- **shift_duties** — unit: one duty checklist per (residence × shift). Frame axes:
  residence × shift-type (cardinality TBD from source docs) × duty items; likely a
  fixed-grid invariant like the weekly meal grid. Verify: deterministic completeness
  checks + Debbie review.
- **resident_reports** — unit: one monthly report per (residence × resident × month).
  Frame axes: residence × resident × month × report sections (contract TBD from a real
  report). Verify: human review mandatory (NDIS-adjacent, names a real person's month).
  Produce rate: residents × 12/yr.

### 3. `risk_governance/` (sketch — LWHC)
The already-monetised line, currently delivered by hand + portfolio skill; the pipeline
move is bringing its knowledge into the containers:

- **Frame** (`risk_governance/frame.json`, to create): centre × document-kind
  (whole-of-centre · workshop · quarterly-report · maintenance-log) × period ×
  (workshop-name for workshop RAs) × risk-register rows. **Time is a first-class
  coordinate** — the annual/quarterly/monthly cadence is IN the frame, so a year of
  LWHC work enumerates to ~17+W units (1 WoC + W workshops + 4 quarterlies + 12
  maintenance logs).
- **Contract** (per document-kind): the RA anatomy already implicit in the delivered
  docs — hazard rows, likelihood×severity matrix, controls, owners, review dates —
  plus the quarterly/monthly documents' anatomies. Verify checklist ends in a HUMAN
  SIGN-OFF gate, always: this line sells accountability, not documents.
- **Skills**: `ra-author` (adapt the existing portfolio `risk-assessment-generator`
  into this repo's one-unit-per-invocation shape), `ra-verify` (mechanical: every
  hazard has owner+review-date+control; matrix arithmetic; register cross-refs),
  `ra-maintain` (monthly delta pass over the register).
- **Deterministic**: register renderer (frame → docx via the repo's docx tooling),
  period enumerator (what's due this month/quarter), diff-reporter for maintenance.
- **Grounding**: MISSION (the centre's duty of care), RESOURCES (WHS legislation,
  sector guidance — the citation canon), the delivered LWHC docs as reference produce.
- **Compound**: each engagement's redlines fold back into contract/skill; referrals
  extend the org axis (the frame is org-parametric by design — second centre = new
  binding, zero new machinery).

### 4. `punditry/` (sketch — the stream instance)
The other half of the empire, and the pattern's laboratory. The persona × topic ×
format frame (sketched when the pattern was named, 2026-07-04) made concrete:

- **Frames** — one `channels/<channel>/channel.json` per channel: the **persona**
  (voice fingerprint, worldview, hard guardrails — e.g. no medical advice from
  PilatesPosition, no financial advice from TheRationalConsumer), the **topic tree**
  (that channel's themes, elicited per channel like course themes), and the
  **format set** it may use. Channel roster (10): `whisky`, `the-living-scientist`,
  `the-rational-consumer`, `the-bible-guy`, `climate-pulse`, `pilates-position`,
  `expert-on-everything`, `tba-1`, `tba-2`, `tba-3`.
- **Crosscutting invariants**: the **platform contract** (X first: length, media,
  threading conventions; platform is a *binding* like context in the communication
  course — one coordinate can render per-platform variants, it never forks the frame);
  **modality** (text · audio · visual — a binding on the same terms: the author
  authors one unit, and per-modality variants are rendered from it — a narrated
  post, a charted figure, a short video. Not hypothetical: the av-pilot line
  (storyboard → narration → cut) is the working instance of the audio-visual
  binding; when punditry builds, that machinery is extracted, never rebuilt); and
  the **post anatomy** (see contract).
- **Trigger types**: a unit is triggered one of three ways — the **calendar tick**
  (today's post, per channel), an **inbound event** (a reply-worthy mention or
  comment), or **cross-channel amplification**: a post whose windowed signal clears
  a threshold becomes a trigger event on sibling channels whose topic trees can
  reach it. Hard clause: an amplification trigger carries only the source post and
  its coordinate tags; the receiving channel authors its own unit through its own
  persona, topic tree, and contract, and gates it like any other post. Mechanical
  echo — reposting or lightly rewording across channels — is banned outright: it
  reads as coordinated inauthentic behaviour, and platforms police exactly that.
- **Channel-birth line** (machinery-as-produce): the channel is itself a unit — one
  channel contract governs every channel, which is what makes them units rather than
  bespoke builds. Contract: `punditry/channel_birth/CONTRACT.md` (drafted 2026-07-11,
  promote-from-instance from climate-pulse's running machinery). Births are serial —
  climate-pulse first, whisky (dataset) second — with friction folded between births;
  gate: **human sign-off at birth and at go-live** (the illiquid unit of the liquid
  pipeline). Skills to create: `channel-author`, `channel-verify`.
- **Contract** (`punditry/CONTRACT.md`, to create — the load-bearing artifact): a post's
  elements (hook → one point → voice signature; source rule — claims trace to the
  channel's RESOURCES; **coordinate tags** — BOb v2.1 attribution so every post carries
  its frame coordinates for the compound loop; guardrails as hard clauses). A second
  unit contract for **replies** (quote context, dignity rules, disengage-after-N-turns,
  never invent facts mid-thread).
- **Skills**: `post-author` (one post per invocation: channel frame + today's topic
  pick + format), `reply-author` (one reply per event packet), `post-verify` — and this
  is where the verify spectrum earns its keep: the liquid line is gated by **automated
  judges** (voice match, guardrail compliance, source grounding, format conformance),
  not humans; the human loop sits ABOVE the metrics weekly (anti-Goodhart), not on
  each unit. (The `climate-pulse-draft` portfolio skill is a proto-`post-author` for
  one channel — extract, don't rewrite.)
- **Deterministic**: the **calendar enumerator** (tick → today's work-list: 10 posts,
  channel × slot), the **poster/ingester** (X API — this is BOb, which already exists
  in the studio repo; streams are the one place the operating rules permit runtime
  code, and it's already built — extend, never rebuild), the **metrics harvester**
  (engagement per coordinate tag, windowed), the judge harness.
- **Grounding**: per-channel MISSION (why this channel exists, who it serves),
  RESOURCES (each channel's source canon: ClimatePulse → named datasets; TheBibleGuy →
  texts and translations; Whisky → the tasting/pricing data), exemplar packs (the
  voice's best posts, the few-shot anchor).
- **Compound**: the empire's engine — 70 posts/week/platform is the high-liquidity
  laboratory; windowed engagement regressed against coordinate tags updates frames
  (topics that land), formats, and skills weekly. What the laboratory learns, the
  illiquid lines (risk_governance) monetise.
- **Produce arithmetic**: posts = 10 channels × 1/day = 70/week = **3,640/year per
  platform** (platforms multiply as bindings); replies = unbounded event stream.
  Neither is pre-enumerable — the enumerator here is a *calendar*, not a manifest.

## Compound-loop flows

Every line runs the same loop shape at a different speed: **produce → signal →
instrument → fold**, with a window setting the fold cadence and a guard keeping the
metric honest. Two speeds coexist everywhere: the **inner loop** (per line, folding
into that line's own frame/skill/grounding) and the **meta loop** (friction from every
line folding into the pattern containers — CONTRACT idioms, packet shapes, skill
shapes, this register). The lab→register pipe is the meta loop: **what transfers
between lines is pattern knowledge, never content.**

| Line | Signal (from the world) | Instrument | Window | Folds into | Guard |
|---|---|---|---|---|---|
| punditry · posts | engagement per coordinate tag | metrics harvester → windowed regression | weekly | channel frames (topic weights), format sets, `post-author`, exemplar packs | anti-Goodhart human over the metrics, never over units |
| punditry · replies | thread outcomes (sentiment, disengage events) | same harness | weekly | reply contract, guardrails | same |
| ai_training | "ask your teacher" requests; colleague feedback; (live tier: learner records) | folded by hand per request | per request / monthly | bindings, packs, RESOURCES | human is the loop |
| ai_training · intra-build | agent friction reports | skill RETURN sections → PR bodies | per batch | packet template, CONTRACT deviations ledger | orchestrator judgement |
| SIL · meal plans | Debbie's dropdown overrides (algorithm pick vs her pick); lifecycle transitions (locked/shopped/closed = acceptance ground truth) | review-interface diffs | per 28-day period; quarterly pool refresh | option pools, allocation weights, constraint blocks | Debbie's override IS the human loop |
| risk_governance | client redlines; sign-off deltas; referrals | engagement-doc compare | per engagement / annual | RA contract, `ra-author`; referrals grow the org axis | sign-off is the loop |
| **meta (pattern)** | friction from all of the above | handovers, memory, this register, contract amendments | continuous | every pipeline's containers | Stuart reviews the objective |

Two structural notes: (1) **no tags, no compounding** — coordinate tags are what let a
signal find its way back to the frame coordinate that caused it; a unit that ships
untagged is a unit the pipeline cannot learn from. (2) **synthetic loops inside slow
loops** — where a real window is annual (RAs), dry-run judges and fleet rehearsals
substitute for the world until real feedback arrives.

## Empire-crosscutting axes

- **cadence**: annual → quarterly → monthly → daily → event. One spectrum from LWHC's
  Whole-of-Centre RA to a punditry reply; every unit sits somewhere on it, and where
  it sits predicts everything else about it.
- **verify mode ↔ feedback liquidity** (inverse pair): deterministic checks → automated
  judges → human review → human sign-off. The faster the cadence, the cheaper the gate
  must be (judges for daily posts); the higher the price/liability, the more human the
  gate (sign-off for RAs). Liquid lines learn; illiquid lines earn.
- **org/client**: ALDI (training) · LWHC (risk) · DMS (SIL) · the public (punditry).
  Org is a binding parameter everywhere — the second client of any pipeline costs a
  frame binding, not a build.
- **tier**: static/live where units are consumed by people who may or may not have
  agents; not meaningful for punditry (all units are published artifacts).

## Resolved decisions (Stuart, 2026-07-08)

- **`whisky/` deleted** — it was a staged attempt at a whisky-specific Harvest pipeline,
  abandoned for now. The punditry *channel* named whisky will live at
  `punditry/channels/whisky/` if and when that pipeline is built.
- **Plan, not build** — the estate stays at sketch level until Stuart has the whole
  shape in mind. No punditry scaffold, no risk_governance frame files yet; this
  register and its map ARE the current deliverable. BOb's go-live proceeds on its own
  runtime, independent of Harvest; extraction into the pipeline comes later.
- **TBA channels parked** — the roster plans for 7 named channels; three slots stay
  open and unnamed.
- **FRAME-LEDGER retired** (Stuart, 2026-07-11) — the studio-root `FRAME-LEDGER.md`
  no longer exists; this estate register is its successor. All references in this
  repo now point here; the historical instance numbering (#3 ai_training,
  #4 sil_operations) is preserved in the pipelines' own docs.
- **Channel roster resolved** (Stuart, 2026-07-11) — this register's roster (7 named
  + 3 TBA) is the channel-birth frame. The studio `punditry-channels/` directories
  beyond climate-pulse and whisky are runtime scaffolds, not frame material.

## Progress map

Estate map: `dimension-map.html` at repo root (same standard as the pipeline maps:
update after every merged batch/milestone, redeploy to its standing artifact URL).
Per-pipeline maps remain the detail views.
