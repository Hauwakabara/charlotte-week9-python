import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from telemetry_capstone import convert_pressure, convert_temperature, parse_record

class TestTelemetry(unittest.TestCase):
    def test_psi_to_kpa(self):
        self.assertAlmostEqual(convert_pressure(100, "psi"), 689.48, places=2)

    def test_kpa_passthrough(self):
        self.assertEqual(convert_pressure(2100, "kPa"), 2100)

    def test_f_to_c(self):
        self.assertAlmostEqual(convert_temperature(212, "F"), 100.0, places=2)

    def test_c_passthrough(self):
        self.assertEqual(convert_temperature(95, "C"), 95)

    def test_parse_valid_active(self):
        rec = parse_record("2025-01-01T08:00:00 | WELL-101 | 3150 | psi | 212 | F | ACTIVE")
        self.assertEqual(rec["well_id"], "WELL-101")
        self.assertEqual(rec["pressure_kpa"], "21718.49")
        self.assertEqual(rec["temperature_c"], "100.00")

    def test_parse_rejects_bad_pressure(self):
        with self.assertRaises(ValueError):
            parse_record("2025-01-01T09:30:00 | WELL-101 | bad | psi | 210 | F | ACTIVE")

    def test_parse_rejects_bar_unit(self):
        with self.assertRaises(ValueError):
            parse_record("2025-01-01T09:45:00 | WELL-102 | 2500 | bar | 100 | C | ACTIVE")

    def test_parse_rejects_negative_pressure(self):
        with self.assertRaises(ValueError):
            parse_record("2025-01-01T10:00:00 | WELL-103 | -10 | psi | 150 | F | ACTIVE")

    def test_parse_rejects_wrong_field_count(self):
        with self.assertRaises(ValueError):
            parse_record("2025-01-01T10:45:00 | WELL-104 | 3000 | psi | 200 | F")

    def test_parse_rejects_bad_status(self):
        with self.assertRaises(ValueError):
            parse_record("2025-01-01T12:45:00 | WELL-101 | 3000 | psi | 200 | F | PAUSED")

if __name__ == "__main__":
    unittest.main()