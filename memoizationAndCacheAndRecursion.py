def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)  #here we will see fib(1),fib(2),fib(3) calculate many times
fib(10)

print("#################use cache using class###################")
class Fib:
    def __init__(self):
        self.cache={1:1,2:1}

    def fib(self,n):
        if n not in self.cache:
            print("Calculating fib({0})".format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
            print(self.cache[n])
        return self.cache[n]

f = Fib()
print("result ",f.fib(5))
print(f.cache)

print("###################use closure############################")

def fib():
    cache = {1:1,2:2}
    def calc_fib(n):
        if n not in cache:
            print("Calculating fib({0})".format(n))            
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib


f = fib()
print(f(5))
print(f(7)) #here you will see Calculating fib() run only for 7 and 6 not to 5 to 3 because these values are already exist in cache


print("###################use decorator############################")
#here decorator handle only caching(cache)
#don't use keyword argument with inner when use decorator it make comlexity
def memorize(fib):
    cache = dict()
    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]
    return inner

@memorize
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)
print(fib(5))
    
#or we call this way
fib = memorize(fib)
print(fib(5))


@memorize
def fact(n):
    print("Calculating fact {0}!".format(n))
    return 1 if n == 1 else n * fact(n-1)

print(fact(5))
print(fact(6))

print("################# use lru_cache #####################")
#note let we have maxsize of cache 5 then we get fact(5) and cache will be {1:1,2:2,3:6,4:24,5:120} and 
# cache is full and then we calculate fact(8)
#now we have 8-5=3 variable more from length of cache here first three element(1,2,3) remove automatically
#and in cache value will be {4:24,5:120,6:720,7:5040,8:40320} if now we calulate fact(3) again then value for
# 1,2,3 calculate and add in cache

from functools import lru_cache

@lru_cache(maxsize = 5)  #here lru_cache is decorator
def fact(n):
    print("Calculating fact {0}!".format(n))
    return 1 if n == 1 else n * fact(n-1)

print(fact(5))
print(fact(8))
print(fact(3))
print(fact(8))
# print(fact(4))
# print(fact(3))


    
