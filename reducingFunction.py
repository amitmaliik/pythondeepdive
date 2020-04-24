list1 = [5,8,6,10,9]

maxValue = (lambda x,y : x if x>y else y)


max1 = list1[0]
for e in list1[1:]:
    max1 = maxValue(max1,e)    
print('it is max value ',max1)


print('####################################################################')
def _reduce(fn,sequence):
    max = sequence[0]
    for e in sequence[1:]:
        max = fn(max,e)
    print(max)

_reduce(lambda x,y : x if x>y else y,list1)

# _reduce(lambda x,y : x if x>y else y,{1,2,3,4}) 
#note => set not work here but it works with reduce

from functools import reduce
print(reduce(lambda a,b :a if a>b else b,list1))
print(reduce(lambda a,b :a if a<b else b,list1))
print(reduce(lambda a,b :a+b ,list1))
print(reduce(lambda a,b :a*b ,list1))
print(reduce(lambda a,b :a*b ,{1,2,3,4})) #here set work because we are using inbuilt reduce function 

print(max(list1))
print(min(list1))
print(sum(list1))
print(any(list1)) #return true if any element truthy in list1
print(all(list1)) #return true if every element truthy in list1

list2 = [0,'',None,100]
print(any(list2)) #return true if any element truthy in list2
print(all(list2)) #return true if every element truthy in list2
print(bool(0), ' ',bool(''), ' ',bool(None), ' ',bool(100))


multiplicationOfList = lambda a,b:a*b
def multiply(fn,sequence):
    # global result    
    result = sequence[0]
    print(id(result))
    for e in sequence[1:]:
        result = fn(result,e)
        print(id(result))
        # print(result)
    return result
result = multiply(multiplicationOfList,list1)
print(result)
print(id(result))

def fact(n):
    return reduce(lambda a,b :a*b,range(1,n+1))

print(fact(5))