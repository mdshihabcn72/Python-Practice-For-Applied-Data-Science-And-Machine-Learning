# Split a list into chunks of size n.

def chanks(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]
        
if __name__ == "__main__":
    print(list(chanks(list(range(12)),4)))