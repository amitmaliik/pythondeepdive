#munkeyPatching means add property or method at run time

from fractions import Fraction

f = Fraction(2,3)
print(f.numerator)
print(f.denominator)

Fraction.speak = 100 #here we add speak property dynamically
print(f.speak)

Fraction.is_integral = lambda self:self.denominator == 1 #if denominator is 1 then it return true
f1 = Fraction(2,3)
f2 = Fraction(64,8) #it is like as (8,1)
print(f1)
print(f2)

print(f1.is_integral())
print(f2.is_integral())