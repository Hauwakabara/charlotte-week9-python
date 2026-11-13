import csv
from datetime import datetime

PSI_TO_KPA = 6.8947572932

def parse_line(line):
    """Parse one raw line. Return clean dict or raise ValueError."""
    parts = line.strip().split("|")
    if len(parts) != 7:
        raise ValueError(f"Expected 7 fields, got {len(parts)}: {line.strip()}")

    well_id, timestamp_str, pressure_str, pressure_unit, temp_str, temp_unit, status = [p.strip() for p in parts]

    if not well_id:
        raise ValueError("Missing well_id")

    # Validate timestamp
    try:
        datetime.fromisoformat(timestamp_str)
    except ValueError:
        raise ValueError(f"Invalid timestamp: {timestamp_str}")

    # Validate pressure
    try:
        pressure = float(pressure_str)
    except ValueError:
        raise ValueError(f"Invalid pressure: {pressure_str}")
    if pressure < 0:
        raise ValueError(f"Negative pressure: {pressure}")

    if pressure_unit not in ("psi", "kPa"):
        raise ValueError(f"Invalid pressure unit: {pressure_unit}")

    # Validate temperature
    try:
        temperature = float(temp_str)
    except ValueError:
        raise ValueError(f"Invalid temperature: {temp_str}")
    if temp_unit not in ("F", "C"):
        raise ValueError(f"Invalid temperature unit: {temp_unit}")

    if status not in ("ACTIVE", "OFFLINE"):
        raise ValueError(f"Invalid status: {status}")

    # Convert
    pressure_kpa = round(pressure * PSI_TO_KPA, 2) if pressure_unit == "psi" else round(pressure, 2)
    temperature_c = round((temperature - 32) * 5 / 9, 2) if temp_unit == "F" else round(temperature, 2)

    return {
        "well_id": well_id,
        "timestamp": timestamp_str,
        "pressure_kpa": pressure_kpa,
        "temperature_c": temperature_c,
        "status": status,
    }

def process_log(source, output):
    """Read raw log, write clean CSV. Skip blanks and # comments. Returns (clean, rejected)."""
    clean = 0
    rejected = 0
    with open(source, "r", encoding="utf-8") as f_in, open(output, "w", newline="", encoding="utf-8") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=["well_id", "timestamp", "pressure_kpa", "temperature_c", "status"])
        writer.writeheader()
        for line_no, line in enumerate(f_in, start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            try:
                row = parse_line(line)
                writer.writerow(row)
                clean += 1
            except ValueError as e:
                print(f"Line {line_no} rejected: {e}")
                rejected += 1
    return clean, rejected

if __name__ == "__main__":
    clean, rejected = process_log("drilling_telemetry_raw.txt", "cleaned_telemetry.csv")
    print(f"Done. Clean: {clean}, Rejected: {rejected}")