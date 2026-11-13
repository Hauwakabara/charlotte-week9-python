# Week 9 Class 5 — Drilling Telemetry Capstone

## Summary
Reads raw drilling telemetry, cleans it, converts psi to kPa and F to C, and separates good records from bad ones. Only accepts ACTIVE or IDLE records.

## How to run
python src/telemetry_capstone.py data/drilling_telemetry_capstone.txt outputs

## How to test
python -m unittest tests/test_telemetry_capstone -v

## Results
Done: 13 cleaned, 7 rejected, 5 wells
- outputs/cleaned_telemetry.csv
- outputs/rejected_records.csv
- outputs/well_summary.csv

## Known limitations
Only supports psi/kPa for pressure and F/C for temperature.