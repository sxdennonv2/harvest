"""Generate a course's numbering, navigation and contents from its manifest.

``course.json`` is the single source of truth. Three ordered dimensions drive
the whole site and all of them shuffle the same way — reorder, re-run, done:

* ``themes`` — the primary sequencing level; theme order groups the pages into
  sections and dictates the macro order of the course;
* ``lessons`` — topic cards, ordered within their theme;
* ``subcards`` — sub-topic cards, ordered within their parent lesson.

No numbers are stored anywhere; this script derives every number from the
theme-grouped position and stamps it into:

* each lesson page — the ``<title>``, kicker, top/footer nav, and the section
  (theme) nav bar that links to every theme's opening lesson;
* ``index.html`` — the ordered lesson list, the section nav bar, the theme x
  ladder grid, and the start link;
* ``CURRICULUM.md`` — the same list and grid in Markdown.

Lessons are laid out theme-by-theme (theme order first, authored lesson order
within); sub-cards sit in the linear walk right after their parent, so the
Prev/Next spine flows ``0003 -> 0003.1 -> 0004``. Filenames are treated as
opaque, stable identifiers. The same recipe drives a sibling course via
``--course-dir``.
"""

from __future__ import annotations

import argparse
import json
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger("build_contents")

LESSON_HTML_INDENT = "  "
MANUAL_CELL_INDENT = "          "


def _esc(text: str) -> str:
    """Escape the characters that matter inside HTML text content."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


@dataclass(frozen=True)
class Cheatsheet:
    href: str
    label: str


@dataclass
class Lesson:
    """A lesson (card) or sub-lesson; ``number`` is assigned from list order."""

    slug: str
    file: str
    title: str
    nav_label: str
    grid_label: str
    theme: str
    cheatsheet: Cheatsheet | None = None
    subcards: list["Lesson"] = field(default_factory=list)
    number: str = ""
    parent_number: str = ""

    @property
    def is_sub(self) -> bool:
        return bool(self.parent_number)

    @property
    def display(self) -> str:
        return f"{self.number} — {self.title}"

    @property
    def nav_display(self) -> str:
        return f"{self.number} — {self.nav_label}"


@dataclass(frozen=True)
class Theme:
    key: str
    title: str
    notes: tuple[str, ...]
    rungs: tuple[str, str, str]


@dataclass
class Course:
    title: str
    lessons_dir: str
    kicker_prefix: str
    end_next_label: str
    rung_corner: str
    rung_short: tuple[str, ...]
    rung_long: tuple[str, ...]
    themes: tuple[Theme, ...]
    lessons: list[Lesson]
    spine: list[Lesson] = field(default_factory=list)


def _parse_lesson(raw: dict) -> Lesson:
    cheat = raw.get("cheatsheet")
    subs = [_parse_lesson(s) for s in raw.get("subcards", [])]
    return Lesson(
        slug=raw["slug"],
        file=raw["file"],
        title=raw["title"],
        nav_label=raw["nav_label"],
        grid_label=raw["grid_label"],
        theme=raw.get("theme", ""),
        cheatsheet=Cheatsheet(cheat["href"], cheat["label"]) if cheat else None,
        subcards=subs,
    )


def _order_by_theme(lessons: list[Lesson], themes: tuple[Theme, ...]) -> list[Lesson]:
    """Sequence lessons by theme order, keeping each theme's own list order.

    Theme order (from ``course.json``) is the primary sort key, so reordering
    the ``themes`` array re-sequences whole sections of the course — the same
    shuffle-and-renumber contract the lesson list already offers. ``sorted`` is
    stable, so within a theme the authored lesson order is preserved. Lessons
    whose theme is blank or unknown fall to the end in their original order.
    """
    theme_rank = {theme.key: rank for rank, theme in enumerate(themes)}
    fallback = len(themes)
    return sorted(lessons, key=lambda lesson: theme_rank.get(lesson.theme, fallback))


def load_course(manifest_path: Path) -> Course:
    """Parse ``course.json`` and assign numbers + build the linear spine."""
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    headers = data["rung_headers"]
    course_meta = data["course"]
    themes = tuple(
        Theme(
            key=t["key"],
            title=t["title"],
            notes=tuple(t.get("notes", [])),
            rungs=tuple(t["rungs"]),  # type: ignore[arg-type]
        )
        for t in data["themes"]
    )

    lessons = _order_by_theme([_parse_lesson(item) for item in data["lessons"]], themes)

    spine: list[Lesson] = []
    for i, lesson in enumerate(lessons, start=1):
        lesson.number = f"{i:04d}"
        spine.append(lesson)
        for j, sub in enumerate(lesson.subcards, start=1):
            sub.number = f"{lesson.number}.{j}"
            sub.parent_number = lesson.number
            sub.theme = lesson.theme
            spine.append(sub)

    course = Course(
        title=course_meta["title"],
        lessons_dir=course_meta["lessons_dir"],
        kicker_prefix=course_meta["kicker_prefix"],
        end_next_label=course_meta["end_next_label"],
        rung_corner=headers["corner"],
        rung_short=tuple(headers["short"]),
        rung_long=tuple(headers["long"]),
        themes=themes,
        lessons=lessons,
        spine=spine,
    )
    logger.info("Loaded %d lessons (%d pages in spine)", len(lessons), len(spine))
    return course


# --- Lesson-page rendering -------------------------------------------------

def _theme_first_page(course: Course, theme_key: str) -> Lesson | None:
    """First page (in spine order) belonging to a theme, or None if empty."""
    for lesson in course.spine:
        if lesson.theme == theme_key:
            return lesson
    return None


def render_theme_nav(course: Course, path_prefix: str, current_key: str = "") -> str:
    """Render the section (theme) nav bar linking each theme to its first lesson.

    Only themes that already have a page are linked, so the bar never points at
    an empty section. ``path_prefix`` prefixes each href so one renderer serves
    both the course root (``lessons/``) and a lesson page (``""``, sibling files).
    The current theme is flagged so the active section can be highlighted.
    """
    links = []
    for theme in course.themes:
        first = _theme_first_page(course, theme.key)
        if first is None:
            continue
        cls = ' class="current"' if theme.key == current_key else ""
        links.append(f'    <a href="{path_prefix}{first.file}"{cls}>{_esc(theme.title)}</a>')
    body = "\n".join(links)
    return (
        '<nav class="theme-nav" aria-label="Course sections">\n'
        '    <span class="theme-nav-label">Sections</span>\n'
        f"{body}\n"
        "  </nav>"
    )


def _nav_prev_html(prev: Lesson | None) -> str:
    if prev is None:
        return ""
    return f'Previous: <a href="{prev.file}">{_esc(prev.nav_display)}</a>'


def _nav_next_html(nxt: Lesson | None, end_label: str) -> str:
    if nxt is None:
        return f"Next: {_esc(end_label)}"
    return f'Next: <a href="{nxt.file}">{_esc(nxt.nav_display)}</a>'


def _nav_mid_html(lesson: Lesson) -> str:
    contents = '<a href="../index.html">Contents</a>'
    if lesson.cheatsheet:
        return f'<a href="{lesson.cheatsheet.href}">{_esc(lesson.cheatsheet.label)}</a> · {contents}'
    return contents


def _nav_block(tag: str, lesson: Lesson, prev: Lesson | None, nxt: Lesson | None, end_label: str) -> str:
    return (
        f'<{tag} class="lesson-nav">\n'
        f'    <span class="nav-prev">{_nav_prev_html(prev)}</span>\n'
        f'    <span class="nav-mid">{_nav_mid_html(lesson)}</span>\n'
        f'    <span class="nav-next">{_nav_next_html(nxt, end_label)}</span>\n'
        f'  </{tag}>'
    )


def _kicker_text(course: Course, lesson: Lesson) -> str:
    base = f"{course.kicker_prefix} · Lesson {lesson.number}"
    if lesson.is_sub:
        return f"{base} · a sub-lesson of {lesson.parent_number}"
    return base


def _apply_theme_nav(text: str, theme_nav: str) -> tuple[str, int]:
    """Refresh (or first-time insert) the section nav bar on a lesson page.

    The bar is owned entirely by this script: if one exists it is replaced, and
    if not it is dropped in right after the top ``lesson-nav`` block. This keeps
    the lesson HTML free of hand-maintained section markup.
    """
    existing = re.compile(r'<nav class="theme-nav"[^>]*>.*?</nav>', re.DOTALL)
    if existing.search(text):
        return existing.subn(lambda _m: theme_nav, text, count=1)
    return re.subn(
        r'(<nav class="lesson-nav">.*?</nav>)',
        lambda m: f"{m.group(1)}\n\n  {theme_nav}",
        text,
        count=1,
        flags=re.DOTALL,
    )


def render_lesson_page(course: Course, index: int, lessons_root: Path) -> None:
    """Rewrite one lesson page's title, nav and kicker from computed numbers."""
    lesson = course.spine[index]
    path = lessons_root / lesson.file
    if not path.exists():
        logger.warning("Lesson file missing, skipped: %s", lesson.file)
        return

    prev = course.spine[index - 1] if index > 0 else None
    nxt = course.spine[index + 1] if index < len(course.spine) - 1 else None

    text = path.read_text(encoding="utf-8")
    title_line = _esc(f"Lesson {lesson.number} — {lesson.title}")
    kicker = _esc(_kicker_text(course, lesson))
    top = _nav_block("nav", lesson, prev, nxt, course.end_next_label)
    foot = _nav_block("footer", lesson, prev, nxt, course.end_next_label)
    theme_nav = render_theme_nav(course, "", lesson.theme)

    text, n_title = re.subn(r"<title>.*?</title>", lambda _m: f"<title>{title_line}</title>", text, count=1, flags=re.DOTALL)
    text, n_nav = re.subn(r'<nav class="lesson-nav">.*?</nav>', lambda _m: top, text, count=1, flags=re.DOTALL)
    text, n_kick = re.subn(r'<p class="kicker">.*?</p>', lambda _m: f'<p class="kicker">{kicker}</p>', text, count=1, flags=re.DOTALL)
    text, n_foot = re.subn(r'<footer class="lesson-nav">.*?</footer>', lambda _m: foot, text, count=1, flags=re.DOTALL)
    text, n_theme = _apply_theme_nav(text, theme_nav)

    missing = [name for name, count in (("title", n_title), ("nav", n_nav), ("kicker", n_kick), ("footer", n_foot), ("theme-nav", n_theme)) if count == 0]
    if missing:
        logger.warning("%s: could not find %s", lesson.file, ", ".join(missing))
    path.write_text(text, encoding="utf-8")
    logger.info("Renumbered %s -> %s", lesson.file, lesson.number)


# --- Contents (index.html) -------------------------------------------------

def render_lessons_html(course: Course) -> str:
    """Render the contents list grouped under a heading per (non-empty) theme."""
    lines: list[str] = []
    for theme in course.themes:
        lessons = _theme_lessons(course, theme.key)
        if not lessons:
            continue
        lines.append(f'{LESSON_HTML_INDENT}<section class="theme-group">')
        lines.append(f"    <h3>{_esc(theme.title)}</h3>")
        lines.append("    <ul>")
        for lesson in lessons:
            href = f"{course.lessons_dir}/{lesson.file}"
            if lesson.subcards:
                lines.append(f'      <li><a href="{href}">{_esc(lesson.display)}</a>')
                lines.append("        <ul>")
                for sub in lesson.subcards:
                    sub_href = f"{course.lessons_dir}/{sub.file}"
                    lines.append(f'          <li><a href="{sub_href}">{_esc(sub.display)}</a></li>')
                lines.append("        </ul>")
                lines.append("      </li>")
            else:
                lines.append(f'      <li><a href="{href}">{_esc(lesson.display)}</a></li>')
        lines.append("    </ul>")
        lines.append(f"{LESSON_HTML_INDENT}</section>")
    return "\n".join(lines)


def _theme_lessons(course: Course, theme_key: str) -> list[Lesson]:
    return [lesson for lesson in course.lessons if lesson.theme == theme_key]


def _manual_cell_html(course: Course, theme: Theme) -> str:
    entries: list[str] = []
    for lesson in _theme_lessons(course, theme.key):
        href = f"{course.lessons_dir}/{lesson.file}"
        entries.append(f'✅ <a href="{href}">{_esc(lesson.number)} {_esc(lesson.grid_label)}</a>')
        for sub in lesson.subcards:
            sub_href = f"{course.lessons_dir}/{sub.file}"
            entries.append(f'↳ ✅ <a href="{sub_href}">{_esc(sub.number)} {_esc(sub.grid_label)}</a>')
    entries.extend(_esc(note) for note in theme.notes)

    body_lines = []
    for i, entry in enumerate(entries):
        suffix = "<br>" if i < len(entries) - 1 else ""
        body_lines.append(f"{MANUAL_CELL_INDENT}{entry}{suffix}")
    body = "\n".join(body_lines)
    return f'        <td class="locked">\n{body}\n        </td>'


def render_grid_html(course: Course) -> str:
    head_cells = "".join(f"        <th>{_esc(h)}</th>\n" for h in course.rung_short)
    rows = []
    for theme in course.themes:
        manual = _manual_cell_html(course, theme)
        rung_cells = "".join(f"        <td>{_esc(r)}</td>\n" for r in theme.rungs)
        rows.append(
            "      <tr>\n"
            f"        <th>{_esc(theme.title)}</th>\n"
            f"{manual}\n"
            f"{rung_cells}"
            "      </tr>"
        )
    body = "\n".join(rows)
    return (
        f'{LESSON_HTML_INDENT}<table class="grid">\n'
        "    <thead>\n"
        "      <tr>\n"
        f"        <th>{_esc(course.rung_corner)}</th>\n"
        f"{head_cells}"
        "      </tr>\n"
        "    </thead>\n"
        "    <tbody>\n"
        f"{body}\n"
        "    </tbody>\n"
        f"{LESSON_HTML_INDENT}</table>"
    )


# --- Contents (CURRICULUM.md) ----------------------------------------------

def render_lessons_md(course: Course) -> str:
    """Render the Markdown contents grouped under a heading per (non-empty) theme."""
    lines: list[str] = []
    for theme in course.themes:
        lessons = _theme_lessons(course, theme.key)
        if not lessons:
            continue
        lines.append(f"### {theme.title}")
        lines.append("")
        for lesson in lessons:
            href = f"{course.lessons_dir}/{lesson.file}"
            lines.append(f"- [{lesson.display}]({href})")
            for sub in lesson.subcards:
                sub_href = f"{course.lessons_dir}/{sub.file}"
                lines.append(f"  - [{sub.display}]({sub_href})")
        lines.append("")
    return "\n".join(lines).rstrip()


def _manual_cell_md(course: Course, theme: Theme) -> str:
    entries: list[str] = []
    for lesson in _theme_lessons(course, theme.key):
        href = f"{course.lessons_dir}/{lesson.file}"
        entries.append(f"✅ [{lesson.number} {lesson.grid_label}]({href})")
        for sub in lesson.subcards:
            sub_href = f"{course.lessons_dir}/{sub.file}"
            entries.append(f"↳ ✅ [{sub.number} {sub.grid_label}]({sub_href})")
    entries.extend(theme.notes)
    return "; ".join(entries)


def render_grid_md(course: Course) -> str:
    header = "| " + " | ".join([course.rung_corner, *course.rung_long]) + " |"
    sep = "|" + "|".join(["---"] * (len(course.rung_long) + 1)) + "|"
    rows = [header, sep]
    for theme in course.themes:
        cells = [f"**{theme.title}**", _manual_cell_md(course, theme), *theme.rungs]
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join(rows)


# --- Region + link injection ----------------------------------------------

def replace_region(text: str, name: str, body: str) -> str:
    """Swap the content between ``BEGIN:auto:<name>`` and ``END:auto:<name>``."""
    pattern = re.compile(
        rf"([ \t]*)(<!-- BEGIN:auto:{re.escape(name)} -->)(.*?)([ \t]*)(<!-- END:auto:{re.escape(name)} -->)",
        re.DOTALL,
    )

    def _repl(match: re.Match[str]) -> str:
        indent = match.group(1)
        return f"{indent}{match.group(2)}\n{body}\n{indent}{match.group(5)}"

    new_text, count = pattern.subn(_repl, text)
    if count == 0:
        raise ValueError(f"Region markers for '{name}' not found")
    logger.info("Updated region '%s' (%d occurrence)", name, count)
    return new_text


def _update_start_link(text: str, course: Course) -> str:
    first = course.lessons[0]
    link = f'Start: <a href="{course.lessons_dir}/{first.file}">{_esc(first.nav_display)}</a>'
    new_text, count = re.subn(
        r'Start: <a href="[^"]+">[^<]*</a>', lambda _m: link, text
    )
    logger.info("Updated %d start link(s)", count)
    return new_text


def build(course_dir: Path) -> None:
    """Regenerate lesson pages and both contents files from ``course.json``."""
    course = load_course(course_dir / "course.json")
    lessons_root = course_dir / course.lessons_dir

    for index in range(len(course.spine)):
        render_lesson_page(course, index, lessons_root)

    index_path = course_dir / "index.html"
    index_text = index_path.read_text(encoding="utf-8")
    index_text = replace_region(index_text, "themenav", "  " + render_theme_nav(course, f"{course.lessons_dir}/"))
    index_text = replace_region(index_text, "lessons", render_lessons_html(course))
    index_text = replace_region(index_text, "grid", render_grid_html(course))
    index_text = _update_start_link(index_text, course)
    index_path.write_text(index_text, encoding="utf-8")
    logger.info("Wrote %s", index_path.name)

    md_path = course_dir / "CURRICULUM.md"
    md_text = md_path.read_text(encoding="utf-8")
    md_text = replace_region(md_text, "lessons", render_lessons_md(course))
    md_text = replace_region(md_text, "grid", render_grid_md(course))
    md_path.write_text(md_text, encoding="utf-8")
    logger.info("Wrote %s", md_path.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--course-dir",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Folder containing course.json, index.html, CURRICULUM.md and lessons/.",
    )
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    try:
        build(args.course_dir)
    except (OSError, ValueError, KeyError) as exc:
        logger.error("Contents build failed: %s", exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
