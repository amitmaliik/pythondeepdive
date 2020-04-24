import inspect
def aaa():
    pass


class XYZ:
    def abc():
        pass

a = XYZ()

#if method is inside class then it call method
#if method is not inside class is call function
print(inspect.isfunction(aaa),' ',inspect.ismethod(aaa))
print(inspect.isfunction(a.abc),' ',inspect.ismethod(a.abc))
print(inspect.isroutine(aaa),' ',inspect.isroutine(aaa)) #isroutine gives True when aaa is method or function