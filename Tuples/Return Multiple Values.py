# Example of returning multiple values using tuples.
def min_max_sum(values):

   return (min(values), max(values), sum(values))


nums = (5, 10, 15, 20)

mn, mx, total = min_max_sum(nums)

print(f"Min: {mn}, Max: {mx}, Sum: {total}")

