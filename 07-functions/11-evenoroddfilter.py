lst = [10, 2, 33, 45, 89, 2]

result = list(filter(lambda x: x % 2 == 0, lst))
print(result) # gets address of filter unless list() around filter()

for i in result:
    print(i)