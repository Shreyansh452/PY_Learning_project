def square(num):
    return num*num

l = [1, 2, 3]
 
# Method 1

l1 = []
for item in l:
    l1.append(square(item))
print(l1)

# Method 2
print(list(map(square,l)))