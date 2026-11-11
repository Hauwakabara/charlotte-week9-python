\# Charlotte Week 9 - Python



\## Part A - Telemetry Collections



This project uses Python collections (list, dict, set) to analyse well telemetry data.



File: daytwo/datastructure01\_homework.py



What it does:

\- Stores 8 pressure readings as a list of dictionaries

\- Gets two earliest + last readings using slicing

\- Uses a set to find 6 distinct well IDs and 3 distinct fields

\- Calculates total pressure: 23690.0 psi

\- Calculates mean pressure: 2961.25 psi

\- Counts observations per well using a dictionary

\- Checks if WELL-12 is in the data: True



How to run:

python daytwo/datastructure01\_homework.py



\## Part C - Reflection



I learned how to use lists, dictionaries, and sets together to clean and summarise real data. Slicing helped me get the earliest and last readings, sets helped me remove duplicates, and dictionaries helped me count per well.



CHARLOTTE PROJECTS  |  WEEK 9 · CLASS 2
Homework
Class 2 consolidation — Python collections and drilling telemetry | 100 marks
Part A — Concept questions (40 marks, 5 each)
1. Explain the difference between a list and a tuple using an engineering example.
A list can change, a tuple cannot. Example: readings is a list because new sensor readings keep coming in, you can append. measurement_units = ("psi", "m") is a tuple because units should never change. If you try to change a tuple, Python gives an error and protects your data.

2. Why are dictionary keys useful for representing one sensor observation?
One observation has many things: well_id, pressure, field, sensor_active. A dictionary gives each one a name, like {"well_id": "WELL-07", "pressure_psi": 3180.0}. So you can get pressure by name reading["pressure_psi"] instead of remembering position 2. It is clear and less easy to mix up.

3. What does zero-based indexing mean? Illustrate with readings[0] and readings[-1].
Counting starts from 0, not 1. readings[0] is the FIRST observation, the earliest one. readings[-1] is the LAST observation. -1 means count from the end backwards. If there are 8 readings, readings[0] is number 1 and readings[7] is number 8, which is also readings[-1].

4. Distinguish observation count and unique well count.
Observation count is how many readings you have = 8. Unique well count is how many different wells = 6. They are different because some wells were measured twice. WELL-07 and WELL-08 appear 2 times each, so 8 readings come from only 6 wells.

5. Explain what a set does when input IDs contain duplicates.
A set automatically removes duplicates. If you put {"WELL-07", "WELL-07", "WELL-08"} into a set, it keeps only {"WELL-07", "WELL-08"}. That is why we use a set to find distinct well IDs.

6. Why is sorted() useful when presenting values derived from a set?
A set has no order, every time you print it the order can change. sorted() puts it in A-Z order, so ["WELL-01", "WELL-07", "WELL-08"] always looks the same. For a report, sorted is clean, predictable and easy to check.

7. What happens if two entries in a single dictionary literal have the same key?
The second one wins and overwrites the first. Example: {"well_id": "WELL-07", "well_id": "WELL-08"} will only keep "WELL-08". The first WELL-07 is lost. That is why you cannot use one dictionary to store all 8 readings, you must use a list of dictionaries.

8. Explain how .get() differs from reading a dictionary key with square brackets.
reading["depth_m"] will crash with KeyError if depth_m does not exist. reading.get("depth_m", "not supplied") will NOT crash, it will just return "not supplied". .get() is safer when a field might be missing, which happens a lot with real sensor data.

## Part C - Reflection

I learned how to use lists, dictionaries, and sets together to analyse real telemetry data.

Using a list of dictionaries helped me store each reading with its well ID, field, time, and pressure. Slicing helped me get the two earliest and last readings easily.

Sets helped me remove duplicates to find the distinct wells and fields. Dictionaries helped me count how many observations each well had.

The hardest part was keeping the data organised, but once I structured it well, calculating total and mean pressure became simple. This task showed me how Python collections make real oil and gas data easier to clean and summarise.


