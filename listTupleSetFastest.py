import string,time
chars = string.ascii_letters
print(chars)

charList = list(chars)
charTuple = tuple(chars)
charSet = set(chars)

print(charList)
print(charTuple)
print(charSet)

def calledFunction(n,container):    
    for i in range(n):
        if 'z' in container:
            pass


start = time.perf_counter()
calledFunction(1000000,charList)
end = time.perf_counter()
print(end-start)


start = time.perf_counter()
calledFunction(1000000,charTuple)
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
calledFunction(1000000,charSet)
end = time.perf_counter()
print(end-start)

#so set is always fastest