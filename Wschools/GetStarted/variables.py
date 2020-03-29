x = 8 #Number
y = 4.5 #Float
z = "String"
print(x,y,z)

a, b, c = "Linda", "Nancy", "Craigs"
print(a, b, c )

#Concatenation
print(a+b)

#Declaring Global variable inside a function
def var():
    global l
    l = "This is local variable which will appear to be global now"
var()
print(l)