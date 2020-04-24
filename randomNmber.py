import random
print(random.random())

#suffle a list
l1 = [1,2,3,4,5,6,7,8,9]
print(sorted(l1,key = lambda x:random.random()))