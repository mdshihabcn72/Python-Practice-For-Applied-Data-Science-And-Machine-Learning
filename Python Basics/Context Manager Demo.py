# Use contextlib to create a simple context manager.

from contextlib import contextmanager

@contextmanager

def simple_cm():
    print("enter")
    try:
        yield   #with ব্লকের কোড এখানে execute হয়
    finally:    #error হলেও exit message print করবে
        print("exit")
        
with simple_cm():
    print("inside")