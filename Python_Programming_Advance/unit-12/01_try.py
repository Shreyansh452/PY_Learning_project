from traceback import print_tb


while(True):
    print("Press q to quit")
    a = input("Enter a number:")
    if a == 'q':
        break
    try:
        print("Trying...")
        a = int(a)
        if a > 9:
            print("You entered a number greater than 9")
    except Exception as e:
        print("Your input resulted in an error:{e}")

print("Thanks for playing the game!")