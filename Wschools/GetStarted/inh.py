class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def namePrint(self):
        print("The name is: ", self.fname, self.lname)
class student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationYear = 2017
x = student("Sushant","Kadam")
print(x.graduationYear)
x.namePrint()