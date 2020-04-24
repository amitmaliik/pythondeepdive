def my_func():
    a = 24*60
    b = (1,2)*5
    c = 'abc'*3
    d = 'ab'*11 #it does not show in c python(11 times)
    e = 'the quick brown fox'*5  #it does not show in c python(5 times)
    f = ['a','b']*3 #it does not show in c python


print(my_func.__code__.co_consts)


a = [1,2,3]
b = {1,2,3}

def my_func1():
    if i in [1,2,3]: #if we use variable a it does not show any constant
        pass
    #list becomes touple

def my_func2():
    if i in {1,2,3}: #if we use variable b it does not show any constant
        pass
    #set becomes frozenSet

print(my_func1.__code__.co_consts)
print(my_func2.__code__.co_consts)

a = '123'
b = {'1','2','3'}
for i in range(300):
    a = set(a)
    print(id(a),' ',id(b))
    print(a,b)
    if a != b:
        print(a,b)
    # print(b)

# a = '123'
# b = ['1','2','3']
# for i in range(300):
#     a = list(a)
#     print(id(a),' ',id(b))
#     print(a,b)
#     if a != b:
#         print(a,b)
    




