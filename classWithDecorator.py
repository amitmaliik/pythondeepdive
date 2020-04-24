class Rectangle:    
    #note when we use width at the place of width in __init__ then it will get infinite loop
    #in else part of @width.setter
    def __init__(self,height,width):        
        self._width = width  #setter will be called here
        self._height = height  

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,width):
        if width < 0:
            raise ValueError('value can not be negative')
        else:
            self._width = width


    # def __str__(self):
    #     return "Rectangle : width {0} and height {1}".format(self._width,self._height)

    # def __repr__(self):
    #     return "Rectangle({0} , {1})".format(self._width,self._height)

    # def __eq__(self,other):
    #     if isinstance(other,Rectangle):
    #         return self._width == other._width and self._height == other._height

    #     else:
    #         return False


rec = Rectangle(10,-12)
rec1 = Rectangle(10,12)
print(rec.width)
# print(str(rec))
print(rec)
print(rec == rec1) #if we do not write __eq__(self) manualy then it compare as object,here we write __eq__(self) and compare values of their

print(rec is rec1)  # it is use for compare object, is operator use for compare object