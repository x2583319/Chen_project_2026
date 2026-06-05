# BrainHack School 2026: BIDS Module Extension

## Module

This folder contains my completed and extended work for the BrainHack School BIDS module.

The module introduces the Brain Imaging Data Structure (BIDS), a standardized way to organize neuroimaging datasets and their metadata.

## Extension

I extended the module by creating a minimal synthetic BIDS dataset and validating it with the BIDS Validator.

The extension includes:

- a synthetic BIDS dataset
- a dataset-level `dataset_description.json`
- a `participants.tsv` file
- a `participants.json` data dictionary
- a synthetic task events file
- an events sidecar JSON file
- a dataset-level `README`
- saved BIDS Validator output

## Synthetic dataset

The synthetic dataset is stored in:

`synthetic_bids/`

It contains one synthetic participant:

`sub-01`

and one synthetic auditory/music listening task:

`task-listening`

The events file is:

`synthetic_bids/sub-01/func/sub-01_task-listening_events.tsv`

The corresponding events metadata file is:

`synthetic_bids/sub-01/func/sub-01_task-listening_events.json`

## Validation

The dataset was checked using the BIDS Validator through `npx`:

`npx bids-validator bhs_modules/bids/synthetic_bids`

The validation output was saved to:

`outputs/bids_validator_output.txt`

## About this extension

This extension focuses on practicing the logic of BIDS organization rather than analyzing real neuroimaging data. Creating a small synthetic dataset makes it easier to check whether required files, tabular metadata, sidecar JSON files, and event descriptions are organized correctly.

This connects to later fMRI quality-control work because BIDS-compatible structure and metadata are necessary before running preprocessing, checking events, extracting trial-level information, or connecting imaging files with behavioral/task variables.
