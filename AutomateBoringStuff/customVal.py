import pyinputplus
def inputVal():
    while True:
        inputValue = pyinputplus.inputStr(">>> ")
        x = 0
        for i in inputValue:
            iasInt = int(i)
            x += iasInt
        if x != 10:
            print("The sum of the num do not add to 10, it is",x)
        else:
            print("Congratulations! You got it right.")
            break 


inputVal()