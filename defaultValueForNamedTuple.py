from collections import namedtuple

def func(x,y=10,z=20):
    print(x,y,z)


func(1)
print(func.__defaults__)


point2D = namedtuple('Point2D','x,y,z,zzz')
# pt1 = point2D(1,2,3)
# print(pt1)
# print(id(pt1))

print(point2D.__new__.__defaults__)

#now we will set default value it will be from right side
point2D.__new__.__defaults__ = (4,5) #it means z has 4 and zzz has 5
pt1 = point2D(1,2) #here we will give value for x and y
print(pt1)
print(point2D.__new__.__defaults__)

pt1 = point2D(1,2,3) #we can set value after set the default value
print(pt1)