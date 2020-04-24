import inspect
def my_func(
    a: "mandatory positional argument",
    b: "optional positional argument" = 1,
    c=2,
    *args:"add extra positional argument", #make it comment and check it
    kw1=100,
    kw2=200,
    kw3=300,
    **kwargs:"add extra keword arguments"
) ->"return nothing":
    """
    this function does nothing but have parameters

    """
    i = 10
    j = 20

print(my_func.__doc__)
print(my_func.__annotations__)
my_func.shorDescription = "this is a function that does nothing much"
print(my_func.shorDescription)
print(my_func.__defaults__)
print(my_func.__kwdefaults__)

sig  = inspect.signature(my_func)
print(sig)
print(dir(sig))
print(sig.parameters)

for k,v in sig.parameters.items():
    print('Key: ',k)
    print('Name: ',v.name)
    print('Default: ',v.default)
    print('Name: ',v.annotation)
    print('Name: ',v.kind)
    print("----------------------------------------")


#position only
print(divmod(8,2))  #divmod(x/y,x%y)
# print(divmod(a=2,b=3)) #not work because it require positional_only
for k,v in inspect.signature(divmod).parameters.items():
    # print(k,v)
    print(v.kind)