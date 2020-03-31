import ast, sys

def readList():
    openFile = open("inventory.txt", "r")
    getContent = openFile.read()
    openFile.close()
    contenDictionary = ast.literal_eval(getContent)
    TotalItem = 0
    for x in contenDictionary:
        print("\t", x, contenDictionary[x])
        val = int(contenDictionary[x])
        TotalItem += val
    print("\t Total Item: ", TotalItem, "\n\n")
    

def writeList():
    openFile = open("inventory.txt", "r")
    getContent = openFile.read()
    contenDictionary = ast.literal_eval(getContent)
    openFile.close()
    print("Please enter the Item you would like to add: ")
    key = input("> ").lower()
    if key in contenDictionary:
        print("This item already exists. Would you like to update?")
        ans = input("Select Y or N: ").lower()
        if(ans == "y"):
            print("Please enter the number of", key, ":")
            value = int(input("> "))
            contenDictionary[key] = value
        else:
            print("you will now return to main menu")
    else:
        print("Please enter the number of", key, ":")
        value = int(input("> "))
        contenDictionary[key] = value
    openFile = open("inventory.txt", "w")
    openFile.writelines(str(contenDictionary))
    openFile.close()


while True:
    print("What would you like to do todat?: ")
    print("\t Type V to view your Inventory: ")
    print("\t Type A to add or update your inventory: ")
    print("\t Press any other key to EXIT ")
    usrInput = input(">> ").lower()
    if(usrInput == "v"):
        readList()
    elif(usrInput == "a"):
        while True:
            writeList()
            exitCommand = input("Press x to exit or hit any key to continue: ").lower()
            if(exitCommand == "x"):
                break
            else:
                writeList()
    else:
        print("Have a nice day!!!")
        sys.exit()
        
