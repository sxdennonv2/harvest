# Unit Contract — one channel

The unit of the **channel-birth line** is **one channel**: the complete,
signed-off declaration from which every post and reply on that channel will be
produced. This is machinery-as-produce, stated plainly: a channel is machinery
to the punditry pipeline (its posts are the pipeline's produce), but it is
produce to the birth line that stamps it — one channel contract governs every
channel, which is exactly what makes channels units rather than bespoke builds
(the discriminator: one written standard governs them all).

This contract is consumed by:

- **`channel-author`** (to create) at instantiate time — births one channel per
  invocation: promote-from-instance where a validated instance or dataset
  exists (climate-pulse's running machinery; whisky's tasting/pricing data),
  elicited otherwise;
- the **studio runtime** (BOb / punditry-harness) — every element below maps
  onto the `CHANNEL.md` surface the harness already reads (see the mapping
  column in the Elements table); the runtime surface is frozen, this contract
  does not rename it;
- **`channel-verify`** (to create) — the checklist at the end is the verifier's
  spec, plus Stuart at the two human gates (birth sign-off, go-live).

Editing this contract is machinery work: touched prose must conform to the
pattern language in the repo-root `CONTEXT.md` (judged at
integrate-verify-merge). A channel instance's **voice material** — its mission
prose, persona commitments, vocabulary lists, sample fragments — is produce:
inside it the channel's own register rules, exactly as Debbie's language rules
inside a meal plan.

Promoted from the running instance, 2026-07-11: `climate-pulse` (status
`dry-run` in the studio repo) — its `CHANNEL.md`, its five subagent briefs, and
the `climate-pulse-draft` portfolio skill — together with the studio machinery
that already abstracts the anatomy once (`CHANNEL.md.template`,
`CHANNEL-ONBOARDING.md` at `studio/punditry-channels/`). This contract lifts
that anatomy into the pattern's containers and adds the verify gate; runtime
enforcement (state plane, harness invariants, scheduler) stays in the studio
docs it already lives in.

## Parameters

A channel is authored from a roster coordinate plus these parameters. Elements
are invariant; bindings vary with the channel.

| Parameter | climate-pulse (reference) | Varies with |
|---|---|---|
| `channel_id` | `climate-pulse` | channel — `^[a-z0-9][a-z0-9-]{1,40}$`, equals its directory name everywhere |
| `domain` | AU/global climate + energy discourse | channel |
| `birth_method` | promote-from-instance (running skill + studio `CHANNEL.md`) | channel — promote where an instance or dataset exists; elicit otherwise |
| `platform_set` | X (first) | binding — per-platform variants render from one authored post; never forks the channel |
| `modality_set` | text (default) | binding — audio-visual renders via av-pilot machinery when extracted; never forks the channel |
| `status` | `dry-run` | lifecycle state (see Lifecycle) |

Births are **serial**: one channel per `channel-author` invocation, and
friction from each birth folds into this contract and the birth skill before
the next birth begins. The birth order is judgement (owner-owned), not a
manifest — climate-pulse first (running instance), whisky second (existing
dataset).

## Ownership

Three classes of element:

- **owner-owned** (Stuart) — the judgement that makes a channel worth running:
  `mission`, `guardrails`, `success-definitions` (including kill criteria),
  the cadence-policy decision, birth order, and both human gates. The author
  may draft these for review; it may not originate or weaken them.
- **author-owned** (`channel-author`) — everything promoted or elicited:
  `persona`, `audience`, `topic-tree`, `format-set`, `grounding`, `targets`,
  the initial `exemplar-pack` selection. Proposed by the author, signed off by
  the owner at the birth gate.
- **machine-owned** — `channel-header` validation, `artifact-pins` resolution,
  `runtime-wiring` scaffolding (state-plane directories, seed files). Rendered,
  never authored.

## Elements

In declaration order. Every element is required unless marked optional. The
"studio surface" column maps each element to where the running harness reads
it — the six-section `CHANNEL.md` anatomy is a frozen runtime surface
(onboarding doc: no seventh section); harvest-side elements that lack a
section map into briefs or grounding, as noted.

| # | Element | Owner | Studio surface | Reference rendering (climate-pulse) |
|---|---|---|---|---|
| 1 | `channel-header` | machine | header block | `channel_id` · `status` · `owner` · `created` |
| 2 | `mission` | owner | §1 Brief · Mission | "Reframe the climate conversation toward measurement, not faction… credible named voice in 30 days or kill the experiment" |
| 3 | `persona` | author | §1 Brief · Voice/register (+ the author skill's editorial stance) | five core commitments · register ("dance like a butterfly, sting like a bee") · vocabulary-prefer · two vocabulary-avoid lists · sample fragments |
| 4 | `audience` | author | §1 Brief · Audience | Curious Professional (primary) · Methodological Skeptic (secondary) · one optimisation rule |
| 5 | `guardrails` | owner | §1 Brief · Hard do-nots | no personal attacks · no defamation · no unsourced claims · no partisan tribal markers · neither fossil-fuel apologetics nor renewable-techno-utopianism |
| 6 | `grounding` | author | §2 Knowledge base | grounding root path · source canon · citation rule ("every empirical claim sourced inline") |
| 7 | `topic-tree` | author | research brief (no dedicated section) | the angle set: data release · new study · policy development · market signal · methodological note |
| 8 | `format-set` | author | §3 `formats_per_day` keys (+ the author skill's writing constraints) | thread (hook → unpack → landing) · standalone · reply · quote-tweet, each with per-platform shape rules |
| 9 | `cadence-policy` | owner | §3 Cadence | quiet hours 22:00–05:00 AEST · ≤6 posts/day · 45-min gap · per-format daily counts |
| 10 | `success-definitions` | owner | §4 Success definitions | named-voice engagements (30d) · follower delta (30d) · reply quality · kill criteria at 14d/21d/30d |
| 11 | `targets` | author | §5 Targets | 20–50 named voices · strategy per side: skewer / amplify / monitor |
| 12 | `artifact-pins` | machine | §6 Artifact pin | `(none yet)` at birth is valid |
| 13 | `exemplar-pack` *(optional at birth)* | author, grows by compound | grounding (no dedicated section) | empty at birth; populated by the first gated posts |
| 14 | `runtime-wiring` *(required from dry-run)* | machine | appendix | state-plane path · harness packages · five briefs · scheduler |

### Element specifications

**channel-header.** Four fields: `channel_id` (the lowercase-hyphen slug used
everywhere internal — display names live in the mission), `status`, `owner`,
`created`. The `channel_id` must equal the channel's directory name in every
plane; the studio state layer validates the format and refuses traversal.

**mission.** One paragraph, owner-owned: why this channel exists, who it
serves, and what winning looks like — including the experiment framing when
the channel is a wedge (climate-pulse: named voice in 30 days or kill). A
mission that cannot fail is not a mission; the kill horizon belongs here or in
`success-definitions`, but it must exist.

**persona.** The voice fingerprint, and the element the whole unit stands on.
Promoted structure, all five parts required:

1. **core commitments** — the stance as testable rules (climate-pulse:
   "descriptive statistics before inference", "out-of-sample is the test"),
   not adjectives;
2. **register** — how the voice carries itself, stated as behaviour
   ("attack methodology, never motives; steelman before you dismantle; let
   sentence structure carry the sharpness");
3. **vocabulary-prefer** — the terms the voice reaches for;
4. **two vocabulary-avoid lists, one per adjacent failure register** — every
   persona sits between two registers it must not drift into (climate-pulse:
   orthodox-activist and dismissive-contrarian). Naming both is required; a
   persona with one enemy register drifts into the other. The both-sides
   rewrite rule follows: if a post could pass as either register's copy,
   rewrite;
5. **sample voice fragments** — 3–6, marked *calibration only, never reuse
   verbatim*.

**audience.** Named personas — a title, an age band, what they already know,
what they want from this channel — never demographics alone. One primary, at
most one secondary, and an explicit optimisation rule for when they pull apart
("optimise for the Curious Professional; don't lose the Skeptic").

**guardrails.** Owner-owned hard clauses, phrased so a judge can block on them
— each one checkable against a single post or reply, no interpretation beyond
the text. Must cover: the law (defamation, the domain's regulated-advice lines
— medical, financial — where the domain has them), sourcing (no claim the
channel wouldn't cite), tribal signalling (both directions), and the
**amplification clause** (estate register, 2026-07-11): when a sibling
channel's post arrives as a trigger, this channel authors its own unit through
its own persona, topic-tree, and contract — mechanical echo is banned
outright. Where the register is adversarial, the **hostile-screenshot test**
is a required guardrail: any single post, screenshotted alone by a hostile
reader, must read as a sourced observation, not a cheap shot.

**grounding.** The channel's grounding root (studio surface calls it the KB
root — frozen name, cite as-is), the source canon (what this channel is
allowed to lean on: named datasets for climate-pulse, tasting/pricing data for
whisky, texts and translations for a scripture channel), and the citation
rule. The citation rule is per-channel but never absent.

**topic-tree.** The channel's themes as frame material — what this channel may
speak about, structured for a coordinate pick (the running instance carries it
as the research brief's angle set; an extracted channel carries it in
`channel.json`). The topic-tree bounds the calendar tick's daily pick and the
amplification trigger's reachability test: a sibling's post a channel's
topic-tree cannot reach is a trigger that channel never receives.

**format-set.** The formats this channel may use, each with its shape stated
(the thread anatomy hook → unpack → landing is climate-pulse's; other channels
declare their own). Per-platform constraints (character limits, threading
conventions) are platform bindings and live with the platform contract — the
format-set says *what shapes exist*, the platform binding says *how each
renders here*.

**cadence-policy.** Owner-owned numbers the publish gate enforces: quiet
hours, max posts/day, min gap, per-format daily counts. The author may propose
values from the instance; the owner disposes.

**success-definitions.** Outcomes with horizons, and **kill criteria** — the
midpoint check and the alarm condition included (climate-pulse: 14d midpoint,
21d zero-named-voice alarm, 30d live-or-die). A channel born without kill
criteria cannot fail, and a unit that cannot fail cannot be judged.

**targets.** The named voices this channel engages, seeded at birth (20–50 for
climate-pulse), each carrying a strategy: skewer the loud-and-poorly-reasoned,
amplify the rigorous-and-underweighted, monitor the rest.

**artifact-pins.** The table of data artifacts the channel consumes, resolved
through the studio artifact plane's resolver, never a directory crawl.
`(none yet)` is a valid birth state.

**exemplar-pack.** The few-shot anchor: the channel's best real posts, added
as they pass the gate and earn signal. Empty at birth by definition — a
promoted channel may seed it from the source instance's gated output; an
elicited channel starts bare. Every exemplar carries its coordinate tags.

**runtime-wiring.** Machine-owned scaffold, required only from `dry-run`:
state-plane directory and seed files, harness package references, the five
subagent briefs, scheduler entries. Defined normatively in the studio
onboarding doc; this contract only requires that it exist and validate before
`dry-run`.

## Lifecycle

A channel moves through four states; transitions add requirements, never relax
them.

| Current state | Valid transitions | Gate |
|---|---|---|
| `paused` (born) | → `dry-run` | mechanical checklist + judged review + **owner sign-off on mission, persona, guardrails** |
| `dry-run` | → `live` · → `killed` | dry-cycle clean (state-plane writes land, zero tree writes, output parity) + **owner go-live approval, recorded** |
| `live` | → `killed` | kill criteria fire, or owner decision |
| `killed` | none — terminal | the state plane keeps the data; the channel stops firing |

Going backwards is not a transition: a `live` channel that stops is killed,
not paused. The channel is the illiquid unit of an otherwise liquid pipeline —
posts ship daily through automated judges, but a channel is born roughly ten
times ever and a misborn channel poisons every post it stamps. Cadence
predicts the gate: **both human gates are mandatory**, matching the estate's
verify↔liquidity spectrum.

## Relationship to the frame

The channel-birth line's frame is the **roster**: one coordinate per planned
channel, each row carrying `channel_id`, domain, birth method, and birth
order. The roster is owner-owned frame data. (Flagged at drafting: the harvest
estate register and the studio `punditry-channels/` directory currently
disagree on the roster — resolution is Stuart's, and this contract
deliberately does not list a roster for that reason.)

Per coordinate, the birth method selects the author's path: promote (analyse
the validated instance or dataset, lift its judgement into the elements) or
elicit (run the elicitation primitive per element — the persona and topic-tree
interviews). Promotion is preferred wherever an instance exists: it is
pre-trusted, the best frame economics.

## Degrees of freedom

The author may: propose every author-owned element from the instance or the
elicitation; seed the exemplar-pack from the source instance's gated output;
propose cadence values for the owner to dispose. It may not: originate or
weaken a guardrail; write a mission; set or soften kill criteria; reuse a
sibling channel's persona wholesale (differentiation is judged at the birth
gate); declare a roster coordinate not owned by the roster; touch the frozen
studio runtime surface (section names, state-plane paths, `channel_id`
format).

## Verify checklist (the future `channel-verify` spec)

Mechanical (no judgement):

- [ ] `channel_id` matches `^[a-z0-9][a-z0-9-]{1,40}$` and equals its
      directory name.
- [ ] All required elements present in declaration order; no placeholder lines
      at `dry-run` or beyond.
- [ ] `persona` carries all five parts, including **two** vocabulary-avoid
      lists; prefer/avoid lists are disjoint.
- [ ] Every guardrail is phrased as a blockable clause (checkable against a
      single unit); the amplification clause is present.
- [ ] `cadence-policy`: per-format daily counts sum to ≤ max posts/day; quiet
      hours are valid hours.
- [ ] `success-definitions` include at least one kill criterion with a
      horizon.
- [ ] `targets` seeded within the declared count band, every row carrying a
      strategy.
- [ ] Every exemplar-pack entry carries coordinate tags.
- [ ] From `dry-run`: runtime-wiring validates per the studio onboarding
      checklist (briefs present, state-plane seeds present, pins resolve).

Judged (agent):

- [ ] The persona is distinct from every sibling channel — a reader shown two
      channels' posts unlabelled would not merge them.
- [ ] The guardrails cover the domain's liability surface (the judged
      question: *what would a lawyer or a regulator flag in this domain, and
      is there a clause for it?*).
- [ ] The mission answers why-this-channel-exists and who-it-serves, and can
      fail.
- [ ] The sample fragments actually exhibit the declared register (read them
      against the commitments).
- [ ] The two avoid-registers are genuinely the adjacent failure modes for
      this domain, not generic.
- [ ] The topic-tree is wide enough for a daily tick and bounded enough to
      keep the persona coherent.

Human (Stuart) — both mandatory, per Lifecycle:

- [ ] Birth sign-off: mission, persona, guardrails, kill criteria.
- [ ] Go-live approval, recorded.

## Known open items

1. **The roster conflict** — harvest's estate register (7 named + 3 TBA) vs
   the studio `punditry-channels/` directory (14 scaffolds; only climate-pulse
   and whisky appear in both). Owner decision; the frame waits on it.
2. **Post and reply unit contracts** — separate artifacts (the estate register
   already names them); this contract governs the channel, not its produce.
3. **Extraction timing** — BOb launches on its own runtime by standing
   decision; when a channel is extracted into harvest containers
   (`channel.json` et al.), the studio `CHANNEL.md` surface remains the
   runtime rendering of the same unit, not a second source of truth.
