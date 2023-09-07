# Syntax :
# list(filter(function, list))

def greater_than_5(num):
    if num>5:
        return True
    else:
        return False

l10 = lambda num: num>10

l = [3, 4, 5, 7, 9 , 9 , 3, 87, 83, 84, 93, 1] 
print(list(filter(greater_than_5, l)))
print(list(filter(l10, l)))                 # Prints all the elements which are greater than 10.
