# Task-fMRI Metadata QC Prototype

This repository contains a small prototype QC workflow for checking task-fMRI metadata and imaging/event file structure.

## Current prototype

The workflow currently performs OpenNeuro smoke tests using remote AWS S3 listings. It checks:

- dataset-level file inventory
- number of detected subjects
- number of BOLD files
- number of events.tsv files
- number of T1w anatomical files
- whether event files have matching BOLD files
- basic event-table content for selected lightweight events.tsv examples

## Open-data validation examples

Two OpenNeuro datasets were tested:

1. ds003720: music genre fMRI dataset
2. ds000007: stop-signal task dataset

The comparison focuses on workflow-level QC, not scientific analysis.

## Repository structure

- `scripts/`: Python QC scripts
- `configs/`: dataset-specific QC configuration examples
- `demo_data/`: small example events.tsv files only, not full imaging datasets
- `reports/`: generated QC reports and comparison summaries

## Example command

Run the smoke-test QC script on an OpenNeuro S3 listing:

    python scripts/qc_openneuro_listing.py \
      --listing reports/ds003720_s3_listing.txt \
      --out reports/ds003720_openneuro_smoke_test.md \
      --dataset "OpenNeuro ds003720 Music Genre fMRI Dataset"

## Current outputs

Generated reports include:

- `reports/ds003720_openneuro_smoke_test.md`
- `reports/ds003720_event_table_content_check.md`
- `reports/ds000007_openneuro_smoke_test.md`
- `reports/ds000007_event_table_content_check.md`
- `reports/open_data_qc_comparison.md`

## Next steps

Future extensions include:

- reading YAML config files directly
- adding nibabel-based NIfTI readability checks
- validating image shape, affine/header readability, and BOLD volume counts
- adding tests for validation functions
