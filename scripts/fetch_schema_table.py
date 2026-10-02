#!/usr/bin/env python3
"""Fetch a schema table from a Google Sheet tab and save it as CSV.

Each schema gets one config file under ``config/schemas/``:

    schema_name: Cell-Taxonomy          # -> docs/schemas/Cell-Taxonomy/
    gsheet_id: "1AC-jt..."
    tab:
      name: Slots
      gid: "2096406242"
    output: Cell-Taxonomy.csv           # optional; defaults to <schema_name>.csv
    version: "2026-10-02"               # optional; bump to force a refresh

The tab is exported unauthenticated, so the sheet must be link-shared
("anyone with the link can view").

Schemasheets directive rows -- the ones whose first cell starts with ``>`` --
are dropped; the real header row and the data rows are kept. The count of
directive rows is NOT assumed: it varies by tab (1 for Prefixes/Subsets/
ValueSets, 2 for Slots/Classes/Relations/Schema), so every leading ``>`` row is
removed rather than a fixed number of lines.

Usage:
    python3 scripts/fetch_schema_table.py --all
    python3 scripts/fetch_schema_table.py --schema Cell-Taxonomy
    python3 scripts/fetch_schema_table.py --config config/schemas/foo.yaml
"""

from __future__ import annotations

import argparse
import csv
import io
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / "config" / "schemas"
SCHEMA_DIR = ROOT / "docs" / "schemas"

EXPORT_URL = "https://docs.google.com/spreadsheets/d/{gsheet_id}/export?format=csv&gid={gid}"

REQUIRED_KEYS = ("schema_name", "gsheet_id", "tab")


class ConfigError(Exception):
    """A config file is missing something or says something impossible."""


def load_config(path: Path) -> dict:
    """Read one config file and check it has what we need."""
    try:
        cfg = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ConfigError(f"{path}: not valid YAML: {exc}") from exc

    if not isinstance(cfg, dict):
        raise ConfigError(f"{path}: expected a mapping at the top level")

    missing = [k for k in REQUIRED_KEYS if not cfg.get(k)]
    if missing:
        raise ConfigError(f"{path}: missing required key(s): {', '.join(missing)}")

    tab = cfg["tab"]
    if not isinstance(tab, dict) or not tab.get("gid"):
        raise ConfigError(f"{path}: 'tab' must be a mapping with a 'gid'")

    name = cfg["schema_name"]
    if "/" in name or name in (".", ".."):
        raise ConfigError(f"{path}: schema_name {name!r} must be a single directory name")

    cfg["_path"] = path
    return cfg


def download_csv(gsheet_id: str, gid: str) -> str:
    """Export one tab as CSV text."""
    url = EXPORT_URL.format(gsheet_id=gsheet_id, gid=gid)
    try:
        with urllib.request.urlopen(url, timeout=60) as resp:
            raw = resp.read()
            content_type = resp.headers.get("Content-Type", "")
    except urllib.error.HTTPError as exc:
        raise ConfigError(
            f"export failed with HTTP {exc.code} for gid={gid}. "
            "Check the gsheet_id/gid, and that the sheet is link-shared."
        ) from exc
    except urllib.error.URLError as exc:
        raise ConfigError(f"could not reach Google Sheets: {exc.reason}") from exc

    # A sheet that is not link-shared answers 200 with a sign-in HTML page.
    # Writing that to a .csv would look like success, so refuse it explicitly.
    if "text/csv" not in content_type:
        raise ConfigError(
            f"expected text/csv for gid={gid} but got {content_type!r}. "
            "The sheet is most likely not shared as 'anyone with the link can view'."
        )

    return raw.decode("utf-8")


def strip_directive_rows(text: str) -> tuple[list[list[str]], int]:
    """Drop every row whose first cell starts with '>'. Returns (rows, dropped)."""
    rows = list(csv.reader(io.StringIO(text)))
    kept = [r for r in rows if not (r and r[0].lstrip().startswith(">"))]
    return kept, len(rows) - len(kept)


def write_csv(rows: list[list[str]], dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", newline="", encoding="utf-8") as fh:
        csv.writer(fh, lineterminator="\n").writerows(rows)


def fetch(cfg: dict) -> Path:
    name = cfg["schema_name"]
    tab = cfg["tab"]
    output = cfg.get("output") or f"{name}.csv"
    dest = SCHEMA_DIR / name / output

    text = download_csv(str(cfg["gsheet_id"]), str(tab["gid"]))
    rows, dropped = strip_directive_rows(text)

    if not rows:
        raise ConfigError(f"{cfg['_path']}: tab gid={tab['gid']} produced no rows after stripping")
    if len(rows) < 2:
        raise ConfigError(
            f"{cfg['_path']}: tab gid={tab['gid']} left only a header row -- no data. "
            "Check the gid points at the intended tab."
        )

    write_csv(rows, dest)
    rel = dest.relative_to(ROOT)
    print(
        f"{name}: tab {tab.get('name', tab['gid'])} -> {rel} "
        f"({len(rows) - 1} data rows, {len(rows[0])} columns, {dropped} directive row(s) dropped)"
    )
    return dest


def collect_configs(args: argparse.Namespace) -> list[dict]:
    if args.config:
        paths = [Path(args.config)]
    else:
        if not CONFIG_DIR.is_dir():
            raise ConfigError(f"no config directory at {CONFIG_DIR.relative_to(ROOT)}")
        paths = sorted(p for p in CONFIG_DIR.iterdir() if p.suffix in (".yaml", ".yml"))
        if not paths:
            raise ConfigError(f"no .yaml config files in {CONFIG_DIR.relative_to(ROOT)}")

    configs = [load_config(p) for p in paths]

    if args.schema:
        configs = [c for c in configs if c["schema_name"] == args.schema]
        if not configs:
            known = ", ".join(sorted(load_config(p)["schema_name"] for p in paths))
            raise ConfigError(f"no config with schema_name {args.schema!r}. Known: {known}")

    return configs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true", help="fetch every config in config/schemas/")
    group.add_argument("--schema", help="fetch only the config with this schema_name")
    group.add_argument("--config", help="fetch this one config file")
    args = parser.parse_args()

    try:
        configs = collect_configs(args)
    except ConfigError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    failures = 0
    for cfg in configs:
        try:
            fetch(cfg)
        except ConfigError as exc:
            print(f"error: {cfg['schema_name']}: {exc}", file=sys.stderr)
            failures += 1

    if failures:
        print(f"{failures} of {len(configs)} schema(s) failed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
