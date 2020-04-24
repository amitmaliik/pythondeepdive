def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    return inner

fun = outer() #here fun is called closure
fn = fun.__code__.co_freevars
print(fn)
print(fun.__closure__)
print(hex(id(0)))
fun()
print(fun.__closure__)
print(hex(id(1)))

#(<cell at 0x000001B924E30C48: int object at 0x00007FF8F9DE9320>,)
#(<cell at 0x000001B924E30C48: int object at 0x00007FF8F9DE9340>,)
#here you will see that cell address is same