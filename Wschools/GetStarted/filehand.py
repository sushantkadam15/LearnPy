f = open("demo.txt")
print(f.read())
l = f.read()
for x in l:
    n = x.split(" ")
    print(n + "\n")
f.close()