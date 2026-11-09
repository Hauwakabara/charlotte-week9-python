well_id = "WELL-01"
pressure_psi = 2500.0
temperature_f = 140.0
sensor_active = True

pressure_kpa = pressure_psi * 6.89476
temperature_c = (temperature_f - 32) * 5 / 9

print(f"Well: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print(f"Sensor active: {sensor_active}")


# Q10 - Second values - PREDICTION FIRST
# My prediction before running:
# Pressure: 3000 * 6.89476 = 20684.28 -> will show 20684.3 kPa
# Temperature: (32 - 32) * 5 / 9 = 0.0 -> will show 0.0 C

pressure_psi = 3000.0
temperature_f = 32.0

pressure_kpa = pressure_psi * 6.89476
temperature_c = (temperature_f - 32) * 5 / 9

print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")


# Q11 - Intentional type mismatch
raw_pressure = "3150"  # This looks like a number but it is a str

# This line FAILS on purpose, so we comment it out:
# print(raw_pressure * 6.89476)  # TypeError: can't multiply sequence by non-int of type 'float'

# float() fixes it - it converts the str "3150" to float 3150.0
pressure_psi = float(raw_pressure)
print(f"Fixed pressure: {pressure_psi * 6.89476:.1f} kPa")

# PART C - Reflection Paragraph
# I chose float for pressure and temperature because they can have decimals,
# and int would lose that precision. I used str for well_id because it is a
# name like "WELL-01", not a number for maths, and bool for sensor_active
# because a sensor is either on (True) or off (False). In Q10, my prediction
# for pressure was 20684.28 but Python printed 20684.3. This is not an error,
# it is rounding because I used :.1f to show only 1 decimal place.
# In Q11, the code failed at first because raw_pressure was "3150", a string,
# and Python cannot multiply a string by a float. Using float() converted
# it from str to float 3150.0, so the calculation worked.