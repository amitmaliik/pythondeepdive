from collections import namedtuple
#namedtuple i sfunction that return a class that inherit from tuple

Point2dClass = namedtuple('Point2d',['x','y'])  
#here Point2d is class returned by namedtuple this class has two property(x,y) and inherit from tuple
#so instance of this class will be tuple

##we can define class this way namedtuple
# Point2dClass = namedtuple('Point2d',('x','y')
# Point2dClass = namedtuple('Point2d','x,y')
# Point2dClass = namedtuple('Point2d','x y')


objectOfPoint2dClass = Point2dClass(10,20)
print(objectOfPoint2dClass.x)
print(objectOfPoint2dClass.y)
# print(objectOfPoint2dClass['x']) #not work

dictOfPoint2dClass = objectOfPoint2dClass._asdict()
print(dictOfPoint2dClass)
print(dict(dictOfPoint2dClass))
print(dictOfPoint2dClass['x']) #it work

print("#########product of vector and sum that##########")

Vector = namedtuple('Vector','x,y,z')
vc1 = Vector(1,2,3)
vc2 = Vector(1,1,1)
print(vc1)
print(vc2)

print(list(zip(vc1,vc2)))  #zip make (x1,x2)(y1,y2)(z1,z2)
print(zip(vc1,vc2))

listComprehensive = sum([e[0]+e[1] for e in zip(vc1,vc2)])
print(listComprehensive)

print(Vector._fields)