# Open Data Metadata Check

Dataset: OpenNeuro ds002345

This report summarizes the metadata files downloaded for the BrainHack School Open Data module.

## participants.tsv

Number of participant rows: 345
Columns: participant_id, age, sex, task, condition, comprehension

sub-001 participant-level metadata:
- participant_id: sub-001
- age: 22,23
- sex: F,F
- task: pieman,tunnel
- condition: n/a,n/a
- comprehension: n/a,n/a

## sub-001_scans.tsv

Number of scan rows for sub-001: 4
Columns: filename, condition, comprehension

Files listed in scans.tsv:
- anat/sub-001_T1w.nii.gz
- func/sub-001_task-pieman_run-1_bold.nii.gz
- func/sub-001_task-pieman_run-2_bold.nii.gz
- func/sub-001_task-tunnel_bold.nii.gz

## Event files

### sub-001_task-pieman_run-1_events.tsv

Number of rows: 2
Columns: onset, duration, trial_type, stim_file
Required timing columns present: onset, duration
Project-relevant columns present: stim_file, trial_type
Project-relevant columns absent: decision, rt
Missing values by column:
- onset: 0
- duration: 0
- trial_type: 0
- stim_file: 0

### sub-001_task-pieman_run-2_events.tsv

Number of rows: 2
Columns: onset, duration, trial_type, stim_file
Required timing columns present: onset, duration
Project-relevant columns present: stim_file, trial_type
Project-relevant columns absent: decision, rt
Missing values by column:
- onset: 0
- duration: 0
- trial_type: 0
- stim_file: 0

### sub-001_task-tunnel_events.tsv

Number of rows: 1
Columns: onset, duration, trial_type, stim_file
Required timing columns present: onset, duration
Project-relevant columns present: stim_file, trial_type
Project-relevant columns absent: decision, rt
Missing values by column:
- onset: 0
- duration: 0
- trial_type: 0
- stim_file: 0

## Interpretation for QC workflow

This dataset is useful for testing general BIDS-style metadata inspection.
The event files include onset and duration columns, which are essential for task-fMRI metadata QC.
However, this dataset does not contain the same rich trial-wise decision and reaction-time fields as the motivating lab dataset.
Therefore, it is best used as an open-data validation case for file structure, event timing, task labels, stimulus labels, and missingness checks.
