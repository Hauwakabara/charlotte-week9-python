# Reflection - Class 03

1. What does classify_pressure() do?
It checks the pressure and returns invalid for None or negative, high for >= 3500, normal for >= 2500, else low.

2. Why loop over all 10 readings?
So we can see every reading, even inactive ones, before we decide what to count.

3. Why use a function like psi_to_kpa()?
So we can reuse the same conversion (x 6.8947572932) anywhere without rewriting it, and avoid mistakes.

4. What happens if we don't filter?
Inactive and invalid readings would lower or break the averages and give a wrong result.

5. What would I change next?
I would read the data from well_readings.csv instead of a hardcoded list, so new wells work automatically.