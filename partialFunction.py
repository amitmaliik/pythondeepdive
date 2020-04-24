from functools import partial
#in partail we can give argument of function see below example

def my_func(x,y,z):
    print(x,y,z)

def f(y,z):
    my_func(10,y,z)

f(20,30)

f = lambda y,z:my_func(10,y,z)
f(20,30)

f = partial(my_func,10)
f(20,30)

f = partial(my_func,10,20)
f(30)

def my_func(a,b,*args,k1,k2,**kwargs):
    print(a,b,args,k1,k2,kwargs)

def f(b,*args,k2,**kwargs):
    my_func(10,b,*args,k1=20,k2=k2,**kwargs)

f(11,111,222,k2=40,k3=300,k4=400)

# def my_func(a,b,*args,k1,k2,**kwargs):    
#     print(a,b,args,k1,k2,kwargs)

# def f(b,k2,**kwargs):
#     my_func(10,b,111,222,k1=20,k2=k2,**kwargs)

# f(11,40,k3=300,k4=400)

f = partial(my_func,10,k1=20) #here partial give value 10 to first variable(a) 
print(id(my_func))
print(id(f))

f(11,111,222,k2=40,k3=300,k4=400)


########################################################################################
#note => when we pass value in second argument than we should not use *args after second argument
#this will not work
# def my_func(a,b,*args,k1,k2,**kwargs):
#     print(a,b,args,k1,k2,kwargs)

# #we can give value of b except a using variable name
# f = partial(my_func,b=11,k1=20) #here partial give value 11 to second variable(b) 
# print(id(my_func))
# print(id(f))

# f(10,111,222,k2=40,k3=300,k4=400)


def my_func(a,b,k1,k2,**kwargs):
    print(a,b,k1,k2,kwargs)

#we can give value of b except a using variable name
f = partial(my_func,b=11,k1=20) #here partial give value 11 to second variable(b) 
print(id(my_func))
print(id(f))

f(10,k2=40,k3=300,k4=400)


###########################################################################################
def pow(base,exponent):
    print(base**exponent)

pow(5,2)

f = partial(pow,2)#here pow takes 2 as first argument by deault 
f(5)

f = partial(pow,exponent = 2)#here we fix 2 as exponent value 
f(5)

a = 2
f = partial(pow,exponent = a)#here we fix 2 as exponent value and exponent has reference of integer 2
f(5)

#here we will change the value of a , so a has reference of integer 3, while exponent has reference of integer 2 
#because these(a,exponent) are immutable , so below f(5) gives 25 not the 125
a = 3
f(5)

#now we will work with mutable
def my_func(a,b):
    print(a,b)

a = [1,2]
f = partial(my_func,a)
f(100)

a.append(12)
f(100)

#######################################################################################
#now we will calculate the distance from origin
origin  = (0,0)
dist = lambda a,b:(a[0]-b[0])**2 + (a[1]-b[1])**2
list1 = [(-3,2),(0,0),(0,2),(1,1),(1,10)]

distance = dist((1,1),origin)
print(distance)
# print(sorted(list1,key=lambda a:a[0]**2+a[1]**2)) #worked

def getDistance(cordinates):#list1 is of tuple so cordinates has 2 value in one tuple
    return (cordinates[0]-origin[0])**2 + (cordinates[1]-origin[1])**2

print(sorted(list1,key = getDistance))



#now we will use partial
result = partial(dist,origin)
print(sorted(list1,key = result))

print(sorted(list1,key = partial(dist,origin)))

f = partial(dist,origin)
print(f((1,2)))
print(sorted(list1,key = f))

f = lambda x : dist(x,origin)
# print(f(list1)) #it will not work because dist function require tuple, not the list of tuple
print(sorted(list1,key = f))#here one by one tuple pass to dist using f

print(sorted(list1,key = lambda x : dist(x,origin)))