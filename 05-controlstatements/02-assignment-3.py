m, p, c = [int(x) for x in input("Enter your grades for maths, physics and chemistry: ").split()]

if m >= 35 and p >= 35 and c >= 35:
    average = (m + p + c) / 3
    if average <= 59:
        print("C")
    elif average <= 69:
        print("B")
    else:
        print("A")
else: 
    print("You have failed the exam.")