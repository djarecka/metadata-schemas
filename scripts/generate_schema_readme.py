#!/usr/bin/env python3
"""
Generate a "Schema properties" section in a README.md from a BICAN schema CSV.

The section is rendered by MkDocs (see mkdocs.yml) as part of the schema's
documentation page, so this script only ever writes Markdown/HTML into the
README — it does not produce a separate HTML page.

Usage (file):
    python generate_schema_readme.py <csv_file> --readme README.md \
        [--status "Approved"] [--version "1.0"] [--owner "@someone"] [--date "2025-01-01"] \
        [--description "..."] \
        [--section-key entity-name] [--section-title "Entity properties"] \
        [--related-model-label "Some Model"] [--related-model-url "https://..."]

Usage (directory — auto-discovers CSV and README.md):
    python generate_schema_readme.py <schema_dir>
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
    return _get(row, "Proposed BICAN Field Name", "Proposed BICAN Field", "BICAN Field Name")


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


def anchor_id(name: str) -> str:
    return name.strip().replace(" ", "-").replace("[", "").replace("]", "").lower()


def e(text: str) -> str:
    """HTML-escape a string."""
    return html_module.escape(text)


def cell(text: str) -> str:
    """Escape a value for use inside a Markdown table cell."""
    return e(text).replace("|", "\\|")


# ---------------------------------------------------------------------------
# README section generation
# ---------------------------------------------------------------------------

def readme_markers(section_key: str = "") -> tuple[str, str]:
    """Start/end marker pair for a README section. A bare key reproduces the
    original single-section markers, so existing single-CSV schemas are unaffected."""
    suffix = f":{section_key}" if section_key else ""
    return f"<!-- schema-properties-start{suffix} -->", f"<!-- schema-properties-end{suffix} -->"


def build_readme_section(
    rows: list[dict],
    section_key: str = "",
    section_title: str = "Schema properties",
    description: str = "",
    status: str = "",
    version: str = "",
    owner: str = "",
    date: str = "",
    related_model_label: str = "",
    related_model_url: str = "",
) -> str:
    """Return the Markdown+HTML content for a '## <section_title>' section."""
    lines: list[str] = []
    readme_start, readme_end = readme_markers(section_key)

    def w(s: str) -> None:
        lines.append(s)

    ordered_keys, groups = group_rows(rows)

    w(readme_start + "\n")
    w(f"## {section_title}\n")
    w("*Auto-generated from CSV. Do not edit this section manually.*\n")

    meta_items = [("Status", status), ("Version", version), ("Owner", owner), ("Date", date)]
    active_meta = [(k, v) for k, v in meta_items if v]
    if active_meta:
        w("\n" + " &middot; ".join(f"**{k}:** {e(v)}" for k, v in active_meta) + "\n")

    if description:
        w(f"\n{e(description)}\n")

    if related_model_label and related_model_url:
        w(f"\n**Related LinkML model:** [{related_model_label}]({related_model_url})\n")

    w("\n### Properties\n")

    for cls in ordered_keys:
        if cls:
            w(f"\n#### {cls}\n")

        w("\n| Property | Type | Required | Aliases | Description |\n")
        w("|----------|------|----------|---------|-------------|\n")

        for row in groups[cls]:
            name = _field_name(row)
            dtype = _get(row, "Data Type") or "—"
            nullable = _get(row, "Nullable", "nullable")
            required = "yes" if nullable.upper() == "FALSE" else "no"
            aliases = _get(row, "Aliases") or "—"
            definition = _get(row, "Definition", "definition", "Description")
            short_def = definition[:120] + "…" if len(definition) > 120 else definition
            aid = anchor_id(name)
            w(f"| [`{cell(name)}`](#{aid}) | {cell(dtype)} | {required} | {cell(aliases)} | {cell(short_def)} |\n")

    w("\n### Property Details\n")

    for cls in ordered_keys:
        if cls:
            w(f"\n#### {cls}\n")

        for row in groups[cls]:
            name = _field_name(row)
            dtype = _get(row, "Data Type")
            nullable = _get(row, "Nullable", "nullable")
            required = nullable.upper() == "FALSE"
            aliases = _get(row, "Aliases")
            definition = _get(row, "Definition", "definition", "Description")
            uuid = _get(row, "BICAN UUID")
            permissible = _get(row, "Permissible Values")
            example = _get(row, "Data Example")
            min_val = _get(row, "Min Value", "min value")
            max_val = _get(row, "Max Value", "max value")
            unit = _get(row, "Unit")
            subsets = _get(row, "Subsets")
            aid = anchor_id(name)
            req_label = "required" if required else "optional"

            w(f'\n<div id="{e(aid)}" class="field-detail">\n')
            w(f"<h5><code>{e(name)}</code> <em>({req_label})</em></h5>\n")
            w("<ul>\n")
            if uuid:
                w(f"<li><strong>BICAN UUID:</strong> <code>{e(uuid)}</code></li>\n")
            if dtype:
                w(f"<li><strong>Data Type:</strong> <code>{e(dtype)}</code></li>\n")
            if aliases:
                w(f"<li><strong>Aliases:</strong> {e(aliases)}</li>\n")
            if subsets:
                w(f"<li><strong>Subsets:</strong> {e(subsets)}</li>\n")
            if example:
                w(f"<li><strong>Example:</strong> <code>{e(example)}</code></li>\n")
            if min_val or max_val:
                rng = f"{min_val or '—'} – {max_val or '—'}"
                if unit:
                    rng += f" {unit}"
                w(f"<li><strong>Range:</strong> {e(rng)}</li>\n")
            w("</ul>\n")
            w(f"<p>{e(definition)}</p>\n")

            if permissible:
                values = [v.strip() for v in permissible.split(",") if v.strip()]
                if values:
                    joined = ", ".join(f"<code>{e(v)}</code>" for v in values)
                    w(f"<p><strong>Permissible values:</strong> {joined}</p>\n")

            w("</div>\n")

    w("\n" + readme_end + "\n")
    return "".join(lines)


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
            lambda _match: section_content.rstrip("\n"),
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
        description="Generate a 'Schema properties' README section from a BICAN schema CSV."
    )
    parser.add_argument(
        "input",
        help="Path to a schema CSV file, or a directory containing one (auto-discovers CSV and README.md).",
    )
    parser.add_argument("--description", default="", help="Short schema description")
    parser.add_argument("--status", default="", help="Document status (e.g. Approved BICAN Standard)")
    parser.add_argument("--version", default="", help="Schema version")
    parser.add_argument("--owner", default="", help="Schema owner(s)")
    parser.add_argument("--date", default="", help="Date created")
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
    parser.add_argument(
        "--related-model-label", default="",
        help="Display name of a corresponding LinkML model in brain-bican/models, e.g. 'Library Generation Model'.",
    )
    parser.add_argument(
        "--related-model-url", default="",
        help="URL of the corresponding LinkML model's docs page. Both --related-model-label and "
             "--related-model-url must be set together.",
    )
    args = parser.parse_args()

    input_path = Path(args.input)

    # Resolve CSV path and apply directory-mode defaults
    if input_path.is_dir():
        schema_dir = input_path
        csv_path = find_csv(schema_dir)
        if not args.readme:
            readme = schema_dir / "README.md"
            if readme.exists():
                args.readme = str(readme)
    else:
        csv_path = input_path

    if not args.readme:
        sys.exit("error: --readme is required (or run in directory mode against a folder with a README.md)")

    print(f"Using CSV: {csv_path}", file=sys.stderr)

    _, rows = read_csv(str(csv_path))

    section = build_readme_section(
        rows,
        section_key=args.section_key,
        section_title=args.section_title,
        description=args.description,
        status=args.status,
        version=args.version,
        owner=args.owner,
        date=args.date,
        related_model_label=args.related_model_label,
        related_model_url=args.related_model_url,
    )
    update_readme(args.readme, section, section_key=args.section_key)
    print(f"README updated: {args.readme}", file=sys.stderr)


if __name__ == "__main__":
    main()
