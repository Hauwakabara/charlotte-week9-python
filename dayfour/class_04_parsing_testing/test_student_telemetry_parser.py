import pytest
from student_telemetry_parser import parse_line

def test_psi_to_kpa_and_f_to_c():
    row = parse_line("WELL-01|2026-01-01T10:00:00|100|psi|212|F|ACTIVE")
    assert row["pressure_kpa"] == 689.48
    assert row["temperature_c"] == 100.0
    assert row["status"] == "ACTIVE"

def test_kpa_and_c_stay_same():
    row = parse_line("WELL-02|2026-01-01T10:05:00|500|kPa|100|C|ACTIVE")
    assert row["pressure_kpa"] == 500.0
    assert row["temperature_c"] == 100.0

def test_wrong_field_count():
    with pytest.raises(ValueError):
        parse_line("WELL-01|2026-01-01T10:00:00|100|psi")

def test_negative_pressure_rejected():
    with pytest.raises(ValueError):
        parse_line("WELL-01|2026-01-01T10:00:00|-10|psi|80|F|ACTIVE")

def test_bad_unit_rejected():
    with pytest.raises(ValueError):
        parse_line("WELL-01|2026-01-01T10:00:00|100|bar|80|F|ACTIVE")

def test_bad_status_rejected():
    with pytest.raises(ValueError):
        parse_line("WELL-01|2026-01-01T10:00:00|100|psi|80|F|UNKNOWN")