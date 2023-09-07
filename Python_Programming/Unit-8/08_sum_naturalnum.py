def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)

num = int(input("Enter a number: "))
print("The sum is: ", sum(num))