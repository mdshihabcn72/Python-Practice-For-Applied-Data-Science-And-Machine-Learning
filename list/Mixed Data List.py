#A list that contains mixed data types.

mixed_list = ["apple",10,True,"String",None]

description = [(type(x).__name__,x) for x in mixed_list]

print("Mixed Data list :", mixed_list)
print("Data types and values :", description)