from pathlib import Path
import pandas as pd

root = Path("data/openneuro_ds002345")
out_dir = Path("reports/open_data")
out_dir.mkdir(parents=True, exist_ok=True)

participants_file = root / "participants.tsv"
scans_file = root / "sub-001" / "sub-001_scans.tsv"
event_files = sorted((root / "sub-001" / "func").glob("*_events.tsv"))

report = []

report.append("# Open Data Metadata Check")
report.append("")
report.append("Dataset: OpenNeuro ds002345")
report.append("")
report.append("This report summarizes the metadata files downloaded for the BrainHack School Open Data module.")
report.append("")

# Participants metadata
participants = pd.read_csv(participants_file, sep="\t")
report.append("## participants.tsv")
report.append("")
report.append(f"Number of participant rows: {len(participants)}")
report.append(f"Columns: {', '.join(participants.columns)}")
report.append("")

if "participant_id" in participants.columns:
    sub001 = participants[participants["participant_id"] == "sub-001"]
    if not sub001.empty:
        report.append("sub-001 participant-level metadata:")
        for col in participants.columns:
            report.append(f"- {col}: {sub001.iloc[0][col]}")
        report.append("")

# Scan metadata
scans = pd.read_csv(scans_file, sep="\t")
report.append("## sub-001_scans.tsv")
report.append("")
report.append(f"Number of scan rows for sub-001: {len(scans)}")
report.append(f"Columns: {', '.join(scans.columns)}")
report.append("")
report.append("Files listed in scans.tsv:")
for filename in scans["filename"]:
    report.append(f"- {filename}")
report.append("")

# Event metadata
required_event_columns = {"onset", "duration"}
optional_project_columns = {"trial_type", "stim_file", "decision", "rt"}

report.append("## Event files")
report.append("")

for event_file in event_files:
    events = pd.read_csv(event_file, sep="\t")
    report.append(f"### {event_file.name}")
    report.append("")
    report.append(f"Number of rows: {len(events)}")
    report.append(f"Columns: {', '.join(events.columns)}")
    
    missing_required = sorted(required_event_columns - set(events.columns))
    if missing_required:
        report.append(f"Required timing columns missing: {', '.join(missing_required)}")
    else:
        report.append("Required timing columns present: onset, duration")
    
    present_optional = sorted(optional_project_columns & set(events.columns))
    absent_optional = sorted(optional_project_columns - set(events.columns))
    
    report.append(f"Project-relevant columns present: {', '.join(present_optional) if present_optional else 'none'}")
    report.append(f"Project-relevant columns absent: {', '.join(absent_optional) if absent_optional else 'none'}")
    
    missing_values = events.isna().sum()
    report.append("Missing values by column:")
    for col, count in missing_values.items():
        report.append(f"- {col}: {count}")
    
    report.append("")

# Interpretation
report.append("## Interpretation for QC workflow")
report.append("")
report.append("This dataset is useful for testing general BIDS-style metadata inspection.")
report.append("The event files include onset and duration columns, which are essential for task-fMRI metadata QC.")
report.append("However, this dataset does not contain the same rich trial-wise decision and reaction-time fields as the motivating lab dataset.")
report.append("Therefore, it is best used as an open-data validation case for file structure, event timing, task labels, stimulus labels, and missingness checks.")
report.append("")

out_file = out_dir / "open_data_metadata_summary.md"
out_file.write_text("\n".join(report), encoding="utf-8")

print(f"Metadata summary written to: {out_file}")
