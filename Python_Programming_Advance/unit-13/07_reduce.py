from functools import reduce


def sum(a, b): return a+b


l = [1, 2, 3, 5, 6, 7]
val = reduce(sum, l)
print(val)
