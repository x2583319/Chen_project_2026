from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
BIDS_DIR = ROOT / "synthetic_bids"

sub = "sub-01"
task = "listening"

func_dir = BIDS_DIR / sub / "func"
func_dir.mkdir(parents=True, exist_ok=True)

# dataset_description.json is required for BIDS datasets
dataset_description = {
    "Name": "Minimal synthetic BIDS dataset for BrainHack School BIDS module",
    "BIDSVersion": "1.10.0",
    "DatasetType": "raw",
    "Authors": ["Chelsea Chen"]
}

(BIDS_DIR / "dataset_description.json").write_text(
    json.dumps(dataset_description, indent=2),
    encoding="utf-8"
)

# participants.tsv
participants = pd.DataFrame({
    "participant_id": [sub],
    "age": [25],
    "sex": ["n/a"]
})
participants.to_csv(BIDS_DIR / "participants.tsv", sep="\t", index=False)

# task events file
events = pd.DataFrame({
    "onset": [0.0, 12.0, 24.0],
    "duration": [10.0, 10.0, 10.0],
    "trial_type": ["music_A", "music_B", "music_A"]
})
events.to_csv(
    func_dir / f"{sub}_task-{task}_events.tsv",
    sep="\t",
    index=False
)

# events sidecar
events_json = {
    "onset": {
        "Description": "Event onset in seconds from the start of the run."
    },
    "duration": {
        "Description": "Event duration in seconds."
    },
    "trial_type": {
        "Description": "Synthetic auditory/music condition label."
    }
}
(func_dir / f"{sub}_task-{task}_events.json").write_text(
    json.dumps(events_json, indent=2),
    encoding="utf-8"
)

print(f"Created minimal synthetic BIDS dataset at: {BIDS_DIR}")
print("Files created:")
for path in sorted(BIDS_DIR.rglob("*")):
    if path.is_file():
        print(path.relative_to(BIDS_DIR))
