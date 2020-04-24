# from functools import operator
import operator
x = 2+3j
f = operator.attrgetter('real')
print(f(x))

# print(dir(operator))
print(operator.add(1,2))
print(operator.mul(1,2))
print(operator.truediv(10,3))
print(operator.floordiv(15,2))


from functools import reduce

print(reduce(lambda x,y : x*y,[1,2,3,4])) # still i did not get how pass three element in lamda in using reduce

#using operator we can do without lamda function

print(reduce(operator.mul,[1,2,3,4]))
print(operator.lt(10,3))
print(operator.truth([])) #empty list is false
print(operator.truth([1]))
print(operator.truth(''))
print(operator.truth(None))
print(operator.truth([0])) #list with any element is True
print(operator.truth(0))
print(operator.truth(1))
print(operator.is_("abc","def"))
print(operator.is_("abc","abc"))

my_list = [1,2,3,4]
print(my_list[1])

print(operator.getitem(my_list,3)) #it require two elements 

#if sequence is mutable then we can delete or set item
my_list[1] = 100
print(my_list)

del my_list[1]
print(my_list)

#now we use operator for set and delete the item
my_list = [1,2,3,4]
operator.setitem(my_list,1,100)
print(my_list)
operator.delitem(my_list,1)
print(my_list)

print("############################ itemgetter ##############################")
my_list = [1,2,3,4]
f = operator.itemgetter(1) #here we pass index
print(f(my_list))
f = operator.itemgetter(1,3)
print(f(my_list))

print("############################ attrgetter ##############################")
class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('testing method is called')

    def test1(self,a):
        print('testing method with variable is called '+str(a))

    def test2(self,a,b,*,e):
        print('testing method with variable is called '+str(a)+" "+str(b)+" "+str(e))


obj = MyClass()

f = operator.attrgetter('a') #attrgetter require variable name, not the index like itemgetter
print(f(obj))

print(obj.a)
my_var = 'a'
# print(obj.my_var) #not work

f = operator.attrgetter(my_var) #attrgetter require variable name, not the index like itemgetter
print(f(obj))

f = operator.attrgetter('a') #attrgetter require variable name, not the index like itemgetter
print(f(obj))

f = operator.attrgetter('a','b') #attrgetter require variable name, not the index like itemgetter
print(f(obj))

f = operator.attrgetter('a','test') #attrgetter require variable name, not the index like itemgetter
print(f(obj))  #it return test method
f(obj)[1]() #here return method and call it

f = operator.attrgetter('test1') #attrgetter require variable name, not the index like itemgetter
f(obj)(100)

a,b,test = operator.attrgetter('a','b','test')(obj) #attrgetter require variable name, not the index like itemgetter
test()

complexList1 = [2+3j,4+5j,-1-3j]
#sort according real part of complex number
def fun(x):
    return x.real

print(sorted(complexList1, key = fun))
print(sorted(complexList1, key = lambda x : x.real))
print(sorted(complexList1, key = operator.attrgetter('real'))) 
#when we use key = fun then one by one object of complexList1 pass,same here we use 'real' as object proerty name and object pass automatically

l = [(3,1,2),(1,1,2),(0,),(6,1,2),(2,3),(3,2,4)]
print(sorted(l,key = lambda x:x[0]))
print(sorted(l,key = operator.itemgetter(0)))

f = operator.attrgetter('test')
f(obj)()
f = operator.attrgetter('test1')
f(obj)(100)
f = operator.attrgetter('test2')
f(obj)(100,200,e=300) #here we will pass 100,200 as positional argument and e = 300 as keyword argument 

f = operator.methodcaller('test')
f(obj)
f = operator.methodcaller('test1',100)
f(obj)
f = operator.methodcaller('test2',100,200,e=300) #here we will pass 100,200 as positional argument and e = 300 as keyword argument 
f(obj)



complexList1 = [2+3j,4+5j,-1-3j]
#sum of real number
fun = lambda x : x.real
result = 0
for e in complexList1:
    result += fun(e)
print(result)

print(reduce(lambda x,y : x.real+y.real,complexList1))
    


# print("#####################################################")
# f = lambda x,y,z : x+y+z

# def fun(fn,sequence):
#     result = sequence[0]+sequence[1] + sequence[2]
#     print(result)
#     # for e in sequence[3::2]:
#     for index in range(3,len(sequence),2):#result will be x and next two element will be y and z
#         if(index+1 <= len(sequence)-1):
#             result = f(result,sequence[index],sequence[index+1])
#             print(result)
#     # print(result)

# fun(f,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
        

