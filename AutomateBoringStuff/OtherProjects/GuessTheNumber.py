import random
def numGen():
    integer = random.randrange(1,21)
    return integer

def game():
    while True:
        gStart = input("Would you like to play the guessing game today? Select Y or N: ").lower()
        if(gStart == "y"):
            Usint = int(input("Enter a number between 1 to 20: "))
            k = numGen()
            if((k > Usint) and (Usint <= 100)):
                print("Your guess", Usint,"is lower than:", k)
            elif((k < Usint) and (Usint <= 100)):
                    print("Your guess", Usint," is higher than:", k)
            elif(k == Usint):
                print("Congratulations! You guessed the right number: ", k)
            else:
                print("Enter a valid input")
        elif(gStart == "n"):
            print("Sad to see you go")
            return False
        else:
            print("Please enter a valid Input")
game()