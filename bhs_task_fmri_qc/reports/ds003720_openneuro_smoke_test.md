# OpenNeuro ds003720 Music Genre fMRI Dataset Smoke-test QC Report

## Scope

This is a remote file-inventory smoke test based on an AWS S3 listing. It checks file presence and BIDS-like matching between event files and BOLD files. It does not download or validate NIfTI image integrity.

## Dataset-level summary

- Total files listed: 287
- Subjects detected: 5
- dataset_description.json found: PASS
- participants.tsv found: WARNING

## Image and event inventory

- BOLD NIfTI files: 90
- BOLD JSON sidecars: 90
- events.tsv files: 90
- T1w anatomical files: 5
- Fieldmap-related files: 0

## Directory/modality counts

- func: 270
- anat: 10
- other/root: 7

## Cross-check: events × BOLD

- Event bases detected: 90
- BOLD bases detected: 90
- Events without matching BOLD: 0
- BOLD without matching events: 0

## Warnings

- WARNING: participants.tsv not found.

## Next step

Download a small subset, such as one subject/run, then add NIfTI readability checks with nibabel: shape, affine/header readability, voxel size, and number of BOLD volumes.