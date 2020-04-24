def dist_sq(x):
    return (x.real)**2 + (x.imag)**2

l1 = 1+1j
print(dist_sq(l1))

l1 = [1+1j,1-1j,3+3j,0]
print(sorted(l1,key = dist_sq))
print(sorted(l1,key = lambda x : (x.real)**2 + (x.imag)**2))


l2 =[(1,2),(4,5),(1,3),(2,4)] #this list of touple sorted by sum of tuple

print(sorted(l2,key = lambda x : x[0]+x[1]))
print(sorted(l2,key = lambda x : x[0]+x[1],reverse = True)) 

l3 = ['clle','velle','ansj','djjdu','uididia','kosooea','kkkfb'] #sort element by last character
print(sorted(l3,key = lambda x : x[-1]))

x = [1,2,3,4]
print(x)
x = set(x)
print(x)
for i in x:
    print(i)