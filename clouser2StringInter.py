x = ""
def outer():
    x = [1,2,3]
    # x = "python"
    print(hex(id(x)))
    def inner():
        # y = x
        x = [1,2,3]
        # x = "python"
        x[0] = 3
        # print(x)
        print(hex(id(x)))
    # print(x)
    return inner
  
fun = outer() #here fun is called closure
print(fun.__code__.co_freevars)
print(fun.__closure__)
fun()


# x = [1,2,3]
# print(id(x))
# x = [1,2,3]
# print(id(x))
