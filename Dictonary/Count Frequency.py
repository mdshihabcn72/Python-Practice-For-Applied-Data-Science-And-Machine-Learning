# Count the frequency of elements using a dictionary.

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

data_frequency = {}

for item in data:
    data_frequency[item] = data_frequency.get(item,0)+1
print(data_frequency)