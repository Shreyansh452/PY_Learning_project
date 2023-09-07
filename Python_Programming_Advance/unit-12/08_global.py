a = 23 # global variable
def func1():
    global a 
    print(f"printing the first a {a}")
    a = 3 # local variable
    print(f"printing the second a {a}")  

func1()
print(f"printing the third a {a}")