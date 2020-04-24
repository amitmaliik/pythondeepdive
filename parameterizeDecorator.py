def decFactory():
    print("running decFactory")
    def dec(fn):
        print("running decorator")
        def inner(*args,**kwargs):
            print("running inner")
            fn(*args,**kwargs)
        return inner
    return dec

def my_fun():
    print("running my_fun")

print("##create decorator##")
dec = decFactory()

print("##running decorator##")
my_fun = dec(my_fun)

print("##call function##")
my_fun()

#or

my_fun = decFactory()(my_fun)
my_fun()


#or we can use this way
print("####we can call above three statement like as####")
@decFactory() #decFactory return a decorator and we can sey @decFactory = @dec
def my_fun():
    print("running my_fun")

my_fun()

print("####################now we will use parameter in decorator########################")

def dec(fn,a):
    print("running decorator")
    def inner(*args,**kwargs):
        print("running inner")     
        print("argument is ",a)
        return fn(*args,**kwargs)
    return inner


def my_fun():
    print("running my_fun")

dec = dec(my_fun,2)
dec()



print("###############using @ symbol with parameterize dacorator##################")
#using @ symbol with parameterize dacorator
def decFactory(a):
    def dec(fn):
        print("running decorator")
        def inner(*args,**kwargs):
            print("running inner")     
            print("argument is ",a)
            return fn(*args,**kwargs)
        return inner
    return dec



@decFactory(2)
def my_fun():
    print("running my_fun")

my_fun()

