tpl = (40, 50, 40, "XYZ")
print(tpl)
print(type(tpl))

# repeat tuple
print(tpl * 3)

# count the number of times an element occurs
print(tpl.count(40))

# return the index of an element
print(tpl.index("XYZ"))

# convert list to tuple
lst = [67, 34, "XYZ"]
print(type(lst))
tpl1 = tuple(lst)
print(type(tpl1))
print(tpl1)