import sys,time
a = 0
print(type(a))
print(sys.getsizeof(a)) #minimum bytes for integer is 24, extra of 24 represent number
# in python does not range exist like java,  bytes increase according to number
print(sys.getsizeof(1))
print(sys.getsizeof(-1))

def cal(a):
    for i in range(10000):
        a = a*2
    print(a)


start = time.perf_counter()
cal(100)
end = time.perf_counter()
print(end-start)
