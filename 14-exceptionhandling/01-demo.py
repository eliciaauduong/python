try:
    import logging

    logging.basicConfig(filename="./14-exceptionhandling/05-mylog2.log", level=logging.DEBUG)

    f = open("./14-exceptionhandling/02-myfile", "w")
    a, b = [int(x) for x in input("Enter two numbers: ").split()]
    logging.info("Division in progress")
    c = a / b
    f.write("Wrtiting %d into file" %c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non-zero number")
    logging.error("Division by zero")
else:
    print("You have entered a non-zero number")
finally:
    f.close()
    print("File Closed")
print("Code after the exception")