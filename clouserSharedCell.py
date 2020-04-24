def outer():
    count = 0
    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1,inc2

inc1,inc2 = outer()

print(inc1.__code__.co_freevars)
print(inc1.__closure__)
print(inc1())
print(inc2.__code__.co_freevars)
print(inc2.__closure__)
print(inc2())

#here we have count as a free variable and count of outer, count of inc1 and count of inc2 indicate to same cell


