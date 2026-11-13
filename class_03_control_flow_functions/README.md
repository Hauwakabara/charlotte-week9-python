# Class 03 - Control Flow & Functions

This lab classifies well pressures and calculates averages for valid active readings only.

Skipped records are records where status is not active, or where pressure is invalid (None or below 0), so they are not counted in the averages. A return value is what a function gives back to the code that called it — for example classify_pressure() returns "high", "normal", "low" or "invalid", and psi_to_kpa() returns the pressure in kPa.