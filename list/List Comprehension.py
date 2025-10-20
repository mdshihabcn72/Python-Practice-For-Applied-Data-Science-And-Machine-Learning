#Examples of list comprehensions: squares and filtered values.

squers = [x**2 for x in range(10)]

even_times_two = [x*2 for x in range(20) if x%2==0]
print("Squares for 0-9 :", squers)
print("Even times two for 0-19:", even_times_two)