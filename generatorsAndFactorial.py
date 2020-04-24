#map,filter,zip return generators
#generators are not precalculated it calculate when request

list1  = [1,2,3,4]

result = filter(lambda x : x%2==0,list1) #here filter return generator(that are not precalculated)

for i in result: #here generator is called so calculation is done here
    print(i)

for i in result:#here we will not show any output because generator calculate one time(that are calculate previous loop)
    print(i)

list2 = [10,20,30]
list3 = [100,200,300,400,500,600]
# result = map(lambda x,y:x+y,list1,list2,list3) #we did not get any error here beacuse here map() gives generatos which are
#                                                #not precalculated, these are calculate when call,
# print(map(lambda x,y:x+y,list1,list2,list3))

# for i in result:  #here we call generators(here generators will be calculated)
# #we get error here because we pass three elements(list1,list2,list3) while in lamda we have only 2(x,y) variables
#     print(i)



print("##################factorial#####################")
def fact(x):
    return 1 if x<2 else x*fact(x-1)


print(fact(3))

print(list(map(fact,range(10)))) #get factorial of first 10 numbers

result = [fact(n) for n in range(10)]
print(result)

result = (fact(n) for n in range(10)) #it gives generators
print(result)
for i in result:
    print(i)

for i in result: #here we will not get any output because generatos called already in first for loop
    print(i)

print(list((fact(n) for n in range(10))))

result = [(fact(n) for n in range(10))] #it gives generators
print(result)

list1 = [1,2,3]
list2 = [11,22,34,44]
print([x+y for x,y in zip(list1,list2) if(x+y)%2==0])


