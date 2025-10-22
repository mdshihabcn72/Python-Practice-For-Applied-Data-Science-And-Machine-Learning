# A tuple with mixed data types.

mixed = (2, "SHIHAB", 3.14, True, None)

for item in mixed:
    print(f"{item!r} is of type {type(item).__name__}")