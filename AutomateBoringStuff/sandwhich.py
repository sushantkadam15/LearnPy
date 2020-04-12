import pyinputplus
print("Would you like to have a sandwhich today?")
userInp = pyinputplus.inputYesNo(">> ").lower()
if userInp == "yes":
    print("What kind of bread would you like?")
    bread = pyinputplus.inputMenu(['wheat', 'white', 'sourdough'])
    meat = pyinputplus.inputMenu(['chicken', 'turkey', 'ham','tofu'])
    cheese = pyinputplus.inputYesNo("Would you like some cheese? >> ")
    if cheese == "yes":
        cheeseType = pyinputplus.inputMenu(["cheddar", "swiss","mozzarella"])
print(f"""
Your order is ready.
A sandwhich with:
       > {bread}
       > {meat}
       > {cheeseType}
""")
    