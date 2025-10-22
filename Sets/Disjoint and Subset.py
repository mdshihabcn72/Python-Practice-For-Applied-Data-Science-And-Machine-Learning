a = {3, 2, 3}
b = {3, 4, 5}
c = {1, 2}
print("A and B disjoint?", a.isdisjoint(b))
print("C subset of A?", c.issubset(a))
print("A superset of C?", a.issuperset(c))