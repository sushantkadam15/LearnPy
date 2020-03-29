class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printName(self):
        print(self.fname, self.lname)

class student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = student("Mike", "Olson")
x.printName()