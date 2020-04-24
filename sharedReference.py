a = "hello"
b = "hello"

print(hex(id(a)))
print(hex(id(b)))

b = b + " world"
print(hex(id(b)))
print(a)
print(b)

a = [1,2,3]
b = a
print(hex(id(a)))
print(hex(id(b)))

a.append(100)
print(hex(id(a)))
print(hex(id(b)))
print(a)
print(b)


a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))
print("hello")

for i in range(100):
    a = 5000
    b = 5000
    print(i)
    if(hex(id(a)) != hex(id(b))):
        print(hex(id(a)))
        print(hex(id(b)))


a = None  #None represent empty object
b = None
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(None)))

if(a == None):
    print('compare using == operator')

if(a is None):
    print('compare using is operator')

a = 10
b = 10.0
print(hex(id(a)))
print(hex(id(b)))

if(a == b):  #logically 10 == 10.0
    print('compare using == operator')

if(a is b):
    print('compare using is operator')



a = 10 + 9j

if(a == b):  #logically 10 == 10.0 , here it compare 10 value of 10+0j to value of b that is 10.0
    print('compare using == operator')

if(a is b):
    print('compare using is operator')

a = int()
print(a)

a = int(18)
print(a)

a = int('110', base = 2)  #'110' is binary no.
print(a)

a = 10
b = int(10)
c = int('10') #get the number using base 10
d = int('1010',2) #get the number using base 2
print(a,b,c,d)
print(id(a),id(b),id(c),id(d))

a = 'hello world'
b  = 'hello world'
for i in range(300):
    if id(a) != id(b):
        print(id(a),' ',id(b))