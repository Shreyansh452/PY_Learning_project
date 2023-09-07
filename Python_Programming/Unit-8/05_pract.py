from doctest import REPORTING_FLAGS


first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))
if first>second and first>third:
    print("first is greater")
if second>first and second>third:
    print("second is greater")
if third>first and third>second:
    print("third is greater")