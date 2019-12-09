num = int(input("Enter a number: "))

prime = True
for i in range(2, num):
    if (num % i == 0):
        prime = False

if prime == True:
    print("prime number")
else:
    print("not a prime number")