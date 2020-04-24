from functools import wraps
def counter(fn):
    count = 0
    # @wraps(fn)
    def inner(*args,**kwargs):
        nonlocal count
        count += 1
        print("function {0},id of fn {1} is called {2} times ".format(fn.__name__,id(fn),count))
        return fn(*args,**kwargs)
    inner = wraps(fn)(inner) #we can write this at the place of @wraps(fn)
    return inner


def add(a,b):
    return a+b

print(id(add))
add = counter(add) #first way we use decorator, here counter is decorator function and add is decorated function
print(id(add))
result = add(1,2)

print(result)
print(help(add))

def mult(a:int,b:int,c:int=1,*,d):
    """
    this is multiply of numbers
    """
    return a*b*c*d

mult = counter(mult)
result = mult(1,2,d=4) #d is kargs argument
print(result)
print(help(mult))