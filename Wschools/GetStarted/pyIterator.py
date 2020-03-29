tup = ("apple", "orange", "mango")
myIter = iter(tup)
print(next(myIter))
print(next(myIter))
print(next(myIter))


class myClass:
    def __iter__ (self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x
    
myNum = myClass()
myit = iter(myClass)

print(next(myit))
