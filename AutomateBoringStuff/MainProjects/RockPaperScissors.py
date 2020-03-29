import random, sys
def game():
    wins = 0 
    losses = 0
    ties = 0
    while True:
        print("Do you wan to play? Select Y or N")
        inp = input().lower()
        if(inp == "y"):
            print("Please select your input: R for Rock, P for Paper and S for Scissors")
            usrInp = input().lower()
            gameArray = ["r", "p", "s"]
            arrayIndex = random.randrange(3)
            compInp = gameArray[arrayIndex]
            if(usrInp == compInp):
                print("Tie")
                ties += 1
            elif(compInp == "r" and usrInp == "p"):
                print("computer chooses:", compInp,"You win")
                wins +=1
            elif(compInp == "s" and usrInp == "r"):
                print("computer chooses:", compInp,"You win")
                wins +=1
            elif(compInp == "p" and usrInp == "s"):
                print("computer chooses:", compInp,"You win")
                wins +=1
            elif(compInp == "p" and usrInp == "r"):
                print("computer chooses:", compInp,"You Lose")
                losses +=1
            elif(compInp == "r" and usrInp == "s"):
                print("computer chooses:", compInp,"You Lose")
                losses +=1
            elif(compInp == "s" and usrInp == "p"):
                print("computer chooses:", compInp,"You Wim")
                losses +=1
            else:
                print("computer chooses:", compInp,"Please enter a valid input")
                continue
        elif (inp == "n"):
            print("Your total score is: \n Wins:", wins, "Losses: ", losses, "Ties: ", ties)
            if(wins > losses):
                print("Congratulations! You won the game")
            return False
        else:
            print("Enter a valid input")
game()