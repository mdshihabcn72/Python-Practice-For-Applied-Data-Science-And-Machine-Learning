# Merge configuration dicts with priority: higher overrides lower.


def merge_configs(*configs):
    res = {}
    for cfg in configs:
        res.update(cfg)
    return res

print(merge_configs({'a': 1, 'b': 2}, {'b': 3}, {'c': 4}))

"""d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

d1.update(d2)
print(d1)  # {'a': 1, 'b': 3, 'c': 4}"""