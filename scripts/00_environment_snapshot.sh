#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR="${1:-.}"
REPORT_DIR="reports"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTFILE="${REPORT_DIR}/environment_snapshot_${TIMESTAMP}.txt"

if [ ! -d "$PROJECT_DIR" ]; then
  echo "Error: directory does not exist: $PROJECT_DIR"
  exit 1
fi

mkdir -p "$REPORT_DIR"

PROJECT_ABS=$(cd "$PROJECT_DIR" && pwd)

{
  echo "BHS Environment Snapshot"
  echo "========================"
  echo "Date: $(date)"
  echo "Project directory: $PROJECT_ABS"
  echo "Current directory: $(pwd)"
  echo "User: $(whoami)"
  echo ""

  echo "Shell information"
  echo "-----------------"
  echo "SHELL=${SHELL:-unknown}"
  echo "Bash version: ${BASH_VERSION:-not running bash directly}"
  echo ""

  echo "Command-line tools"
  echo "------------------"

  for tool in bash git python3 conda code; do
    if command -v "$tool" >/dev/null 2>&1; then
      echo "[OK] $tool: $(command -v "$tool")"
      "$tool" --version 2>&1 | head -n 1 || true
    else
      echo "[MISSING] $tool"
    fi
    echo ""
  done

  echo "Python package check"
  echo "--------------------"

  python3 - <<'PY'
packages = [
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "nibabel",
    "nilearn"
]

for package in packages:
    try:
        module = __import__(package)
        version = getattr(module, "__version__", "version unknown")
        print(f"[OK] {package}: {version}")
    except ImportError:
        print(f"[MISSING] {package}")
PY

  echo ""
  echo "Project file inventory"
  echo "----------------------"

  echo "Number of files by type:"
  find "$PROJECT_ABS" \
    -path "$PROJECT_ABS/.git" -prune -o \
    -path "$PROJECT_ABS/reports" -prune -o \
    -type f -print | while read -r file; do
      case "$file" in
        *.nii.gz)
          echo "nii.gz"
          ;;
        *.*)
          basename "$file" | awk -F. '{print $NF}'
          ;;
        *)
          echo "no_extension"
          ;;
      esac
    done | sort | uniq -c | sort -nr

  echo ""
  echo "Selected neuroimaging/data-related files:"
  find "$PROJECT_ABS" \
    -path "$PROJECT_ABS/.git" -prune -o \
    -path "$PROJECT_ABS/reports" -prune -o \
    -type f \( \
      -name "*.nii" -o \
      -name "*.nii.gz" -o \
      -name "*.tsv" -o \
      -name "*.csv" -o \
      -name "*.json" -o \
      -name "*.html" \
    \) -print | sort

} | tee "$OUTFILE"

echo ""
echo "Saved report to: $OUTFILE"
