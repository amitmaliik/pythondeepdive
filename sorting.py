l = ['c','B','D','a']
print(sorted(l))

print(ord('a')," ",ord('A'))

print(sorted(l,key = lambda x : x.upper()))

def fn(x):
    print('hello')
    print(x)
    print(type(x))
    # return [a.upper() for a in x] #we can iterate string so we use list comprehensive
    return x.upper()

print(sorted(l,key = fn)) #one by one element throw to fn(x) function
# print(fn(l))

l1 = {'abc':200,'def':300,'ghi':100}

print(sorted(l1))
print(sorted(l1,key = lambda x : l1[x])) #sorted according value

def fn1(x):
    return l1[x]

print(sorted(l1,key = fn1))
