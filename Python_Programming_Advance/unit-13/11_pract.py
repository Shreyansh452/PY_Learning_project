from functools import reduce
l = [3, 4, 5, 1, 6, 7, 2, 9, 10]
a = reduce(max, l)
print(a)
