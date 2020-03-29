import random
import pyperclip

wordFile = open("mywords.txt")
wordList = wordFile.read().split()
fileLength = len(wordList)

def passwordGenerator():
    while True:
        UsrInput = input("Generate a password? Select Y or N: ").lower()
        if(UsrInput == "y"):
            indexIntOne = random.randrange(0,fileLength)
            indexIntTwo = random.randrange(0,fileLength)
            num = str(random.randrange(0,100))
            wordOne = wordList[indexIntOne].title()
            wordTwo = wordList[indexIntTwo].lower()
            output = wordOne + wordTwo + num
            pyperclip.copy(output)
            print(wordOne + wordTwo + num)
        elif(UsrInput == "n"):
            print("Have a nice day!")
            return False
        else:
            print("Enter a valid input")

passwordGenerator()

wordFile.close()
