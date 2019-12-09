dict1 = {1:"john", 2:"bob", 3:"bill"}
print(dict1)

print(dict1.items())

k = dict1.keys()
for i in k:
    print(i)

# print all values
v = dict1.values()
for i in v:
    print(i)

# use the key to print value
print(dict1[3])

# delete element by key
del dict1[2]
print(dict1)