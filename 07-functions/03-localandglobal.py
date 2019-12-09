x = 123 # global variable

def display():
    x = 678 # local variable
    print(x)
    print(globals()['x']) # pass the name of the global variable

print(x)
z = display
z()
z()
z()