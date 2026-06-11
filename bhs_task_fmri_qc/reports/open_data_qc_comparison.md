# Open-data QC Comparison

| Check | ds003720 music fMRI | ds000007 stop-signal task |
|---|---:|---:|
| Subjects | 5 | 20 |
| BOLD | 90 | 118 |
| Events | 90 | 118 |
| T1w | 5 | 20 |
| Events without BOLD | 0 | 0 |
| BOLD without Events | 0 | 0 |

## Interpretation

- ds003720 tests the workflow on a music fMRI dataset.
- ds000007 tests the workflow on a non-music task-fMRI dataset.
- The comparison focuses on file inventory and event/BOLD matching, not scientific analysis.
- Differences in event-table columns demonstrate why a configurable QC workflow is useful.