# BrainHack School 2026 Open Data Module

## Module

Open Data

## Dataset selected

For this module, I selected OpenNeuro dataset `ds002345`, the Narratives dataset.

This is an open BIDS-style fMRI dataset involving naturalistic auditory/language stimuli. I selected it because my BrainHack School project focuses on 
trial-wise or event-level task-fMRI metadata QC, and this dataset provides public BIDS metadata files that can be inspected without relying only on 
private lab data.

## Why this dataset fits the module

This dataset fits the BrainHack School Open Data module because it is an open neuroimaging dataset with participant-level metadata and BIDS-style task 
files.

For this exercise, I downloaded a small metadata-focused sample from the dataset, including:

- dataset-level metadata
- participant-level metadata
- subject-level scan metadata
- task event files for one participant

I chose not to download the full imaging `.nii.gz` files at this stage because my project focuses on metadata QC/reporting before deeper neuroimaging 
analysis.

## Why this dataset fits my BrainHack School project

My BrainHack School project focuses on building a configurable QC workflow for task-fMRI metadata. The main idea is to make the metadata layer 
inspectable and trustworthy before deeper analysis.

The motivating lab dataset for my project involves auditory/music fMRI and contains richer trial-wise metadata, such as stimulus information, decisions, 
and reaction times. However, because that dataset is private, I also need an open dataset to test whether my workflow can generalize to public BIDS-style 
data.

The Narratives dataset is useful for this purpose because it includes BIDS-style files such as:

- `participants.tsv`
- `sub-001_scans.tsv`
- task-level `events.tsv` files

These files allow me to test whether my workflow can inspect participant metadata, scan metadata, event timing, task labels, and missing values in a 
public dataset.

## Files downloaded

I downloaded the following files:

    data/openneuro_ds002345/dataset_description.json
    data/openneuro_ds002345/participants.json
    data/openneuro_ds002345/participants.tsv
    data/openneuro_ds002345/sub-001/sub-001_scans.json
    data/openneuro_ds002345/sub-001/sub-001_scans.tsv
    data/openneuro_ds002345/sub-001/func/sub-001_task-pieman_run-1_events.tsv
    data/openneuro_ds002345/sub-001/func/sub-001_task-pieman_run-2_events.tsv
    data/openneuro_ds002345/sub-001/func/sub-001_task-tunnel_events.tsv

## Initial inspection

I checked the downloaded files using:

    find data/openneuro_ds002345 -type f
    head data/openneuro_ds002345/participants.tsv
    head data/openneuro_ds002345/sub-001/sub-001_scans.tsv
    head data/openneuro_ds002345/sub-001/func/sub-001_task-pieman_run-1_events.tsv

The initial inspection showed that the dataset includes participant-level information:

    participant_id  age    sex  task           condition  comprehension
    sub-001         22,23  F,F  pieman,tunnel  n/a,n/a    n/a,n/a

It also includes subject-level scan information:

    filename                                      condition  comprehension
    anat/sub-001_T1w.nii.gz                       n/a        n/a
    func/sub-001_task-pieman_run-1_bold.nii.gz    n/a        n/a
    func/sub-001_task-pieman_run-2_bold.nii.gz    n/a        n/a
    func/sub-001_task-tunnel_bold.nii.gz          n/a        n/a

The event file includes BIDS-style timing information:

    onset  duration  trial_type  stim_file
    0.0    13.0      music       pieman_audio.wav
    15.0   422.0     story       pieman_audio.wav

## Important notes from initial inspection

For this module, I downloaded metadata files only, not the full imaging `.nii.gz` files. This choice fits my BrainHack School project because my workflow 
focuses on metadata QC and reporting before deeper neuroimaging analysis.

The selected open dataset is not structurally identical to the motivating lab dataset. The motivating lab dataset contains richer trial-wise information, 
including decisions and reaction times. In contrast, the OpenNeuro Narratives dataset contains BIDS-style event files with onset, duration, trial type, 
and stimulus file information.

Therefore, this open dataset is useful for testing general BIDS metadata inspection, but not for reproducing the full trial-wise behavioral QC logic from 
the motivating lab dataset.

One metadata feature noticed during inspection is that some participant-level fields contain comma-separated values. For example, `sub-001` has multiple 
values for age, sex, and task. This is not necessarily an error, but it is an important QC consideration because automated scripts may need to handle 
multi-value metadata fields carefully.

I used `sub-001` as a lightweight open-data validation sample. The goal was not to analyze the full dataset, but to identify whether public BIDS metadata 
files can serve as a test case for my configurable QC workflow.

## Relevance to metadata QC

This dataset can be used to test whether my QC workflow can inspect:

- required columns in BIDS event files
- onset and duration values
- task labels
- stimulus file labels
- participant-level metadata
- scan-level metadata
- missing values
- multi-value participant fields
- consistency between subject-level scan files and event files

## Connection to my planned workflow

In my project pitch, I proposed the following progression:

1. create synthetic demo metadata
2. run a configurable QC/reporting workflow
3. validate the workflow on an open BIDS task-fMRI dataset
4. later test the workflow on the motivating private lab dataset

This Open Data module supports step 3. It gives me a public dataset that can be used to test whether the workflow is reusable beyond one private project.

## Reflection

This module helped me connect my project idea to open science. Instead of only developing the QC workflow around private lab data, I can also test it on 
a public BIDS-style dataset.

The initial inspection also showed why metadata QC is useful. Even in a public BIDS dataset, metadata can contain features that require careful handling, 
such as comma-separated participant-level values and event files that describe long naturalistic segments rather than short trial-wise responses.

This makes the open dataset a useful test case for building a more flexible, configurable QC workflow.
