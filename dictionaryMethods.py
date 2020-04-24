d1 = {"a":1,"b":2,"c":3,"d":4}
d2 = {"b":5,"c":6,"e":20}
d1.update(d2)
# d = d1.update(d2) #not work
print(d1)

print("##### move from first to last #####")

dic1 = {"a":1,"b":2,"c":3,"d":4}
dic1["a"] = dic1.pop("a")
print(dic1)

print("##### move from last to first #####")
dic1 = {"a":1,"b":2,"c":3,"d":4}
for i in range(len(dic1)-1):
    key = next(iter(dic1.keys()))
    print(key)
    dic1[key] = dic1.pop(key)

print(dic1)

print("##### pop last item #####")
dic1 = {"a":1,"b":2,"c":3,"d":4}
dic1.popitem()
print(dic1)

print("##### pop first item #####")
dic1 = {"a":1,"b":2,"c":3,"d":4}
key = next(iter(dic1.keys()))
dic1.pop(key)
print(dic1)