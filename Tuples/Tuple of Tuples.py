# Demonstrate how to work with a tuple of tuples.

records = (("id","name"),(1,"Alice"),(2,"Shihab"),(3,"Sajjad"))

headers = records[0]

data = records[1:]

print("Headers : ",headers)

print("Data Rows :")

for row in data:
    print(dict(zip(headers,row)))
