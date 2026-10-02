#!/usr/bin/env bash
# Run from the repo root:  bash scripts/generate_all_schema_docs.sh
set -euo pipefail

SCRIPT="$(dirname "$0")/generate_schema_readme.py"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

cd "$ROOT"

python3 "$SCRIPT" \
  "docs/schemas/Cell-Annotation-and-Taxonomy/Cell Annotation" \
  --status "Approved BICAN Standard" \
  --version "1.0" \
  --owner "@UCDNJJ, @jeremymiller" \
  --date "10-03-2025"

python3 "$SCRIPT" \
  "docs/schemas/Library-Minimal-Metadata" \
  --related-model-label "Library Generation Model" \
  --related-model-url "https://brain-bican.github.io/models/index_library_generation/"

python3 "$SCRIPT" \
  "docs/schemas/Donor-Metadata/Donor_Metadata.csv" \
  --status "Endorsed BICAN Standard" \
  --version "1.0.0" \
  --date "2023-04-01" \
  --readme "docs/schemas/Donor-Metadata/README.md"

python3 "$SCRIPT" \
  "docs/schemas/Developing-Human-Metadata/Dev Human.csv" \
  --status "Accepted by MOWG" \
  --version "1.0.0" \
  --date "2024-07-08" \
  --readme "docs/schemas/Developing-Human-Metadata/README.md"

python3 "$SCRIPT" \
  "docs/schemas/Developing-NHP-Metadata/Dev NHP.csv" \
  --status "Accepted by MOWG" \
  --version "1.0.0" \
  --date "2024-07-08" \
  --readme "docs/schemas/Developing-NHP-Metadata/README.md"

python3 "$SCRIPT" \
  "docs/schemas/Developing-Tissue-Metadata/Dev Tissue.csv" \
  --status "Accepted by MOWG" \
  --version "1.0.0" \
  --date "2024-07-08" \
  --readme "docs/schemas/Developing-Tissue-Metadata/README.md"

python3 "$SCRIPT" \
  "docs/schemas/Institutional-Certification/IC_Metadata_Schema.csv" \
  --status "Endorsed BICAN Standard" \
  --version "1.0.0" \
  --date "2024-08-07" \
  --readme "docs/schemas/Institutional-Certification/README.md"

python3 "$SCRIPT" \
  "docs/schemas/Macaque-Metadata/HMBA_Macaque_WB_Omics_Spatial.csv" \
  --status "Accepted by MOWG" \
  --version "1.0.0" \
  --date "2024-07-08" \
  --readme "docs/schemas/Macaque-Metadata/README.md" \
  --section-key "wb-omics-spatial" \
  --section-title "WB Omics Spatial properties"

python3 "$SCRIPT" \
  "docs/schemas/Macaque-Metadata/HMBA_Macaque_Population.csv" \
  --status "Accepted by MOWG" \
  --version "1.0.0" \
  --date "2024-07-08" \
  --readme "docs/schemas/Macaque-Metadata/README.md" \
  --section-key "population" \
  --section-title "Population properties"

python3 "$SCRIPT" \
  "docs/schemas/Macaque-Metadata/HMBA_Macaque_Patchseq.csv" \
  --status "Accepted by MOWG" \
  --version "1.0.0" \
  --date "2024-07-08" \
  --readme "docs/schemas/Macaque-Metadata/README.md" \
  --section-key "patchseq" \
  --section-title "Patchseq properties"

# Cell-Taxonomy comes from a schemasheets Slots tab (fetched by
# fetch_schema_tables.yaml), not a BICAN field table, so only the columns that
# map obviously are rendered: slot -> Property, Data Type, Nullable -> Required,
# Alias -> Aliases, Definition -> Description. Its remaining columns
# (AIT Location, Source, Notes, New, from_schema) have no equivalent here and
# BICAN UUID / Data Example / Min / Max / Unit are absent from the tab, so the
# detail blocks simply omit them. See the column-vocabulary note before
# extending this.
python3 "$SCRIPT" \
  "docs/schemas/Cell-Taxonomy/Cell-Taxonomy.csv" \
  --readme "docs/schemas/Cell-Taxonomy/README.md" \
  --related-model-label "Cell Taxonomy Model" \
  --related-model-url "https://brain-bican.github.io/models/index_cell_taxonomy/"

# NOTE: the old project-registration-biccn skip comment was removed here. That
# directory no longer exists -- the refactoring merge replaced it with
# BICAN-Project-Registration, whose CSVs use the standard column vocabulary
# (Proposed BICAN Field Name, BICAN UUID, LinkML Class, Definition, ...), so it
# could be wired in without new mapping work. Not done yet.

python3 "$(dirname "$SCRIPT")/sync_index_intro.py" README.md docs/index.md

echo "Done."
