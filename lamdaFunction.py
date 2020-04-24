x = lambda a,b : a**b
print(type(x))
print(x(2,3))
print(help(x))
print(x.__annotations__)


def apply_func(x,fn):
    return fn(x)


print(apply_func(3,lambda x : x**2))
print(apply_func('abc',lambda x : x[1:]*2))

def fun1(x):
    return x**3

print(apply_func(3,fun1))

x = lambda : "hello"
print(x())

x = lambda a , *args , y , **kwargs : (a,args,y,kwargs)
print(x(1,'a','b','c',y=123,name='ajay',salary=3000))

x = lambda a , *args , y , **kwargs : (a,*args,y,*kwargs)
print(x(1,'a','b','c',y=123,name='ajay',salary=3000))


def sq(x):
    return x**2

def apply_func(x,fn):
    return fn(x)

print(apply_func(3,sq))
print(apply_func(3,lambda x : x**2))

def apply_func(fn,*args,**kwargs): #apply_func(*args,**kwargs,fn) it not work , fn should be at first position
    print(*args)
    print(args)
    # print(**kwargs) #not work
    # print(kwargs)
    return fn(*args,**kwargs)

print(apply_func(sq,3))
print(apply_func(lambda x : x**2,3))
print(apply_func(lambda x,y : x**y,2,3))
print(apply_func(lambda x,*,y : x+y,1,y=20)) # * represent that only x will be posiotional argument(*args)
print(apply_func(lambda *args : sum(args),1,2,3,4,5,6,7,8,9))
print(apply_func(lambda *args,**kwargs : sum(args),1,2,3,4,5,6,7,8,9,y=10))
print(apply_func(lambda *args,**kwargs : sum(args),1,2,3,4,5,6,7,8,9,y=10))
# print(apply_func(sum,(1,2,3,4,5,6,7,8,9),y=10)) #not work
print(apply_func(sum,(1,2,3,4,5,6,7,8,9)))
# print(apply_func(sum,1,2,3,4,5,6,7,8,9)) #not work sum require tuple or list
print(sum((1,2,3,4,5,6,7,8,9))) #sum function require tuple or list
# print(sum(1,2,3,4,5,6,7,8,9)) #not work, sum function require tuple or list


a = {'id':1,'name':2}
print(a)
print(*a)

def apply_func(**kwargs):
    print(kwargs)
    

apply_func(**a) #we can pass dictionary this way
apply_func(a=10,b=20)

list1 = [1,2,3,4,4,5,6,6]

from functools import reduce
print(reduce(lambda a,b :a if a>b else b,list1))

# list1 = []
print(reduce(lambda a,b :a+b ,list1))

list1 = []
print(reduce(lambda a,b :a+b ,list1,100)) #we can use initializer in lmda function

list1 = [1,2,3,4]
print(reduce(lambda a,b :a+b ,list1,1)) #addig start from initializer like 1+1+2+3+4
