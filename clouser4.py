def counter(fn):
    count = 0
    def inner(*args,**kwargs):
        nonlocal count
        count += 1
        print("function {0} is called {1} times ".format(fn.__name__,count))
        return fn(*args,**kwargs)
    return inner


def add(a,b):
    return a+b

def mult(a,b):
    return a*b

add = counter(add)
print(add.__closure__) #here we will see two cells one for fn and second for count
add(1,2)
add(2,3)
print(add.__closure__)
print(hex(id(3)))

mult = counter(mult)
mult(1,2)
mult(2,3)
print(mult.__closure__)