#immutabel object has same reference
a = 10
b = 10

#mutabel object has different object
c = [1,2,3]
d = [1,2,3]
# d.append(100)

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(c)
print(d)