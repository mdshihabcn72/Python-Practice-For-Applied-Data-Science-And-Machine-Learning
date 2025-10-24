# Use get() and setdefault() for safe key access.

sample_dict = {'a': 1, 'b': 2, 'c': 3}
value_a = sample_dict.get('a', 0)  # Returns 1
value_d = sample_dict.get('d', 0) 
print(f"Value for 'a': {value_a}, Value for 'd': {value_d}") # Returns 0 since 'd' is not present