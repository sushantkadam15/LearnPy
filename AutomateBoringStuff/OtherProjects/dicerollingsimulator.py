import random
def diceroll():
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    print("Dice1:",d1, "Dice2:", d2, "Sum:", d1+d2)

def game():
    while True:
        UserInput = input("Would you like to roll a dice? Select Y or N: ").lower()
        if(UserInput ==  "y"):
            diceroll()
        elif(UserInput == "n"):
            print("Sad to see you go")
            return False
        else:
            print("Invalid Input!! Please only select Y or N")
            
game()

