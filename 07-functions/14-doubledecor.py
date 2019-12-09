def decor(fun):
    def inner():
        result = fun()
        return result * 2
    return inner

def num():
    return 18

funres = decor(num)
print(funres())

'''
OR

def decor(fun):
    def inner():
        result = fun()
        return result * 2
    return inner

@decor
def num():
    return 18

print(num())
'''