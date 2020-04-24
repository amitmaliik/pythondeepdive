def my_func(a,b=2,c=3,*,kw1,kw2=2):#here * is necessary , before * whatever default value set show in a.__defaults__
    pass

#when we pass value like a=2,b=3 and we want to that values work like as positional argument then use *
#before * all variables that have default value then they are shows in a__defaults__ 
#after * variable must be present
a = my_func
print(a.__name__)
print(a.__defaults__)
print(a.__kwdefaults__)

def my_fun(a,b=1,*args,**kwargs):
    i = 10
    b = min(i,b)
    return a*b


print(my_fun.__code__.co_varnames)
print(my_fun.__code__.co_argcount) #it does not count *args and **kwargs,here it count only a,b. So it show 2

