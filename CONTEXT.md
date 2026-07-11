# Harvest

The ubiquitous language of the Harvest pattern — the terms used identically in
conversation, documents, skills, and filenames across every pipeline in this repo.
Names steer (Pocock): when a term below appears in a packet or a contract, it means
exactly this and nothing else. Pipelines may grow local dialects (SIL's
*harmonization*, ai_training's *ladder* and *specimen*, punditry's *channel*) in
their own docs; this file holds the pattern-level language only.

Five rules govern how this language binds:

- **Machinery, never produce.** These terms bind contracts, skills, packets, frames,
  and registers — the method's own artifacts. Inside a unit, the audience's language
  rules: a meal plan says "Weekly Menu Planner" because that is Debbie's word.
- **Avoid-terms are scoped.** An _Avoid_ term is banned as a name for the term it
  shadows, not banished from English — "the checklist is the verifier's spec" is
  fine; "the unit contract (spec)" is not. A term marked _Avoid (always)_ is banned
  outright.
- **Identifiers are two-tier.** Machine-read names that already shipped (frame keys,
  element IDs, skill names — e.g. the frame key `contexts`, the element
  `context-rebind`) are frozen: renaming them is churn across scripts and produce
  for zero unit gain. All *new* identifiers must be conformant from birth.
- **The two-pipeline test.** A term earns an entry here only when a second pipeline
  needs it; until then it is dialect and lives in its pipeline's own docs.
- **Enforcement is prospective and judged.** New and next-touched machinery
  conforms; the check is a judged item in the orchestrator's integrate-verify-merge
  pass and in any edit to a machinery artifact — not a lint script, and never a
  retroactive sweep.

One word is handled with tongs: **context**. It is genuinely overloaded (packet
context, LLM context, CONTEXT.md) — never use it bare; say the precise thing.

## The pattern

**Harvest**:
The method itself — a pipeline of composable atomistic skills, moving through
frame → expand → instantiate → verify → compound. Persists entirely as six kinds of
text file plus git; has no runtime.
_Avoid_: framework, platform, system

**Container**:
One of the six kinds of persistent text Harvest lives in: frame, contract, skills,
deterministic tools, grounding, and git. Everything the pattern knows is in a
container; nothing persists by memory.
_Avoid_: component, store

**Frame**:
A domain's structure captured as data (JSON), owned by judgement and read by code.
The single source of truth for what exists in a pipeline.
_Avoid_: config, schema, taxonomy file

**Grounding**:
The container holding what a pipeline's authors cite and its voices anchor to —
MISSION, RESOURCES, exemplar packs. Structure lives in the frame, anatomy in the
contract; the world lives here.
_Avoid_: knowledge base, docs (bare)

**Expansion**:
How a frame's coordinates become work: **Enumeration** (a finite, listable set,
produced in batches) or **Stream** (coordinates arriving on a clock or as events,
produced one at a time, forever).
_Avoid_: generation mode, rollout

**Instantiate**:
The stage where an agent spends judgement once to produce one unit from one
coordinate, against the contract. The agent doing this is the **author** — it
authors the author-owned elements, and instantiation skills are named
`<unit>-author`. Build time only, never runtime (static tier). Machines render;
authors author: **render** means deterministic materialisation (the Builder,
machine-owned elements, conditional blocks, per-platform variants) and never the
author's act.
_Avoid (always)_: generate. _Avoid_: render (for the author's act)

**Verify**:
The stage that gates every unit before it ships: deterministic checks first, judged
review second, human sign-off where liability demands it.
_Avoid_: QA, review (bare)

**Compound**:
The stage where feedback folds back into frames, contracts, skills, or grounding —
so the next unit is cheaper or better than the last. Recorded in git; nothing
compounds by memory.
_Avoid_: retro, learning loop (as a noun for the stage)

## The space

**Dimension**:
A named axis of a pipeline's addressable space (persona, theme, rung…), declared in
a DIMENSIONS.md with its kind: tree, crosscutting invariant, or binding.
_Avoid_: parameter (bare), variable

**Coordinate**:
One point in a frame's space — enough to name a unit unambiguously (course × theme ×
lesson × persona). Units carry their coordinates for life (see Coordinate tags).
_Avoid_: permutation (that's the count, not the point), cell

**Spine**:
A frame's units-and-subunits in authored order; the walk the Builder numbers and
navigates.
_Avoid_: sequence, list

**Candidate**:
A coordinate that exists in the frame but has no unit yet — enumerated, waiting. A
built unit is never a candidate.
_Avoid_: backlog item, todo

**Prerequisite edge (`builds_on`)**:
A frame-encoded dependency between units: the prerequisite must precede the dependent
in the spine (static) and in serving order (live). Asserted only when the unit's own
prose depends on it; contrast-references don't qualify.
_Avoid_: link, relation

**Persona**:
The audience binding a family of produce is voiced for. In pipelines whose frames
fork by audience it forks family dirs; in persona-wide produce it doesn't.
_Avoid_: user type, role (bare)

**Tier**:
Where materialisation happens: **static** (agent at build time, pre-built produce,
host-anywhere — for audiences without agents) or **live** (agent at runtime, generated
per request over the same frame + contract — never pre-built).
_Avoid_: mode, deployment (bare)

## The unit

**Unit**:
The atomistic thing a pipeline produces — a lesson page, a meal plan, a risk
assessment, a post, a reply. One skill invocation makes exactly one.
_Avoid_: artifact (too broad — contracts are artifacts too), item, deliverable

**Unit contract**:
The written anatomy every unit must satisfy, plus its verify checklist. What makes
judgement delegable without decay.
_Avoid_: spec, template (a template renders; a contract judges)

**Element**:
One named slot in a unit's anatomy. **Machine-owned** elements are written by the
Builder from the frame; **author-owned** elements are produced by the instantiating
agent.
_Avoid_: section (bare), field

**Binding**:
A parameter's concrete form in a given unit ("Why it matters to a buyer" is the
buying-analyst binding of the persona-relevance element). Elements are invariant;
bindings vary.
_Avoid_: customisation, variant (Variant is a persona-forked unit)

**Rebinding**:
Extending an existing unit along another binding of a crosscutting axis — another
persona, platform, or setting — without forking it: a move, not a rewrite. Carried
by a compact optional element with the invariant restated.
_Avoid_: port, duplicate

**One idea**:
The single concept a unit delivers or teaches. If a unit needs a second, the frame is
wrong — split the coordinate, don't pad the unit.
_Avoid_: topic, theme (Theme is a frame grouping)

**Must-survive list**:
The unit's load, enumerated: the facts, asks, owners, dates (or hazards, allergens,
figures) that every transformation of the unit must preserve. The reconciliation
check at every rung.
_Avoid_: requirements, acceptance criteria

**Produce**:
What the pipeline outputs — the units themselves, as distinct from the machinery that
made them. Produce is product; machinery is method.
_Avoid_: output (bare), content

## The work

**Skill**:
An agentic stage as versioned prose instructions (plus bundled deterministic scripts)
— source code whose interpreter is a model. One invocation, one unit.
_Avoid_: prompt (a skill outlives any prompt), agent (the agent runs the skill)

**Builder**:
The deterministic renderer that replays a frame forever: numbering, navigation,
indexes, grids. Course-agnostic; idempotent; makes agent output order-independent.
_Avoid_: generator (bare), compiler

**Enumerator**:
The deterministic script that walks frames and emits a Manifest. For streams, the
enumerator is a **Calendar** (a clock, not a list).
_Avoid_: planner

**Manifest**:
The disposable work-list an Enumerator emits — one row per pending unit-job. A build
product, never a source of truth; regenerate rather than edit.
_Avoid_: queue, plan file

**Packet**:
The self-contained brief a delegated agent authors from: contract pointer,
coordinate, pins, grounding anchors, hard rules — complete enough that the agent
never sees the parent conversation. Each pipeline's DIMENSIONS.md declares its own
ingredient list.
_Avoid_: prompt, brief (bare); never bare "context"

**Pin**:
A judgement made in the packet so the agent doesn't wander — the pinned one-idea, a
named failure mode to avoid. Pins are the steering.
_Avoid_: hint, guideline

**Orchestrator / Author split**:
The concurrency law of delegated batches: authors write only their own unit file;
the orchestrator alone touches shared files (frames, packs, scaffolding, indexes).
_Avoid_: locking, coordination (bare)

**Batch**:
One fan-out of parallel author invocations plus the orchestrator's integrate-verify-
merge pass. One PR per batch. A **Sweep** is the batches that exhaust a manifest.
_Avoid_: run, job (a job is one row)

**Line**:
One unit-kind within a pipeline, with its own contract, cadence, gate, and feedback
liquidity (sil_operations runs three: meal plans, shift duties, resident reports).
Liquid lines learn; illiquid lines earn.
_Avoid_: product, stream (that's an expansion mode)

**Judge**:
An agent doing verification a script can't: voice, one-idea singularity, check
quality, grounding. Judges gate liquid lines so humans don't have to.
_Avoid_: reviewer (bare), evaluator

**Gate**:
Whatever a unit must pass before shipping, on the spectrum: deterministic checks →
judge → human review → human sign-off. Cadence predicts the gate.
_Avoid_: approval, checkpoint

**Family**:
A persona-bound directory of produce (`teach-buying-analyst/…`). Persona variants are
sibling families mirroring the source family's frames.
_Avoid_: fork, copy

## The learning

**Friction**:
What an agent reports when the contract, frame, or packet fought the work — compound-
stage input by definition, never noise. Every skill's RETURN demands it.
_Avoid_: issues, feedback (bare)

**Deviation ledger**:
The contract's running record of known departures and their resolutions — the
contract's own memory.
_Avoid_: known issues, exceptions list

**Coordinate tags**:
The frame coordinates a unit carries into the world (BOb v2.1 attribution) so its
performance can be regressed back onto the frame. No tags, no compounding.
_Avoid_: metadata (bare), tracking

**Liquidity**:
How fast and cheap a line's feedback arrives. Liquid lines (daily posts) learn;
illiquid lines (signed annual RAs) earn. The laboratory funds the register with
learning, not cash.
_Avoid_: velocity, engagement (that's a signal, not the property)

**Anti-Goodhart loop**:
The human sitting above every metric-driven compound loop, reviewing the objective
rather than the units — so the metric never silently becomes the goal.
_Avoid_: oversight (bare), human-in-the-loop (humans are NOT in the unit loop on
liquid lines; that's the point)

**Promote-from-instance**:
Frame-birth by analysing real, validated artifacts (Debbie's menu docx, the delivered
RA) rather than eliciting blind. Pre-trusted; the best frame economics.
_Avoid_: reverse-engineering (bare)

**Elicitation primitive**:
The recorded prompt that births a frame's tree ("what are the fundamental pillars of
functionality within {app}?") — a reusable asset, so frames are reproducible, not
hand-curated.
_Avoid_: brainstorm prompt

## How this file changes

This file compounds like any container: friction reports may propose term changes —
a term that fought the work is compound input, not noise. Changes land by PR with
the rationale in the commit message; Stuart signs off on every change, because
naming is judgement and a language change silently re-steers every future agent.
Standing deviations are the frozen identifiers named in the preamble; if they
outgrow it (more than ~5), give them a ledger.
