# A tuple that contains other tuples.

nested_tuple = (1,(2,3),(4,5,6),("a","b"))

def flatten_tuple(t):
    out =()
    for item in t:
        if isinstance(item,tuple):
            out += flatten_tuple(item)
        else:
            out += (item,)
    return out

print("Nested Tuple : ", nested_tuple)
print("Flattened Tuple :", flatten_tuple(nested_tuple))