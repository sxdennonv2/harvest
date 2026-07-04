#!/usr/bin/env python3
"""Mechanical verifier for Harvest lesson pages.

The deterministic half of the lesson-verify skill: checks every lesson in one or more
course directories against the unit contract's mechanical checklist (CONTRACT.md).
Judged checks (one-idea singularity, prompt self-containment, check quality, voice,
citation grounding) belong to the agent, not this script.

Usage:  verify_lessons.py <course-dir> [<course-dir> ...]
Exit 0 = all mechanical checks pass; exit 1 = failures listed on stdout.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ELEMENT_CHECKS: list[tuple[str, str]] = [
    ("title-tag", r"<title>[^<]+</title>"),
    ("lesson-nav", r'<nav class="lesson-nav">'),
    ("kicker", r'<p class="kicker">'),
    ("mission-tie", r'class="mission"'),
    ("practice-pointer", r'class="workbook"'),
    ("one-idea", r"<h2>The one idea</h2>"),
    ("persona-relevance", r"<h2>Why it matters"),
    ("bad-habit", r"callout bad"),
    ("manual-craft", r"<h2>How to do it</h2>"),
    ("quiz-heading", r"<h2>Check yourself</h2>"),
    ("try-real", r"<h2>Try it for real</h2>"),
    ("ladder-intro", r"<h2>The AI moves"),
    ("ladder-point", r"The point of the ladder"),
    ("primary-source", r"Primary source"),
    ("ask-teacher", r'class="ask"'),
    ("footer-nav", r'<footer class="lesson-nav">'),
]


def spine(data: dict) -> list[dict]:
    """Lessons + subcards in authored order (subcards inherit the parent theme)."""
    out: list[dict] = []
    for lesson in data["lessons"]:
        out.append(lesson)
        for sub in lesson.get("subcards", []):
            sub = dict(sub)
            sub.setdefault("theme", lesson.get("theme", ""))
            out.append(sub)
    return out


def verify_lesson(course_dir: Path, lesson: dict, n_rungs: int) -> list[str]:
    path = course_dir / "lessons" / lesson["file"]
    if not path.exists():
        return [f"file missing: {lesson['file']}"]
    text = path.read_text(encoding="utf-8")
    fails = []

    for name, pattern in ELEMENT_CHECKS:
        if not re.search(pattern, text):
            fails.append(f"missing {name}")

    answers = re.findall(r'<div class="q-block" data-answer="(\d+)"', text)
    if len(answers) != 3:
        fails.append(f"quiz blocks = {len(answers)} (contract: exactly 3)")
    if any(int(a) > 3 for a in answers):
        fails.append("quiz data-answer out of range 0-3")

    moves = len(re.findall(r"<h3>Rung", text))
    if moves != n_rungs - 1:
        fails.append(f"rung-moves = {moves} (contract: {n_rungs - 1})")
    if len(re.findall(r"<textarea", text)) < n_rungs - 1:
        fails.append("copyable prompt textarea missing for a rung")
    checks = len(re.findall(r"<strong>Check:</strong>", text))
    if checks < n_rungs - 1:
        fails.append(f"rung checks = {checks} (contract: one per rung-move)")

    if re.search(r"Lesson [1-9](?![0-9])", text):
        fails.append("bare lesson-number reference in prose (use slug links)")

    for href in sorted(set(re.findall(r'href="([^"]+)"', text))):
        if href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = (course_dir / "lessons" / href.split("#")[0]).resolve()
        if not target.exists():
            fails.append(f"broken link: {href}")
    return fails


def verify_frame(data: dict) -> list[str]:
    """builds_on edges: slugs exist, and authored order is a valid topological sort."""
    order = {lesson["slug"]: i for i, lesson in enumerate(spine(data))}
    fails = []
    for lesson in spine(data):
        for prereq in lesson.get("builds_on", []):
            if prereq not in order:
                fails.append(f"{lesson['slug']}: builds_on unknown slug '{prereq}'")
            elif order[prereq] >= order[lesson["slug"]]:
                fails.append(
                    f"order violates edge: {prereq} (pos {order[prereq] + 1}) must "
                    f"precede {lesson['slug']} (pos {order[lesson['slug']] + 1})"
                )
    return fails


def verify_course(course_dir: Path) -> int:
    data = json.loads((course_dir / "course.json").read_text(encoding="utf-8"))
    n_rungs = len(data["rung_headers"]["short"])
    lessons = spine(data)
    total_fails = 0

    print(f"== {data['course']['title']}  ({len(lessons)} pages, {n_rungs}-rung ladder)")
    for fail in verify_frame(data):
        total_fails += 1
        print(f"  FRAME FAIL  {fail}")
    for lesson in lessons:
        fails = verify_lesson(course_dir, lesson, n_rungs)
        if fails:
            total_fails += len(fails)
            for fail in fails:
                print(f"  FAIL  {lesson['slug']}: {fail}")
        else:
            print(f"  pass  {lesson['slug']}")
    return total_fails


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    grand_total = 0
    for arg in sys.argv[1:]:
        grand_total += verify_course(Path(arg))
        print()
    print(f"{'ALL MECHANICAL CHECKS PASS' if grand_total == 0 else f'{grand_total} FAILURES'}")
    return 0 if grand_total == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
