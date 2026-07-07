# Harvest

The ubiquitous language of the Harvest pattern — the terms used identically in
conversation, documents, skills, and filenames across every pipeline in this repo.
Names steer (Pocock): when a term below appears in a packet or a contract, it means
exactly this and nothing else. Pipelines may grow local dialects (SIL's
*harmonization*, punditry's *channel*) in their own docs; this file holds the
pattern-level language only.

## The pattern

**Harvest**:
The method itself — a pipeline of composable atomistic skills, moving through
frame → expand → instantiate → verify → compound. Persists entirely as six kinds of
text file plus git; has no runtime.
_Avoid_: framework, platform, system

**Frame**:
A domain's structure captured as data (JSON), owned by judgement and read by code.
The single source of truth for what exists in a pipeline.
_Avoid_: config, schema, taxonomy file

**Expansion**:
How a frame's coordinates become work: **Enumeration** (a finite, listable set,
produced in batches) or **Stream** (coordinates arriving on a clock or as events,
produced one at a time, forever).
_Avoid_: generation mode, rollout

**Instantiate**:
The stage where an agent spends judgement once to produce one unit from one
coordinate, against the contract. Build time only, never runtime (static tier).
_Avoid_: generate, render (render is the Builder's word)

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
A frame's lessons-plus-subcards in authored order; the walk the Builder numbers and
navigates.
_Avoid_: sequence, list

**Candidate**:
A coordinate that exists in the frame but has no unit yet — enumerated, survey-tagged,
waiting. A built unit is never a candidate.
_Avoid_: backlog item, todo

**Prerequisite edge (`builds_on`)**:
A frame-encoded dependency between units: the prerequisite must precede the dependent
in the spine (static) and in serving order (live). Asserted only when the unit's own
prose depends on it; contrast-references don't qualify.
_Avoid_: link, relation

**Ladder / Rung**:
The organisation's GenAI adoption model — the invariant crosscutting axis every unit
climbs internally (manual craft → chat → in-app copilot → agent). One org, one
ladder; swap the org, swap the ladder.
_Avoid_: levels, tiers (Tier means deployment)

**Persona**:
The audience binding a family of produce is voiced for. In functionality pipelines it
forks family dirs; in persona-wide produce it doesn't.
_Avoid_: user type, role (bare)

**Room**:
The setting a communication unit rebinds into — email, document, slides, chat. Lives
inside pages via the rebind element ("Other rooms, same craft"); never forks a page.
_Avoid_: context — genuinely overloaded (packet context, LLM context, CONTEXT.md);
the frame key `contexts` remains for compatibility, but in language say Room.

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
A parameter's concrete rendering in a given unit ("Why it matters to a buyer" is the
buying-analyst binding of the persona-relevance element). Elements are invariant;
bindings vary.
_Avoid_: customisation, variant (Variant is a persona-forked unit)

**Rebinding**:
Extending an existing unit into another Room or persona without forking it — a move,
not a rewrite. Carried by a compact optional element with the invariant restated.
_Avoid_: port, duplicate

**One idea**:
The single concept a unit teaches or delivers. If a unit needs a second, the frame is
wrong — split the coordinate, don't pad the unit.
_Avoid_: topic, theme (Theme is a frame grouping)

**Must-survive list**:
The unit's load, enumerated: the facts, asks, owners, dates (or hazards, allergens,
figures) that every transformation of the unit must preserve. The reconciliation
check at every rung.
_Avoid_: requirements, acceptance criteria

**Specimen**:
A practice-pack scenario's deliberately flawed input (the flabby draft, the
franken-deck, the planted-error email) that units teach against.
_Avoid_: example, sample (bare)

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
The self-contained brief a delegated agent authors from: contract pointer, coordinate,
pinned one-idea, specimen anchor, rung-failure pins, voice reference, hard rules.
Complete enough that the agent never sees the parent conversation.
_Avoid_: context packet (see Room note), prompt, brief (bare)

**Pin**:
A judgement made in the packet so the agent doesn't wander: the pinned one-idea, the
named signature failure per rung. Pins are the steering.
_Avoid_: hint, guideline

**Orchestrator / Author split**:
The concurrency law of delegated batches: authors write only their own unit file;
the orchestrator alone touches shared files (frames, packs, scaffolding, indexes).
_Avoid_: locking, coordination (bare)

**Batch**:
One fan-out of parallel author invocations plus the orchestrator's integrate-verify-
merge pass. One PR per batch. A **Sweep** is the batches that exhaust a manifest.
_Avoid_: run, job (a job is one row)

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
