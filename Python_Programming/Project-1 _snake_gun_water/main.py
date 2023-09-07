import random


def gameWin(comp, you):
    if comp == you :
        return 

    elif comp == 's':
     if you == 'w':
        return False
    elif you == 'g':
        return True

    elif comp == 'g':
     if you == 's':
        return False
    elif you == 'w':
        return True

    elif comp == 'w':
     if you == 'g':
        return False
    elif you == 's':
        return True


print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
print(randNo)
if randNo == 1 :
    comp = 's'
if randNo == 2 :
    comp = 'w'
if randNo == 3 :
    comp = 'g'
you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")

print(f"Computer choose {comp}")
print(f"you choose {you}")

a = gameWin(comp, you)
if a == None:
    print("The game is tie!")
elif a:
    print("you Win!")
else:
    print("You lose!")