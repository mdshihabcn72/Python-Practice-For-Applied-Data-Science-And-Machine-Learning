# Build a histogram normalized to probabilities

from collections import Counter

data = [1,2,3,3,1,4,5,6,6,7,2]

counter = Counter(data)

total = sum(counter.values())
probabilities = {k:v/total for k,v in counter.items()}

print(probabilities)
print(total)

