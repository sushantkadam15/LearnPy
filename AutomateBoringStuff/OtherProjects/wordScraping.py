oldFile = open("words.txt")
textImport = oldFile.read().split()
newFile = open("mywords.txt", "x")
for i in textImport:
    if len(i) < 7:
        print(i, len(i))
        newFile.write(i + "\n")

newFile.close()
oldFile.close()
