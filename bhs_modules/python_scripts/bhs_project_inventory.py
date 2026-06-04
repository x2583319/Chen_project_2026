import argparse
import csv
from collections import Counter
from pathlib import Path


def get_file_extension(path):
    """
    Return a clean file extension label.
    Special case: .nii.gz should be treated as one extension.
    """
    name = path.name

    if name.endswith(".nii.gz"):
        return "nii.gz"

    if path.suffix:
        return path.suffix.lstrip(".").lower()

    return "no_extension"


def should_skip(path, skip_names):
    """
    Decide whether a file should be skipped based on folder names.
    """
    return any(part in skip_names for part in path.parts)


def scan_project(project_root, skip_names):
    """
    Scan a project folder and return file information.
    """
    project_root = Path(project_root).expanduser().resolve()

    if not project_root.exists():
        raise FileNotFoundError(f"Project root does not exist: {project_root}")

    file_rows = []

    for path in project_root.rglob("*"):
        if path.is_file() and not should_skip(path, skip_names):
            relative_path = path.relative_to(project_root)
            extension = get_file_extension(path)

            file_rows.append({
                "relative_path": str(relative_path),
                "extension": extension,
                "size_bytes": path.stat().st_size
            })

    return project_root, file_rows


def save_csv(file_rows, output_csv):
    """
    Save the project inventory as a CSV file.
    """
    output_csv = Path(output_csv)
    output_csv.parent.mkdir(parents=True, exist_ok=True)

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["relative_path", "extension", "size_bytes"]
        )
        writer.writeheader()
        writer.writerows(file_rows)


def save_summary(project_root, file_rows, output_txt):
    """
    Save a human-readable summary report.
    """
    output_txt = Path(output_txt)
    output_txt.parent.mkdir(parents=True, exist_ok=True)

    extension_counts = Counter(row["extension"] for row in file_rows)
    total_size = sum(row["size_bytes"] for row in file_rows)

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write("BHS Project Inventory Report\n")
        f.write("============================\n\n")

        f.write(f"Project root: {project_root}\n")
        f.write(f"Total files scanned: {len(file_rows)}\n")
        f.write(f"Total size: {total_size} bytes\n\n")

        f.write("File counts by extension:\n")
        f.write("-------------------------\n")

        for extension, count in extension_counts.most_common():
            f.write(f"{extension}: {count}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Create a simple file inventory report for a BHS project folder."
    )

    parser.add_argument(
        "--project-root",
        required=True,
        help="Path to the project folder to scan."
    )

    parser.add_argument(
        "--output-csv",
        default="reports/project_inventory.csv",
        help="Path to save the detailed CSV inventory."
    )

    parser.add_argument(
        "--output-txt",
        default="reports/project_inventory_summary.txt",
        help="Path to save the summary TXT report."
    )

    parser.add_argument(
        "--skip",
        nargs="*",
        default=[".git", "__pycache__", ".DS_Store"],
        help="Folder or file names to skip."
    )

    args = parser.parse_args()

    project_root, file_rows = scan_project(args.project_root, args.skip)

    save_csv(file_rows, args.output_csv)
    save_summary(project_root, file_rows, args.output_txt)

    print("Project inventory completed!")
    print(f"Files scanned: {len(file_rows)}")
    print(f"CSV saved to: {args.output_csv}")
    print(f"Summary saved to: {args.output_txt}")


if __name__ == "__main__":
    main()