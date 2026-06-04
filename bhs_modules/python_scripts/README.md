# BrainHack School 2026 - Writing Scripts in Python Module

This folder contains my completion of the BrainHack School "Writing scripts in Python" module and a small project-specific extension.

## 1. Official module

The official module asked us to create a command-line Python script for encrypting and decrypting text files.

Files:

- `useful_functions.py`
  - Contains reusable encryption and decryption functions.
- `cypher_script.py`
  - Uses `argparse` to run encryption/decryption from the command line.

Example usage:

```bash
python cypher_script.py -i message.txt -o message_encrypted.txt -k my_key -m encryption
python cypher_script.py -i message_encrypted.txt -o message_decrypted.txt -k my_key -m decryption
```

I also tested the official encrypted message from the tutorial and successfully decrypted the koala ASCII art.

## 2. Extension

To extend the module, I adapted the same command-line scripting structure to my own BHS project.

File:

- `bhs_project_inventory.py`

This script uses `argparse` and `pathlib` to scan a project folder and generate:

- a detailed CSV file inventory
- a human-readable TXT summary report
- file counts by extension
- total number of scanned files
- total file size

Example usage:

```bash
python bhs_project_inventory.py \
  --project-root /Users/chenxuan/Chen_project_2026 \
  --output-csv reports/project_inventory.csv \
  --output-txt reports/project_inventory_summary.txt
```

Example output:

```text
Project inventory completed!
Files scanned: 12
CSV saved to: reports/project_inventory.csv
Summary saved to: reports/project_inventory_summary.txt
```

This extension is relevant to my BHS project because it supports reproducibility, project organization, and file-level quality control.