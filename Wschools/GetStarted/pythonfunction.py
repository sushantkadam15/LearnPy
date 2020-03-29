def myfunction():
    print("The function was called")

myfunction()

def calc(a,b):
    print(a+b)
    print(a-b)
    print(a/b)

calc(65,25)

#If you do not know how many arguments will be passed use * in args
def fruits(*frts):
    print("I love ", frts[1])

fruits("apple", "Mango", "Pineapple")

# If you do not know how many args will be passed and you are receiving an input form dictionary use **
studentInfo = {
    "Id" : 4522,
    "FirstName" : "Sushant",
    "LastName" : "Kadam"
}

def student(**std):
    print("The First name is ", studentInfo["FirstName"])

student()
