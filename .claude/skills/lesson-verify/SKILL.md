---
name: lesson-verify
description: Verify Harvest lesson pages against the unit contract — mechanical checks via bundled script, judged checks via agent. Use when asked to verify, audit, or check lessons or a course, and as the mandatory close of every lesson-author run.
argument-hint: "<course-dir> [more course-dirs] | <course-dir>/lessons/<slug>.html"
---

You are the verify stage of the Harvest pipeline. Lessons are a liquid line — verification
is automated and cheap, so run it often and whole-course by default. The contract is the
spec: `ai_training/teach-buying-analyst/CONTRACT.md` (its "Verify checklist" section is
what you are executing; both pipelines share it).

## Stage 1 — mechanical (always, first)

Run the bundled script against every course dir in scope:

    .venv/bin/python .claude/skills/lesson-verify/verify_lessons.py \
        ai_training/teach-buying-analyst/excel ai_training/communication [...]

It checks, per page: all 16 greppable contract elements, exactly 3 quiz blocks with
in-range answers, one rung-move per ladder rung above manual (each with a copyable
prompt textarea and a Check), no bare lesson-number prose references, and every internal
link resolving. Per frame: `builds_on` slugs exist and the authored order is a valid
topological sort.

Zero failures is the only pass. If the script and CONTRACT.md ever disagree, the
contract wins — fix the script in the same run and say so.

## Stage 2 — judged (agent, sampled or targeted)

The script cannot read for quality. On new or changed lessons (always), plus a 2–3 page
sample on whole-course runs, judge against the contract:

- **One idea**: does the page teach exactly one thing? Does the quiz test the mental
  model rather than the prose's wording?
- **Prompt self-containment**: would each rung prompt work pasted into the named tool by
  someone with only the practice artefact open? No context the tool can't have.
- **Check quality**: would each rung's check actually catch that rung's most likely
  failure (invented commitments, softened deadlines, pasted values, wrong ranges)?
- **Persona voice**: consistent with the course's binding; bad-habit concrete and real.
- **Citation grounding**: every cited source exists in the course's RESOURCES.md and
  supports the claim it anchors.

## Report

One line per page (pass / findings), frame findings, then judged findings with severity:
**violation** (contract clause broken — must fix before the lesson ships) vs **advisory**
(quality improvement). Never fix silently: report, and fix only when asked or when the
run's instructions include fixing. Findings about the contract itself (a clause that's
ambiguous, a check the script can't express) are compound-stage input — record them in
the report's final section.
