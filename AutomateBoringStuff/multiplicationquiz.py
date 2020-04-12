import random, pyinputplus
def MultiplicationGame():
    QuestionNo = 1

    userScore = 0
    gameStart = pyinputplus.inputYesNo("Would you like to play the multiplucation game?").lower()
    if gameStart == "yes":
        print("Get ready to answer 10 questions.")
        while True:
            int1 = random.randint(10,100)
            int2 = random.randint(1,10)
            multipliedValue = int1*int2
            print("Question", QuestionNo,":", int1, "X",int2," = ")
            userAnswer = pyinputplus.inputNum(">> ")
            QuestionNo +=1
            if userAnswer == multipliedValue:
                print("Correct!")
                userScore += 1
            else:
                print("Incorrect Answer")
            if QuestionNo > 10:
                break
        print("Your final score is", userScore)
    else:
        print("Have a nice day!")
    

MultiplicationGame()