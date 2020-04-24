import sys
import time

#no difference show between execution time(both methods)
def compareUsingEqual(n):
    a = 'a i very long string'
    b = 'b i very long string'
    for i in range(n):
        if a == b:
            pass


def compareUsingIs(n):
    a = sys.intern('a i very long string')
    b = sys.intern('b i very long string')
    for i in range(n):
        if a is b:
            pass


start = time.perf_counter()
compareUsingEqual(1000000)
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
compareUsingIs(1000000)
end = time.perf_counter()
print(end-start)

a = {1,2,3}
print(a)
for i in a:
    print(i)


