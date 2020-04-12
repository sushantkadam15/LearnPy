import pyinputplus as pyInp 
while True:
    print("Want to know how to keep an idiot busy for hours?")
    inputUser = pyInp.inputYesNo(">> ").lower()
    if inputUser == "yes":
        continue
    else:
        break