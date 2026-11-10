readings = [
    {"well_id": "WELL-01", "field": "north", "pressure_psi": 2800.0, "sensor_active": True},
    {"well_id": "WELL-02", "field": "south", "pressure_psi": 2950.0, "sensor_active": True},
    {"well_id": "WELL-03", "field": "east", "pressure_psi": 2750.0, "sensor_active": False},
    {"well_id": "WELL-07", "field": "north", "pressure_psi": 3100.0, "sensor_active": True},
    {"well_id": "WELL-07", "field": "north", "pressure_psi": 3180.0, "sensor_active": True},
    {"well_id": "WELL-08", "field": "south", "pressure_psi": 2900.0, "sensor_active": True},
    {"well_id": "WELL-08", "field": "south", "pressure_psi": 3050.0, "sensor_active": False},
    {"well_id": "WELL-12", "field": "east", "pressure_psi": 2960.0, "sensor_active": True},
]

# 1. Two earliest + last
print("Two earliest:")
print(readings[0])
print(readings[1])
print("\nLast:")
print(readings[-1])
print(f"\nTotal observations: {len(readings)}")

# 2. Sorted distinct IDs and fields
well_ids = sorted({r["well_id"] for r in readings})
fields = sorted({r["field"] for r in readings})
print(f"\nDistinct well IDs ({len(well_ids)}): {well_ids}")
print(f"Distinct fields: {fields}")

# 3. Sum and mean
pressures = [r["pressure_psi"] for r in readings]
total = sum(pressures)
mean = total / len(pressures)
print(f"\nTotal pressure: {total} psi")
print(f"Mean pressure: {mean} psi")

# 4. Per well counts - keeps duplicates
counts = {}
for r in readings:
    well = r["well_id"]
    counts[well] = counts.get(well, 0) + 1

print("\nObservations per well:")
for well, count in sorted(counts.items()):
    print(f"{well}: {count}")

print(f"\nIs WELL-12 in data? {'WELL-12' in well_ids}")