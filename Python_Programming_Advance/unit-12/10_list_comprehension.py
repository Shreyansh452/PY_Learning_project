from optparse import Values


a = [3, 4, 2, 5, 23, 24]

# b = []
# for item in a :
#     if item%2 == 0:
#         b.append(item)
#  print(b)

# This is shortcut for whatever written above
b = [i for i in a if i%2==0]
print(b)

t = [2, 3, 1, 3, 2, 1]       # It is set so it dont repeat Values
s = {i for i in t}
print(s)

