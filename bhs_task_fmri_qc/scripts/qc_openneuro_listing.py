from pathlib import Path
import argparse
import re
from collections import Counter

def parse_aws_listing(path):
    rows = []
    for line in Path(path).read_text().splitlines():
        parts = line.split(maxsplit=3)
        if len(parts) != 4:
            continue
        date, time, size, key = parts
        try:
            size = int(size)
        except ValueError:
            continue
        rows.append({"date": date, "time": time, "size": size, "key": key})
    return rows

def strip_suffix(key):
    suffixes = [
        "_events.tsv",
        "_bold.nii.gz",
        "_bold.nii",
        "_bold.json",
        "_T1w.nii.gz",
        "_T1w.nii",
        "_T1w.json",
    ]
    for suffix in suffixes:
        if key.endswith(suffix):
            return key.replace(suffix, "")
    return key

def main():
    parser = argparse.ArgumentParser(
        description="Smoke-test QC for an OpenNeuro AWS S3 listing."
    )
    parser.add_argument("--listing", required=True, help="Path to aws s3 ls --recursive output")
    parser.add_argument("--out", required=True, help="Output Markdown report")
    parser.add_argument("--dataset", default="OpenNeuro dataset", help="Dataset label for the report")
    args = parser.parse_args()

    rows = parse_aws_listing(args.listing)
    keys = [r["key"] for r in rows]

    subjects = sorted(set(re.findall(r"(sub-[A-Za-z0-9]+)", "\n".join(keys))))

    dataset_description = [k for k in keys if k.endswith("dataset_description.json")]
    participants = [k for k in keys if k.endswith("participants.tsv")]

    events = [k for k in keys if k.endswith("_events.tsv")]
    bold = [k for k in keys if k.endswith("_bold.nii.gz") or k.endswith("_bold.nii")]
    bold_json = [k for k in keys if k.endswith("_bold.json")]
    t1w = [k for k in keys if k.endswith("_T1w.nii.gz") or k.endswith("_T1w.nii")]
    fmap = [k for k in keys if "/fmap/" in k]

    modality_counts = Counter()
    for k in keys:
        if "/func/" in k:
            modality_counts["func"] += 1
        elif "/anat/" in k:
            modality_counts["anat"] += 1
        elif "/fmap/" in k:
            modality_counts["fmap"] += 1
        elif "/stimuli/" in k:
            modality_counts["stimuli"] += 1
        else:
            modality_counts["other/root"] += 1

    event_bases = {strip_suffix(k) for k in events}
    bold_bases = {strip_suffix(k) for k in bold}

    events_without_bold = sorted(event_bases - bold_bases)
    bold_without_events = sorted(bold_bases - event_bases)

    warnings = []
    if not dataset_description:
        warnings.append("dataset_description.json not found.")
    if not participants:
        warnings.append("participants.tsv not found.")
    if not events:
        warnings.append("No events.tsv files found.")
    if not bold:
        warnings.append("No BOLD NIfTI files found.")
    if events_without_bold:
        warnings.append(f"{len(events_without_bold)} event file base(s) have no matching BOLD file.")
    if bold_without_events:
        warnings.append(f"{len(bold_without_events)} BOLD file base(s) have no matching events file.")

    out = []
    out.append(f"# {args.dataset} Smoke-test QC Report\n")
    out.append("## Scope\n")
    out.append(
        "This is a remote file-inventory smoke test based on an AWS S3 listing. "
        "It checks file presence and BIDS-like matching between event files and BOLD files. "
        "It does not download or validate NIfTI image integrity.\n"
    )

    out.append("## Dataset-level summary\n")
    out.append(f"- Total files listed: {len(keys)}")
    out.append(f"- Subjects detected: {len(subjects)}")
    out.append(f"- dataset_description.json found: {'PASS' if dataset_description else 'WARNING'}")
    out.append(f"- participants.tsv found: {'PASS' if participants else 'WARNING'}\n")

    out.append("## Image and event inventory\n")
    out.append(f"- BOLD NIfTI files: {len(bold)}")
    out.append(f"- BOLD JSON sidecars: {len(bold_json)}")
    out.append(f"- events.tsv files: {len(events)}")
    out.append(f"- T1w anatomical files: {len(t1w)}")
    out.append(f"- Fieldmap-related files: {len(fmap)}\n")

    out.append("## Directory/modality counts\n")
    for name, count in modality_counts.most_common():
        out.append(f"- {name}: {count}")
    out.append("")

    out.append("## Cross-check: events × BOLD\n")
    out.append(f"- Event bases detected: {len(event_bases)}")
    out.append(f"- BOLD bases detected: {len(bold_bases)}")
    out.append(f"- Events without matching BOLD: {len(events_without_bold)}")
    out.append(f"- BOLD without matching events: {len(bold_without_events)}\n")

    if events_without_bold:
        out.append("### Example events without matching BOLD\n")
        for item in events_without_bold[:10]:
            out.append(f"- WARNING: {item}")
        out.append("")

    if bold_without_events:
        out.append("### Example BOLD files without matching events\n")
        for item in bold_without_events[:10]:
            out.append(f"- WARNING: {item}")
        out.append("")

    out.append("## Warnings\n")
    if warnings:
        for w in warnings:
            out.append(f"- WARNING: {w}")
    else:
        out.append("- PASS: No major file-inventory warnings detected in this smoke test.")

    out.append("\n## Next step\n")
    out.append(
        "Download a small subset, such as one subject/run, then add NIfTI readability checks "
        "with nibabel: shape, affine/header readability, voxel size, and number of BOLD volumes."
    )

    Path(args.out).write_text("\n".join(out))
    print(f"Wrote report to {args.out}")

if __name__ == "__main__":
    main()
