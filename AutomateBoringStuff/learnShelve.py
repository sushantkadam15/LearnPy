import shelve, sys, pyperclip
database = shelve.open("DATA")
task = (sys.argv[1]).lower()

if task == "save":
    copiedText = pyperclip.paste()
    database[sys.argv[2]] = copiedText
elif task == "list":
    for i in database:
        print(i)
elif task == "use":
    print(database[sys.argv[2]])
elif task == "delete":
    database.pop(sys.argv[2])
database.close()
