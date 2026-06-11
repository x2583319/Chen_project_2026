# OpenNeuro ds000007 Stop-signal Task Dataset Smoke-test QC Report

## Scope

This is a remote file-inventory smoke test based on an AWS S3 listing. It checks file presence and BIDS-like matching between event files and BOLD files. It does not download or validate NIfTI image integrity.

## Dataset-level summary

- Total files listed: 492
- Subjects detected: 20
- dataset_description.json found: PASS
- participants.tsv found: PASS

## Image and event inventory

- BOLD NIfTI files: 118
- BOLD JSON sidecars: 122
- events.tsv files: 118
- T1w anatomical files: 20
- Fieldmap-related files: 0

## Directory/modality counts

- func: 355
- anat: 80
- other/root: 57

## Cross-check: events × BOLD

- Event bases detected: 118
- BOLD bases detected: 118
- Events without matching BOLD: 0
- BOLD without matching events: 0

## Warnings

- PASS: No major file-inventory warnings detected in this smoke test.

## Next step

Download a small subset, such as one subject/run, then add NIfTI readability checks with nibabel: shape, affine/header readability, voxel size, and number of BOLD volumes.