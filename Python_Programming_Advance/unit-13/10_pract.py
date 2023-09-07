l = [23, 25, 5, 1, 5, 95, 100, 625, 30, 34, 80, 84, 73]

l10 = lambda num:num%5==0

print(list(filter(l10, l)))
