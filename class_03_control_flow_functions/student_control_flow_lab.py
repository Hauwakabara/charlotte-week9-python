# Class 03 - Control Flow & Functions
# Well pressure lab

READINGS = [
    {"well_id": "WELL-07", "pressure_psi": 3100, "status": "active"},
    {"well_id": "WELL-07", "pressure_psi": 3260, "status": "active"},
    {"well_id": "WELL-08", "pressure_psi": 2700, "status": "active"},
    {"well_id": "WELL-08", "pressure_psi": 2890, "status": "active"},
    {"well_id": "WELL-10", "pressure_psi": 3400, "status": "active"},
    {"well_id": "WELL-10", "pressure_psi": 3595, "status": "active"},
    {"well_id": "WELL-07", "pressure_psi": 3000, "status": "inactive"},
    {"well_id": "WELL-08", "pressure_psi": -100, "status": "active"},
    {"well_id": "WELL-09", "pressure_psi": 3200, "status": "inactive"},
    {"well_id": "WELL-10", "pressure_psi": None, "status": "active"},
]

# A. Decisions
def classify_pressure(pressure_psi):
    if pressure_psi is None or pressure_psi < 0:
        return "invalid"
    if pressure_psi >= 3500:
        return "high"
    if pressure_psi >= 2500:
        return "normal"
    return "low"

# C. Functions
def psi_to_kpa(psi):
    return psi * 6.8947572932

# B. Loops - print ALL 10, even inactive ones
print("All readings:")
for r in READINGS:
    label = classify_pressure(r["pressure_psi"])
    print(f'{r["well_id"]}: {r["pressure_psi"]} psi -> {label} (status: {r["status"]})')

# D. Filter - only active + valid count toward averages
print("\nConversion check:")
print(f"3150 psi = {psi_to_kpa(3150):.2f} kPa")

totals = {}
counts = {}
valid = 0
skipped = 0

for r in READINGS:
    if r["status"] != "active":
        skipped += 1
        continue
    if classify_pressure(r["pressure_psi"]) == "invalid":
        skipped += 1
        continue
    valid += 1
    totals[r["well_id"]] = totals.get(r["well_id"], 0) + r["pressure_psi"]
    counts[r["well_id"]] = counts.get(r["well_id"], 0) + 1

print(f"\nvalid={valid}, skipped={skipped}")
print("Averages (valid active only):")
for well_id in sorted(totals):
    avg = totals[well_id] / counts[well_id]
    print(f"{well_id}: {avg:.2f} psi from {counts[well_id]} valid active readings")