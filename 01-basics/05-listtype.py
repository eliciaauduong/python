lst = [10, 20, "Elicia", -10, 30.5]
print(lst)

# list indexing
print(lst[3])

# list slicing
print(lst[3:5])

# repeat the list
print(lst * 4)

# count the number of elements
print(len(lst))

# add an element to the list
lst.append(40)
# delete an element by name
lst.remove("Elicia")
# delete an element by index
del(lst[1])
print(lst)

# remove all elements of a list
# lst.clear()
# print(lst)

# print the maximum element
print(max(lst))

# print the minimum element
print(min(lst))

# insert an element at a given index
lst.insert(3, 99)
print(lst)

# sort the elements
# default is ascending
# descending lst.sort(reverse = True)
lst.sort()
print(lst)

