a = int(input("Enter the first number:\n"))
b = int(input("Enter the second number:\n"))
c = int(input("Enter the third number:\n"))
d = int(input("Enter the fourth number:\n"))

if(a>b and a>c and a>d):
    print("The greater number is:",a)
elif(b>a and b>c and b>d):
    print("The greaternumber is:",b)
elif(c>b and c>a and c>d):
    print("The greater number is :",c)
elif(d>a and d>b and d>c):
    print("The greater number is:",d)
else:
    print("False")