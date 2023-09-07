try:
    a = int(input("Enter a number:"))
    c = 1/a
    print(c)
except ValueError as e:
    print("Exception 1 occured")
    print(e)
except ZeroDivisionError as e:
    print("Exception 2 occured")
    print(e)

print("Thanks for using the code!")