lst = [20, 30, 40, 234]
print(type(lst))

# NO SLICING OR REPETITION FOR BOTH

b = bytes(lst) # cannot be indexed
print(type(b))

b1 = bytearray(lst) # can be indexed
print(type(b1))
b1[2] = 33