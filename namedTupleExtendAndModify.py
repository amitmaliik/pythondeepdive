from collections import namedtuple

point2d = namedtuple('Point2d','x y z')

pt1 = point2d(1,2,3)
print(pt1.x)

#here using tuple slice
current = pt1[:2] #it gives tuple
print(current)

#here using unpack, except last element
*current,_ = pt1 #_ represent the last element,here current give the list
#*current,z = pt1 #we can use variable name also

print(*current)
print(current)

print('###################now we modify the namedtuple###################')
#when we modify namedTuple then it create a new tuple

point2d = namedtuple('Point2d','x y z')
pt1 = point2d(1,2,3)
print(id(pt1))

pt1 = pt1._replace(z=4,y=6) #here change modify the namedTuole but it create a new tuple
print(id(pt1))

print('###################now we extend the namedtuple###################')
#when we extend namedTuple then it create a new tuple
point2d = namedtuple('Point2D','x,y,z')
pt1 = point2d(1,2,3)
print(id(pt1))
print(pt1._fields)
# pt1._fields += ('zzz',) #we can not assign value to pt1._fields because it is read only
# print(pt1._fields)
point3d = namedtuple('Point3D',pt1._fields+('zzz',)) #here we create a new tuple using previous tuple fields 
pt3 = point3d(*pt1,100) #here we pass pt1 values and one extra value(100)
print(pt3)





