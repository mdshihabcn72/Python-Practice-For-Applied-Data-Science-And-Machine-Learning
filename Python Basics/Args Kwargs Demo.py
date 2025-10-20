# Demonstrate *args and **kwargs usage.

def printer(*args,**kwargs):
    print("args : ",args) #*args → যেকোনো সংখ্যক positional arguments নেয় (টাপল আকারে)
    print("kw : ",kwargs) #**kwargs → যেকোনো সংখ্যক keyword arguments নেয় (ডিকশনারি আকারে)
    
    
if __name__ =="__main__":
    printer(20,30,1,a=50,b=40,c=20)


"""
---args----
def show_args(*args):
    print("args : ",args)

show_args(1, 2, 3)           # Arguments: (1, 2, 3)
show_args("a", "b", "c")     # Arguments: ('a', 'b', 'c')
show_args()                  # Arguments: ()  

----kwargs----
def show_kwargs(**kwargs):
    print("Keyword args:", kwargs)

show_kwargs(a=1, b=2)        # Keyword args: {'a': 1, 'b': 2}
show_kwargs(name="John", age=25) # Keyword args: {'name': 'John', 'age': 25}
show_kwargs()                # Keyword args: {}
"""