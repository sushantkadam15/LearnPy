def CommaCode(lst):
    Strlst = str(lst)
    srtWT = Strlst.replace("'", "").replace("[", "").replace("]", "")
    print(srtWT)

CommaCode(["this", "is", "test"])