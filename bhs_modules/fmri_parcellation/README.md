# BrainHack School 2026: fMRI Parcellation Module Extension

## Module

This folder contains my completed and extended work for the BrainHack School fMRI Parcellation module.

The original module asks participants to run the parcellation notebook, retrieve three additional atlases using Nilearn datasets, visualize them, and answer the discussion question.

## Extension

I extended the module by creating an atlas audit script:

`scripts/atlas_audit_extension.py`

The script retrieves and compares four Nilearn atlases:

1. Schaefer 2018, 100 ROIs, 7 networks
2. Harvard-Oxford cortical maxprob 25%, 2mm
3. AAL SPM12
4. MSDL probabilistic atlas

For each atlas, the script reports:

- atlas family
- atlas type
- template information, when available
- image shape
- voxel size
- number of labels
- whether the atlas is deterministic or probabilistic
- practical notes for later ROI-based fMRI analysis

The script also saves visualizations for each atlas.

## Outputs

The generated outputs are:

- `outputs/atlas_audit_summary.csv`
- `outputs/atlas_audit_summary.json`
- atlas visualization figures in `figures/`

## Why this extension matters

Parcellation choice affects later fMRI analysis because the atlas defines the regions from which signals are extracted. A functional atlas such as Schaefer may be more suitable for connectivity or decoding workflows, while anatomical atlases such as Harvard-Oxford and AAL are easier to interpret anatomically. Probabilistic atlases such as MSDL require different handling from deterministic label atlases because their maps are 4D probability maps rather than a single 3D label image.

For my BrainHack School project, this extension connects the parcellation module with later BIDS/NiBabel-based quality control and possible ROI-based connectivity or decoding analysis.
