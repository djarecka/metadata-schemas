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

python3 "$SCRIPT" \
  "docs/schemas/Donor-Metadata/donor-metadata.csv" \
  --title "Human Donor Metadata" \
  --status "Endorsed BICAN Standard" \
  --version "1.0.0" \
  --date "2023-04-01" \
  --output "docs/schemas/Donor-Metadata/schema.html" \
  --readme "docs/schemas/Donor-Metadata/README.md"

python3 "$SCRIPT" \
  "docs/schemas/Developing-Human-Metadata/Dev Human.csv" \
  --title "Developing Human Metadata" \
  --status "Accepted by MOWG" \
  --version "1.0.0" \
  --date "2024-07-08" \
  --output "docs/schemas/Developing-Human-Metadata/schema.html" \
  --readme "docs/schemas/Developing-Human-Metadata/README.md"

python3 "$SCRIPT" \
  "docs/schemas/Developing-NHP-Metadata/Dev NHP.csv" \
  --title "Developing NHP Metadata" \
  --status "Accepted by MOWG" \
  --version "1.0.0" \
  --date "2024-07-08" \
  --output "docs/schemas/Developing-NHP-Metadata/schema.html" \
  --readme "docs/schemas/Developing-NHP-Metadata/README.md"

python3 "$SCRIPT" \
  "docs/schemas/Developing-Tissue-Metadata/Dev Tissue.csv" \
  --title "Developing Tissue Metadata" \
  --status "Accepted by MOWG" \
  --version "1.0.0" \
  --date "2024-07-08" \
  --output "docs/schemas/Developing-Tissue-Metadata/schema.html" \
  --readme "docs/schemas/Developing-Tissue-Metadata/README.md"

python3 "$SCRIPT" \
  "docs/schemas/Institutional-Certification/IC_Metadata_Schema.csv" \
  --title "Institutional Certification Metadata" \
  --status "Endorsed BICAN Standard" \
  --version "1.0.0" \
  --date "2024-08-07" \
  --output "docs/schemas/Institutional-Certification/schema.html" \
  --readme "docs/schemas/Institutional-Certification/README.md"

python3 "$SCRIPT" \
  "docs/schemas/Macaque-Donor-and-Tissue-Metadata/HMBA_Macaque_WB_Omics_Spatial.csv" \
  --title "HMBA Macaque WB Omics Spatial" \
  --status "Accepted by MOWG" \
  --version "1.0.0" \
  --date "2024-07-08" \
  --output "docs/schemas/Macaque-Donor-and-Tissue-Metadata/schema-wb-omics-spatial.html" \
  --readme "docs/schemas/Macaque-Donor-and-Tissue-Metadata/README.md" \
  --section-key "wb-omics-spatial" \
  --section-title "WB Omics Spatial properties"

python3 "$SCRIPT" \
  "docs/schemas/Macaque-Donor-and-Tissue-Metadata/HMBA_Macaque_Population.csv" \
  --title "HMBA Macaque Population" \
  --status "Accepted by MOWG" \
  --version "1.0.0" \
  --date "2024-07-08" \
  --output "docs/schemas/Macaque-Donor-and-Tissue-Metadata/schema-population.html" \
  --readme "docs/schemas/Macaque-Donor-and-Tissue-Metadata/README.md" \
  --section-key "population" \
  --section-title "Population properties"

python3 "$SCRIPT" \
  "docs/schemas/Macaque-Donor-and-Tissue-Metadata/HMBA_Macaque_Patchseq.csv" \
  --title "HMBA Macaque Patchseq" \
  --status "Accepted by MOWG" \
  --version "1.0.0" \
  --date "2024-07-08" \
  --output "docs/schemas/Macaque-Donor-and-Tissue-Metadata/schema-patchseq.html" \
  --readme "docs/schemas/Macaque-Donor-and-Tissue-Metadata/README.md" \
  --section-key "patchseq" \
  --section-title "Patchseq properties"

# project-registration-biccn intentionally skipped: its CSVs (Field, Data Type,
# Required, Description) use a different column layout than generate_schema_html.py
# expects (Proposed BICAN Field Name, LinkML Class, BICAN UUID, Nullable, ...),
# so it needs its own column-mapping support before it can be wired in here.

echo "Done."
