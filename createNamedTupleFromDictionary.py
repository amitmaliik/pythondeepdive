#alternative of dictionay
#Q=> when we will create tuple from dictionary 
#Ans=> when keys of dictionay are fixed

from collections import namedtuple
data_dict = {'key1':100,'key2':200,'key3':300}

data = namedtuple('Data',data_dict.keys())
d1 = data(key3=300,key1=100,key2=200)
print(d1)
d1 = data(**data_dict) #here argument pass as a key value argument(key1=100,key2=200,key3=300)
print(d1)

key_name = 'key1'
print(data_dict[key_name]) #for dictionary access the value of key , in this we can not set default value when key does't exist
print(data_dict.get(key_name,None)) #in this method we can set default value when key does't exist
print(data_dict.get('key10',None)) #it set default value None of that key does not exist

print(getattr(d1,key_name)) #for namedTuple access the value of key
print(d1.key1)

#now we will set default value in namedTuple when key does not exist
print(getattr(d1,'key10',None))

data_list = [
    {'key1':1,'key2':2},
    {'key1':3,'key2':4},
    {'key1':5,'key2':6,'key3':7},
    {'key1':100},
]

keys = set()
for dict_ in data_list:
    for key in dict_:
        keys.add(key)

print(keys) #here key may be in disorder means not as (key1,key2,key3)

keys = {key for dict_ in data_list for key in dict_} #fetch key using set comprehensive
print(keys) #here key may be in disorder means not as (key1,key2,key3)

# struct = namedtuple('Struct',sorted(keys))
struct = namedtuple('Struct',keys)
print(struct._fields)

#we want to create namedTuples from list of dictionary but dictionary has different no. of argument
#here namedTuple has total no. of keys so when we try create namedTuple from data_list[0](that has 
#only two keys but namedTuple required three values(key1,key2,key3))
# solution => set default values for all keys firstly

struct.__new__.__defaults__ = (None,) * len(struct._fields)

print(struct(key1=10)) #here we will see key2 and key3 has None

#first way create tuple list
tuple_list = []
for dict_ in data_list:
    tuple_list.append(struct(**dict_))

print(tuple_list)

#second way create tuple list
def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_}
    struct = namedtuple('Struct',keys)
    struct.__new__.__defaults__ = (None,) * len(struct._fields)
    return [struct(**dict_) for dict_ in dicts] #**dict_ means unpack the dictionary and argment
    #pass like as (key1=1,key2=2)

print(tuplify_dicts(data_list))
    



 