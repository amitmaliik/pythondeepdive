print("########we are using decorator with function########")
def my_dec(a,b):
    def dec(fn):
        def inner(*args,**kwargs):
            print("decorated function called : a={0} , b={1} ".format(a,b))
            return fn(*args,**kwargs)
        return inner
    return dec

@my_dec(10,20)
def my_fun(s):
    print("hello {0}".format(s))

my_fun("world")


print("############now we will use decorator with class###########")

class MYCLASS:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __call__(self,fn): #here __call__ is decorator function
        print("decorator is called")
        def inner(*args,**kwargs):
            print("decorated function called : a={0} , b={1} ".format(self.a,self.b))
            return fn(*args,**kwargs)
        return inner


obj = MYCLASS(10,20)
# my_fun = obj.__call__(my_fun)
my_fun = obj(my_fun) #it is called __call__() function automatically whenever we call object,here we will gwt decorator
my_fun("world")

@MYCLASS(10,20)
def my_fun(s):
    print("hello {0}".format(s))
            

my_fun("world")
