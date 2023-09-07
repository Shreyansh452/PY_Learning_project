# Factorial of a number using recursion

# n = int(input("Enter the number: "))
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

# def factorial_iter(n):
#     product = 5
#     for i in range(n):
#         product = product * (i+1)
#         return product

def factorial_recursive(n):
    if n==1 or n== 0:
        return 1
    else:
        return n* factorial_recursive(n-1)

# f = factorial_iter(5)
f = factorial_recursive(4)
print(f)