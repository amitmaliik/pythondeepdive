name = "python"
print(f"{name} rocks")

sq = lambda x : x**2
a = 10
b = 4
print(sq(a) if b>5  else a)

print(f"{(lambda x : x**2)(a) if b>3 else a}")