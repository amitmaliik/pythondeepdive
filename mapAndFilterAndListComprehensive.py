list1 = [1,2,3]
list2 = [14,15,16,22,24,28]
def sq(x):
    # print(x)
    return x**2

#map(func,*iterable)  #we can pass more than list
print(list(map(sq,list1)))
print('****************start****************')
for i in map(sq,list1): #map return iterator
    print('i ',i)

print('****************end******************')
def add(x,y):
    return x+y

print(list(map(add,list1,list2))) #if lists have different length then result list will be of short length
print(list(map(lambda x,y: x+y,list1,list2)))

#####################filter##########################
#filter(fun,iterable) #we can pass only one list

list1 = [0,1,2,3,4]
print(list(filter(None,list1))) #filter return value according to true or false here we did not pass any function
                                #while pass None , here filter assume 0 as False and other value as True

def isEven(x):
    return x%2 == 0

print(list(filter(isEven,list1)))
print(list(filter(lambda x : x%2==0,list1)))

#####################zip############################
#zip(*iterable)

list1  = [1,2,3]
print(list(zip(list1)))

list2 = [11,22,33,44]
print(list(zip(list1,list2))) #zip print no. of argument = sort length of lists

##################listComprehensive####################
#listComprehensive is alternative of map 
list1 = [1,2,3]
def sq(x):
    return x**2

print(list(map(sq,list1)))

result = []
for x in list1:
    result.append(x**2)

print(result)

print([x**2 for x in list1])

list2 = [11,22,33,44]
print(list(map(lambda x,y:x+y,list1,list2)))

#######now we will use list comprehensive#######
print([x+y for x,y in zip(list1,list2)])

#######filter with list comprehensive###########
list1 = [1,2,3,4]
print(list(filter(lambda x : x%2==0,list1)))


#######now we will use list comprehensive#######
print([x for x in list1 if x%2 == 0])

print([x if x%2 == 0 else x*2 for x in list1 ]) #it return even values from list1 and multiply by 2 of odd values