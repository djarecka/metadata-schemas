#!/usr/bin/env python3
"""
Keep index.html's intro paragraph(s) in sync with README.md.

The "intro" is whatever prose sits between the README's H1 title and its
first H2 section. index.html marks where that content goes with:

    <!-- readme-intro-start -->
    ...
    <!-- readme-intro-end -->

Usage:
    python scripts/sync_index_intro.py [README.md] [index.html]
"""

import html
import re
import sys
from pathlib import Path

START = "<!-- readme-intro-start -->"
END = "<!-- readme-intro-end -->"


def extract_intro_paragraphs(readme_text: str) -> list[str]:
    lines = readme_text.splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if start is None:
        return []
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    body = "\n".join(lines[start + 1:end]).strip()
    return [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]


def render_paragraphs(paragraphs: list[str]) -> str:
    return "\n".join(f"<p class=\"lead\">{html.escape(p)}</p>" for p in paragraphs)


def sync(readme_path: Path, index_path: Path) -> None:
    readme_text = readme_path.read_text(encoding="utf-8")
    paragraphs = extract_intro_paragraphs(readme_text)
    if not paragraphs:
        print(f"No intro paragraph found in {readme_path}; leaving {index_path} untouched.", file=sys.stderr)
        return

    index_html = index_path.read_text(encoding="utf-8")
    if START not in index_html or END not in index_html:
        print(f"Markers {START!r}/{END!r} not found in {index_path}; nothing to sync.", file=sys.stderr)
        return

    replacement = f"{START}\n{render_paragraphs(paragraphs)}\n{END}"
    updated = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        lambda _match: replacement,
        index_html,
        flags=re.DOTALL,
    )
    index_path.write_text(updated, encoding="utf-8")
    print(f"Synced intro from {readme_path} into {index_path}", file=sys.stderr)


def main() -> None:
    readme_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("README.md")
    index_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("index.html")
    sync(readme_path, index_path)


if __name__ == "__main__":
    main()
