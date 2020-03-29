class student:
    def __init__(self, fname, lname, sid, major):
        self.Firstname = fname
        self.LastName = lname
        self.SID = sid
        self.Major = major
    
    def comment(self):
        print("Hello my name is " + self.Firstname + " " + self.LastName)

s1 = student("Sushant", "Kadam", 1655, "Python")
s1.comment()
