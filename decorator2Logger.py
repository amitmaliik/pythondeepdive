from functools import wraps
from datetime import datetime,timezone
from time import perf_counter
def logged(fn):
    count = 0
    @wraps(fn)
    def inner(*args,**kwargs):
        nonlocal count
        count += 1
        run_dt = datetime.now(timezone.utc)
        result = fn(*args,**kwargs)
        print("{0} function {1} is called {2} times ".format(run_dt,fn.__name__,count))
        return result
    return inner        

@logged
def my_func():
    pass
my_func()

print('###############################################################################')

def timed(fn):
    @wraps(fn)
    def inner(*args,**kwargs):
        startTime = perf_counter()
        print(startTime)
        result = fn(*args,**kwargs)
        endTime = perf_counter()
        print(endTime)
        print('{0} ran for {1:.6f}s '.format(fn.__name__,endTime-startTime))    
        return result
    return inner

@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce
    return reduce(mul,range(1,n+1))

result = fact(3)
print(result)

print('###############################################################################')

#it is like as 
fact = logged(timed(fact))
result = fact(3)
print(result)




