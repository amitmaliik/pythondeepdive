#any object that can be called using the () operator is called callable
#callable method return None or value

#all classes are callable but instance of class may or may not be callable
#for making object callable use __call__() in class

#for check object is callable or not use callable(), here we will pass object inside in callable() method
print(callable(print))
print(callable("abc".upper))
print(callable(str.upper))
print(callable(callable))
print(callable(10))
print(callable('abc'))
# print(type('aaa'.upper()))
print(type('aaa'.upper))

print(dir('builtin_function_or_method'))

def aaa():
    pass
print(callable(aaa))

#here you will see hello on screen , print method return None
result = print('hello')
print(result)

#here append() will return None , while change in list
l = [1,2,3]
result = l.append(4)
print(result)

#here upper() return value like 'ABC'
s = 'abc'
result = s.upper()
print(result)

print('#################################test Class#####################################')
from decimal import Decimal
print(callable(Decimal))
a = Decimal('10.5')
print(callable(a)) #instance of class is not callable


class MyClass:
    def __init__(self,x=1):
        print('initializing the class')
        self.counter = x

print(callable(MyClass))

obj = MyClass(10)
print(callable(obj)) #here class object is not callable


#now we make class object callable
class MyClass:
    def __init__(self,x=1):
        print('initializing the class')
        self.counter = x

    def __call__(self,x=1):
        print('updating....')
        self.counter += x

print(callable(MyClass))

obj = MyClass(10)
print(obj.counter)
print(callable(obj)) #here class object is callable because we have __call__() in class

MyClass.__call__(obj,10)
print(obj.counter)

obj() #now we can call object like as obj()
print(obj.counter)
