from datetime import datetime,timezone
def info(self): #it provide object information
    results = []
    results.append('time is {0} '.format(datetime.now(timezone.utc)))
    results.append('class is {0} '.format(self.__class__.__name__))
    results.append('id is {0} '.format(hex(id(self))))

    for k,v in vars(self).items(): #vars is inbuild function that is used for get object key value
        results.append('{0} : {1} '.format(k,v))

    return results

def debug_info(cls): #it is decorator function,here we will decorate the class
    cls.debug = info
    return cls

class Person:
    def __init__(self,name,year):
        self.name = name
        self.year = year

    def say_hello(self):
        return "hello there"

#1st way
Person  = debug_info(Person)
p = Person('john','1999')
output  = p.debug()
print(output)

#2nd way
@debug_info #it means we pass Person class to debug_info()
class Person:
    def __init__(self,name,year):
        self.name = name
        self.year = year

    def say_hello(self):
        return "hello there"

p = Person('john','1999')
output  = p.debug()
print(output)


@debug_info
class Automobile:
    def __init__(self,make,model,year,topSpeed):
        self.make = make
        self.model = model
        self.year = year
        self.topSpeed = topSpeed
        self._speed = 0  

    @property #it is inbuild decorator
    def speed(self):        
        return self._speed

    @speed.setter
    def speed(self,newSpeed):
        if newSpeed > self.topSpeed:
            raise ValueError('speed can not be exceed to topSpeed')
        else:
            self._speed = newSpeed

auto = Automobile('ford','ford T',1965,100)
# auto.speed = 101 #it will throw valueError
auto.speed = 100
output = auto.debug()
print(output)
print(auto.speed)


 
