# Demonstrate adding and updating dictionary entries.

dict_example = {"name":"Alice","age":30}

dict_example["city"] = "New York"  # Adding a new entry
dict_example["age"] = 25

print(dict_example) 
name = dict_example["name"]
print(f"The type is : {type(name).__name__}")