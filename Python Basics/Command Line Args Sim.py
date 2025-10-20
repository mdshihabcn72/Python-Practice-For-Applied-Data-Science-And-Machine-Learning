# Simulate parsing simple command-line args from list.

args = ["--name","Shihab","--age","23","--city","Jiangsu"]

it = iter(args)
print(next(it))

parsed = {}

for i in it:
    if i.startswith("--"):
        parsed[i.lstrip("-")] = next(it,None)

print(parsed)

"""""
#with multiple values for a single key

def parse_multiple(args):
    it = iter(args)
    parsed = {}
    for a in it:
        if a.startswith("--"):
            key = a.lstrip("-")
            values = []
            while True:
                next_val = next(it,None)
                if next_val is None or next_val.startswith("--"):
                    parsed[key]= values
                    if next_val and next_val.startswith("--"):
                        
                        args = [next_val]+list(it)
                        it = iter(args)
                    break
                values.append(next_val)
    return parsed           

argss = ["--name","Shihab","--age","23","--city","Jiangsu"]

if __name__=="__main__":
    print(parse_multiple(argss))
    """