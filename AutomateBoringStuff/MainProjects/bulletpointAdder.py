import pyperclip
text = pyperclip.paste().strip()
text = text.split("\n")
finList = open("finList.txt", "w")
for i in text:
    finList.write("* " + i + " \n")

finList.close()
finList = open("finList.txt")
print(finList.read())
