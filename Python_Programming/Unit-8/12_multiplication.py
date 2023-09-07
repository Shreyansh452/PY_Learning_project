def mul(n, i):
    if (i > 10):
        return
    print(n,"*",i,"=",n * i)
    return mul(n, i + 1)
n = 8
mul(n, 1)

 