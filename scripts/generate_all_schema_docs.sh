#!/usr/bin/env bash
# Run from the repo root:  bash scripts/generate_all_schema_docs.sh
set -euo pipefail

SCRIPT="$(dirname "$0")/generate_schema_html.py"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

cd "$ROOT"

python3 "$SCRIPT" \
  "docs/schemas/Cell-Annotation-and-Taxonomy/Cell Annotation" \
  --title "Cell Annotation Schema" \
  --status "Approved BICAN Standard" \
  --version "1.0" \
  --owner "@UCDNJJ, @jeremymiller" \
  --date "10-03-2025"

python3 "$SCRIPT" \
  "docs/schemas/Library-Minimal-Metadata"

# Add more schema directories here:
#
# python3 "$SCRIPT" \
#   "docs/schemas/Donor-Metadata" \
#   --title "Donor Metadata Schema"

echo "Done."
