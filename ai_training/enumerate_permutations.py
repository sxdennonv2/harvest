#!/usr/bin/env python3
"""Enumerate the AI-training estate's addressable permutations from the frames.

The frames (each course's course.json) are the source of truth; this script is a
build product generator — it emits a DISPOSABLE work-list manifest, never edits a
frame, and can be re-run at any time. A coordinate counts as built when its target
page exists on disk, so re-runs are incremental: only genuinely missing pages
become jobs. The manifest is what a fan-out orchestrator
consumes: one row = one subagent job (one lesson-variant, per the one-invocation-
one-unit contract).

Axis rules encoded here (see ai_training/DIMENSIONS.md):
- pipeline/application/lesson: read from the frames.
- persona: multiplies FUNCTIONALITY pages only. The communication course is
  persona-wide by its MISSION ("the whole office"; persona-relevance binding is
  already neutral) — pass --personas-include-communication to override.
- context: lives INSIDE communication pages (context-rebind element) — never forks.
- tier: static only. Live-tier permutations are runtime generations by definition;
  pre-building them would be the static tier in costume, so they are counted in the
  summary but never emitted as jobs.

Usage:
  enumerate_permutations.py                  # summary to stdout
  enumerate_permutations.py --out manifest.json   # + write the work-list
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).parent

# persona key -> (family dir name, display name, survey grounding)
PERSONAS: dict[str, tuple[str, str]] = {
    "buying-analyst": ("teach-buying-analyst", "Buying analyst"),
    "specialist-analyst": ("teach-specialist-analyst", "Specialist / Analyst"),
    "manager-director": ("teach-manager-director", "Manager / Director"),
    "office-assistant": ("teach-office-assistant", "Office Assistant"),
}
BUILT_PERSONA = "buying-analyst"  # the authored source family

FUNCTIONALITY_COURSES = ["excel", "outlook", "powerpoint", "word"]
COMMUNICATION_DIR = ROOT / "communication"


def load_frame(path: Path) -> dict:
    return json.loads((path / "course.json").read_text(encoding="utf-8"))


def spine(frame: dict) -> list[dict]:
    """Lessons + subcards in authored order (same rule as the builder/verifier)."""
    out = []
    for lesson in frame["lessons"]:
        out.append(lesson)
        out.extend(lesson.get("subcards", []))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, help="write the pending work-list as JSON")
    ap.add_argument("--personas-include-communication", action="store_true",
                    help="also fork the communication course per persona (default: "
                         "persona-wide, no fork)")
    args = ap.parse_args()

    jobs: list[dict] = []
    built = 0
    context_cells = 0

    # Functionality pipeline: application tree, persona forks pages.
    for course in FUNCTIONALITY_COURSES:
        src_dir = ROOT / "teach-buying-analyst" / course
        frame = load_frame(src_dir)
        for lesson in spine(frame):
            for persona, (family, display) in PERSONAS.items():
                if persona == BUILT_PERSONA:
                    built += 1
                    continue
                target = ROOT / family / course / "lessons" / lesson["file"]
                if target.exists():
                    built += 1
                    continue
                jobs.append({
                    "pipeline": "app-functionality",
                    "course": course,
                    "persona": persona,
                    "kind": "persona-variant",
                    "slug": lesson["slug"],
                    "title": lesson["title"],
                    "theme": lesson.get("theme", ""),
                    "builds_on": lesson.get("builds_on", []),
                    "source_page": str(src_dir / "lessons" / lesson["file"]),
                    "target_page": str(target),
                    "note": f"translate persona bindings/voice to {display}; craft, "
                            f"scenarios, rungs and checks stand",
                })

    # Communication pipeline: persona-wide unless overridden; contexts in-page.
    comm = load_frame(COMMUNICATION_DIR)
    for lesson in spine(comm):
        context_cells += len(lesson.get("contexts", ["email"]))
        if args.personas_include_communication:
            for persona, (family, display) in PERSONAS.items():
                if persona == BUILT_PERSONA:
                    built += 1
                    continue
                target = ROOT / f"communication-{persona}" / "lessons" / lesson["file"]
                if target.exists():
                    built += 1
                    continue
                jobs.append({
                    "pipeline": "communication", "course": "communication",
                    "persona": persona, "kind": "persona-variant",
                    "slug": lesson["slug"], "title": lesson["title"],
                    "theme": lesson.get("theme", ""),
                    "source_page": str(COMMUNICATION_DIR / "lessons" / lesson["file"]),
                    "target_page": str(target),
                    "note": f"persona variant for {display}",
                })
        else:
            built += 1  # persona-wide page serves all personas as-is

    static_total = built + len(jobs)
    print(f"built pages (static, authored)     : {built}")
    print(f"pending jobs (static, enumerable)  : {len(jobs)}")
    print(f"static-tier addressable total      : {static_total}")
    print(f"communication lesson×context cells : {context_cells} (carried in-page)")
    print(f"live-tier permutations             : unbounded (runtime generation over "
          f"{static_total} static coordinates — never pre-built)")
    if jobs:
        by = {}
        for j in jobs:
            key = (j["persona"], j["course"])
            by[key] = by.get(key, 0) + 1
        print("\npending by persona × course:")
        for (persona, course), n in sorted(by.items()):
            print(f"  {persona:20} {course:14} {n}")

    if args.out:
        args.out.write_text(json.dumps(
            {"generated_from": "frames (course.json) — disposable build product",
             "built": built, "pending": jobs}, indent=2), encoding="utf-8")
        print(f"\nwork-list written: {args.out} ({len(jobs)} jobs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
