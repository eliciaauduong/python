s = {10, 20, 30, "XYZ", 10, 20, 10}

# add elements to the set
s.update([88, 99])

# remove an element from the set
s.remove(30)

print(s)
print(type(s))

# cannot add or remove elements
f = frozenset(s)
