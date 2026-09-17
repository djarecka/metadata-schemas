#!/usr/bin/env python3
"""
Generate schema documentation HTML from a CSV file, and optionally update a README.md.
Layout inspired by https://docs.hubmapconsortium.org/param-search/schema-sample.html

Usage (file):
    python generate_schema_html.py <csv_file> [--title "..."] [--description "..."] \
        [--output schema.html] [--readme README.md] \
        [--status "Approved"] [--version "1.0"] \
        [--owner "@someone"] [--date "2025-01-01"]

Usage (directory — auto-discovers CSV and README.md):
    python generate_schema_html.py <schema_dir> [--title "..."] [--output schema.html]
"""

import csv
import argparse
import html as html_module
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# CSV helpers
# ---------------------------------------------------------------------------

def find_csv(directory: Path) -> Path:
    """Find the primary schema CSV in a directory.

    Prefers files without 'upd' in the name; falls back to any CSV found.
    """
    csvs = sorted(directory.glob("*.csv"))
    if not csvs:
        raise FileNotFoundError(f"No CSV files found in {directory}")
    preferred = [p for p in csvs if "upd" not in p.name.lower()]
    return preferred[0] if preferred else csvs[0]


def read_csv(csv_path: str) -> tuple[list[str], list[dict]]:
    """Return (fieldnames, rows) from a CSV, handling BOM and stripping whitespace."""
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = [k.strip() for k in (reader.fieldnames or [])]
        rows = []
        for raw in reader:
            rows.append({k.strip(): (v or "").strip() for k, v in raw.items()})
    return fieldnames, rows


def _get(row: dict, *keys: str) -> str:
    """Return the first non-empty value matching any key (case-insensitive)."""
    lower = {k.lower(): v for k, v in row.items()}
    for key in keys:
        v = lower.get(key.lower(), "")
        if v:
            return v
    return ""


# Convenience wrappers for columns that have known name variants across CSVs.

def _field_name(row: dict) -> str:
    return _get(row, "Proposed BICAN Field Name", "Proposed BICAN Field")


def _linkml_class(row: dict) -> str:
    return _get(row, "LinkML Class", "LinkML Class Name")


# ---------------------------------------------------------------------------
# Shared grouping logic
# ---------------------------------------------------------------------------

def group_rows(rows: list[dict]) -> tuple[list[str], dict[str, list[dict]]]:
    """Group rows by LinkML Class. Returns (ordered_keys, groups)."""
    groups: dict[str, list[dict]] = {}
    for row in rows:
        name = _field_name(row)
        if not name:
            continue
        cls = _linkml_class(row)
        groups.setdefault(cls, []).append(row)
    ordered_keys = sorted(groups.keys(), key=lambda k: ("" if k == "" else "~" + k))
    return ordered_keys, groups


# ---------------------------------------------------------------------------
# Anchor / ID helpers
# ---------------------------------------------------------------------------

def anchor_id(name: str) -> str:
    return name.strip().replace(" ", "-").replace("[", "").replace("]", "").lower()


def e(text: str) -> str:
    """HTML-escape a string."""
    return html_module.escape(text)


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

CSS = """
:root {
    color-scheme: light dark;
    --bg: #ffffff;
    --bg-alt: #f6f8fa;
    --text: #1a1a1a;
    --text-muted: #59636e;
    --border: #d8dee4;
    --accent: #0969da;
    --accent-bg: #ddf0ff;
    --req-bg: #ffe9e6; --req-text: #c5221f;
    --opt-bg: #e8f0fe; --opt-text: #1557b0;
    --type-bg: #e6f4ea; --type-text: #137333;
    --card-bg: #ffffff;
}
@media (prefers-color-scheme: dark) {
    :root {
        --bg: #0d1117;
        --bg-alt: #161b22;
        --text: #e6edf3;
        --text-muted: #8b949e;
        --border: #30363d;
        --accent: #4a9eff;
        --accent-bg: #10243e;
        --req-bg: #3d1f1c; --req-text: #ff8a80;
        --opt-bg: #16283f; --opt-text: #8ab4f8;
        --type-bg: #10321d; --type-text: #7ee787;
        --card-bg: #161b22;
    }
}
* { box-sizing: border-box; }
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, sans-serif;
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 24px 48px;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
}
.site-nav { display: flex; align-items: center; gap: 8px; padding: 16px 0;
            border-bottom: 1px solid var(--border); margin-bottom: 24px;
            font-size: 0.92em; color: var(--text-muted); }
.site-nav a { font-weight: 600; }

h1 { font-size: 1.9em; border-bottom: 3px solid var(--accent); padding-bottom: 10px; }
h2 { font-size: 1.3em; color: var(--accent); margin-top: 40px; border-bottom: 1px solid var(--border); padding-bottom: 6px; }
h3 { font-size: 1.05em; color: var(--text-muted); margin-top: 28px; }
p  { margin: 8px 0 14px; }
a  { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

.meta { background: var(--bg-alt); border: 1px solid var(--border); border-radius: 6px;
        padding: 10px 16px; margin: 12px 0 24px; display: flex; flex-wrap: wrap; gap: 10px 30px; }
.meta span { font-size: 0.88em; color: var(--text-muted); }
.meta span b { color: var(--text); }

table { border-collapse: collapse; width: 100%; margin: 14px 0 24px; font-size: 0.93em; }
th { background: var(--accent); color: #fff; padding: 9px 12px; text-align: left; font-weight: 600; }
td { padding: 8px 12px; border-bottom: 1px solid var(--border); vertical-align: top; }
tr:last-child td { border-bottom: none; }
tbody tr:hover { background: var(--bg-alt); }
td:first-child { white-space: nowrap; }

code { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
       background: var(--accent-bg); color: var(--accent); padding: 1px 5px; border-radius: 3px;
       font-size: 0.88em; }
.badge { display: inline-block; padding: 1px 8px; border-radius: 10px;
         font-size: 0.78em; font-weight: 600; white-space: nowrap; }
.req  { background: var(--req-bg); color: var(--req-text); }
.opt  { background: var(--opt-bg); color: var(--opt-text); }
.type { background: var(--type-bg); color: var(--type-text); font-family: monospace; }

.field-card { border: 1px solid var(--border); border-radius: 8px; padding: 18px 20px;
              margin: 12px 0; background: var(--card-bg); }
.field-card h3 { margin-top: 0; }
.field-card .props tr td:first-child { color: var(--text-muted); font-size: 0.85em;
                                        width: 140px; border-bottom: none; }
.field-card .props tr td:last-child  { border-bottom: none; }
.field-card .props { background: var(--bg-alt); border-radius: 4px; }

.enum-list { display: flex; flex-wrap: wrap; gap: 6px; margin: 6px 0; list-style: none; padding: 0; }
.enum-list li { background: var(--accent-bg); color: var(--accent); padding: 2px 10px;
                border-radius: 12px; font-family: monospace; font-size: 0.85em; }

.group-label { font-size: 0.8em; text-transform: uppercase; letter-spacing: 0.06em;
               color: var(--text-muted); margin-bottom: 4px; }
"""


def build_html(
    rows: list[dict],
    title: str,
    description: str = "",
    status: str = "",
    version: str = "",
    owner: str = "",
    date: str = "",
    home_link: str | None = None,
) -> str:
    out: list[str] = []

    def w(s: str) -> None:
        out.append(s)

    w(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)}</title>
<style>
{CSS}
</style>
</head>
<body>
""")

    if home_link:
        w(f'<nav class="site-nav"><a href="{e(home_link)}">&larr; All BICAN schemas</a></nav>\n')

    w(f'<h1>{e(title)}</h1>\n')

    meta_items = [("Document Status", status), ("Version", version), ("Owner", owner), ("Date", date)]
    active = [(k, v) for k, v in meta_items if v]
    if active:
        w('<div class="meta">\n')
        for k, v in active:
            w(f'  <span><b>{e(k)}:</b> {e(v)}</span>\n')
        w('</div>\n')

    if description:
        w(f'<p>{e(description)}</p>\n')

    ordered_keys, groups = group_rows(rows)

    w('<h2 id="properties">Properties</h2>\n')

    for cls in ordered_keys:
        if cls:
            w(f'<p class="group-label">{e(cls)}</p>\n')

        w('<table>\n<thead><tr>')
        w('<th>Property</th><th>Type</th><th>Required</th><th>Aliases</th><th>Description</th>')
        w('</tr></thead>\n<tbody>\n')

        for row in groups[cls]:
            name = _field_name(row)
            dtype = _get(row, "Data Type")
            nullable = _get(row, "Nullable", "nullable")
            required = nullable.upper() == "FALSE"
            aliases = _get(row, "Aliases")
            definition = _get(row, "Definition", "definition")
            aid = anchor_id(name)

            req_badge = (
                '<span class="badge req">required</span>'
                if required
                else '<span class="badge opt">optional</span>'
            )
            short_def = definition[:160] + "…" if len(definition) > 160 else definition

            w(f'<tr>')
            w(f'<td><a href="#{e(aid)}"><code>{e(name)}</code></a></td>')
            w(f'<td><span class="badge type">{e(dtype) if dtype else "—"}</span></td>')
            w(f'<td>{req_badge}</td>')
            w(f'<td>{e(aliases) if aliases else "—"}</td>')
            w(f'<td>{e(short_def)}</td>')
            w('</tr>\n')

        w('</tbody></table>\n')

    w('<h2 id="property-details">Property Details</h2>\n')

    for cls in ordered_keys:
        if cls:
            w(f'<h3>{e(cls)}</h3>\n')

        for row in groups[cls]:
            name = _field_name(row)
            dtype = _get(row, "Data Type")
            nullable = _get(row, "Nullable", "nullable")
            required = nullable.upper() == "FALSE"
            aliases = _get(row, "Aliases")
            definition = _get(row, "Definition", "definition")
            uuid = _get(row, "BICAN UUID")
            permissible = _get(row, "Permissible Values")
            example = _get(row, "Data Example")
            min_val = _get(row, "Min Value", "min value")
            max_val = _get(row, "Max Value", "max value")
            unit = _get(row, "Unit")
            subsets = _get(row, "Subsets")
            aid = anchor_id(name)

            req_badge = (
                '<span class="badge req">required</span>'
                if required
                else '<span class="badge opt">optional</span>'
            )

            w(f'<div class="field-card" id="{e(aid)}">\n')
            w(f'<h3><code>{e(name)}</code> {req_badge}</h3>\n')

            prop_rows = [("BICAN UUID", f"<code>{e(uuid)}</code>" if uuid else "—")]
            if dtype:
                prop_rows.append(("Data Type", f'<span class="badge type">{e(dtype)}</span>'))
            if aliases:
                prop_rows.append(("Aliases", e(aliases)))
            if subsets:
                prop_rows.append(("Subsets", e(subsets)))
            if example:
                prop_rows.append(("Example", f"<code>{e(example)}</code>"))
            if min_val or max_val:
                rng = f"{min_val or '—'} – {max_val or '—'}"
                if unit:
                    rng += f" {unit}"
                prop_rows.append(("Range", e(rng)))

            if prop_rows:
                w('<table class="props">\n')
                for pk, pv in prop_rows:
                    w(f'<tr><td>{e(pk)}</td><td>{pv}</td></tr>\n')
                w('</table>\n')

            w(f'<p>{e(definition)}</p>\n')

            if permissible:
                values = [v.strip() for v in permissible.split(",") if v.strip()]
                if values:
                    w('<p><strong>Permissible values:</strong></p>\n')
                    w('<ul class="enum-list">\n')
                    for v in values:
                        w(f'<li>{e(v)}</li>\n')
                    w('</ul>\n')

            w('</div>\n')

    w('</body>\n</html>\n')
    return "".join(out)


# ---------------------------------------------------------------------------
# README Markdown generation
# ---------------------------------------------------------------------------

def readme_markers(section_key: str = "") -> tuple[str, str]:
    """Start/end marker pair for a README section. A bare key reproduces the
    original single-section markers, so existing single-CSV schemas are unaffected."""
    suffix = f":{section_key}" if section_key else ""
    return f"<!-- schema-properties-start{suffix} -->", f"<!-- schema-properties-end{suffix} -->"


def build_readme_section(rows: list[dict], section_key: str = "", section_title: str = "Schema properties") -> str:
    """Return the Markdown content for a '## <section_title>' section."""
    lines: list[str] = []
    readme_start, readme_end = readme_markers(section_key)

    def w(s: str) -> None:
        lines.append(s)

    def cell(s: str) -> str:
        return s.replace("|", "\\|")

    ordered_keys, groups = group_rows(rows)

    w(readme_start + "\n")
    w(f"## {section_title}\n")
    w("*Auto-generated from CSV. Do not edit this section manually.*\n")

    for cls in ordered_keys:
        if cls:
            w(f"\n### {cls}\n")

        w("\n| Property | Type | Required | Description |\n")
        w("|----------|------|----------|-------------|\n")

        for row in groups[cls]:
            name = _field_name(row)
            dtype = _get(row, "Data Type") or "—"
            nullable = _get(row, "Nullable", "nullable")
            required = "yes" if nullable.upper() == "FALSE" else "no"
            definition = _get(row, "Definition", "definition")
            short_def = definition[:120] + "…" if len(definition) > 120 else definition
            w(f"| `{cell(name)}` | {cell(dtype)} | {required} | {cell(short_def)} |\n")

    w("\n" + readme_end + "\n")
    return "".join(lines)


def relative_root_link(output_path: str) -> str:
    """Relative path from an output HTML file's directory back to the repo-root index.html."""
    depth = len(Path(output_path).parent.parts)
    return ("../" * depth + "index.html") if depth else "index.html"


def update_readme(readme_path: str, section_content: str, section_key: str = "") -> None:
    """Insert or replace a Schema properties section in a README.md file.

    Sections are identified by section_key so multiple CSVs in the same
    folder (e.g. per-entity schemas) can each own a distinct section."""
    path = Path(readme_path)
    original = path.read_text(encoding="utf-8") if path.exists() else ""
    readme_start, readme_end = readme_markers(section_key)

    if readme_start in original and readme_end in original:
        # Replace between existing markers (inclusive)
        updated = re.sub(
            re.escape(readme_start) + r".*?" + re.escape(readme_end),
            section_content.rstrip("\n"),
            original,
            flags=re.DOTALL,
        )
    else:
        # Insert just before ## Changelog, or append if not found
        match = re.search(r"^## Changelog\b", original, flags=re.MULTILINE)
        if match:
            insert_at = match.start()
            updated = (
                original[:insert_at].rstrip("\n")
                + "\n\n"
                + section_content
                + "\n"
                + original[insert_at:]
            )
        else:
            updated = original.rstrip("\n") + "\n\n" + section_content

    path.write_text(updated, encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate schema documentation HTML from a BICAN CSV file or directory."
    )
    parser.add_argument(
        "input",
        help="Path to a schema CSV file, or a directory containing one (auto-discovers CSV and README.md).",
    )
    parser.add_argument("--title", default="", help="Page title (derived from directory name if omitted)")
    parser.add_argument("--description", default="", help="Short schema description")
    parser.add_argument("--status", default="", help="Document status (e.g. Approved BICAN Standard)")
    parser.add_argument("--version", default="", help="Schema version")
    parser.add_argument("--owner", default="", help="Schema owner(s)")
    parser.add_argument("--date", default="", help="Date created")
    parser.add_argument("--output", "-o", default=None, help="Output HTML file (default: schema.html next to CSV)")
    parser.add_argument("--readme", default=None, help="README.md to create/update (auto-detected in directory mode)")
    parser.add_argument(
        "--section-key", default="",
        help="Identifies this CSV's README section when a folder has multiple CSVs sharing one README "
             "(e.g. one entity per CSV). Leave unset for single-CSV schemas.",
    )
    parser.add_argument(
        "--section-title", default="Schema properties",
        help="Heading for the README section (default: 'Schema properties'; "
             "set per-CSV, e.g. 'Person properties', for multi-CSV schemas).",
    )
    args = parser.parse_args()

    input_path = Path(args.input)

    # Resolve CSV path and apply directory-mode defaults
    if input_path.is_dir():
        schema_dir = input_path
        csv_path = find_csv(schema_dir)
        if not args.output:
            args.output = str(schema_dir / "schema.html")
        if not args.readme:
            readme = schema_dir / "README.md"
            if readme.exists():
                args.readme = str(readme)
        if not args.title:
            args.title = schema_dir.name.replace("-", " ").replace("_", " ").title()
    else:
        csv_path = input_path
        if not args.title:
            args.title = csv_path.stem.replace("-", " ").replace("_", " ").title()

    print(f"Using CSV: {csv_path}", file=sys.stderr)

    _, rows = read_csv(str(csv_path))

    if args.output or not args.readme:
        content = build_html(
            rows,
            title=args.title,
            description=args.description,
            status=args.status,
            version=args.version,
            owner=args.owner,
            date=args.date,
            home_link=relative_root_link(args.output) if args.output else None,
        )
        if args.output:
            Path(args.output).write_text(content, encoding="utf-8")
            print(f"Written to {args.output}", file=sys.stderr)
        else:
            sys.stdout.write(content)

    if args.readme:
        section = build_readme_section(rows, section_key=args.section_key, section_title=args.section_title)
        update_readme(args.readme, section, section_key=args.section_key)
        print(f"README updated: {args.readme}", file=sys.stderr)


if __name__ == "__main__":
    main()
