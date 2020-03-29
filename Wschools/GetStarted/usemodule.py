import mymodule
import platform
mymodule.calc(10,4)
print(mymodule.person1["FName"])
x = platform.system()
print(x)

x = dir(platform)
print(x)

for i in x:
    print(i)