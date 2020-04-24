def pow(n):
    def inner(x):
        return x**n
    return inner

square = pow(2)
print(square.__code__.co_freevars)
print(square.__closure__)
print(square(4))

cube = pow(3)
print(cube.__code__.co_freevars)
print(cube.__closure__)
print(cube(5))
print(hex(id(5)))

#a new closure is created whenever function is called, so here two closure is created

print(cube(2))
print(cube.__code__.co_freevars)
print(cube.__closure__)