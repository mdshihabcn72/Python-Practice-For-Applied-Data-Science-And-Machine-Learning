# Demonstrate how to add and remove elements in a set.

numbers = {1, 2, 3,4,3,4}
numbers.add(4)
numbers.discard(2)
numbers.update([5, 6])


print("Updated set:", numbers)