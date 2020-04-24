def outer():
    x = "python"
    def inner():
        print(x) #here it is called free variable

    return inner

fun = outer() #here fun is called closure
fn = fun.__code__.co_freevars
print(fn)
print(fun.__closure__)