import re, pyperclip
areaCodeList = open("areacode.txt")
areaCodeString = areaCodeList.read()
areaCodeList.close()
newList = areaCodeString.replace(",", ",")
newList = newList.replace("\t", " ,")
newList = newList.split("\n")
finalList = []
for i in newList:
    tempList = i.split(",")
    finalList.append(tempList)

finalList[9].extend([0,1])


searchCriteria1 = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
searchCriteria2 = re.compile(r"\d\d\d \d\d\d \d\d\d\d")
searchCriteria3 = re.compile(r"\d\d\d\d\d\d\d\d\d\d")
serchCriteria = [searchCriteria1, searchCriteria2, searchCriteria3]

userNumber = input("> ")
for i in serchCriteria:
    result = i.search(userNumber)
    if result != None:
        verifiedNumber = result.group()
        userAreaCode = str(verifiedNumber[0:3])
        #Array to search on finalList
        for i in finalList:
            area = str(i)
            newArea = str(area)
            r = re.compile(r'.*'+ str(userAreaCode) + (".*"))
            n = r.search(area)
            if n != None:
                print(" Number entered: " + userNumber + " \n The area code " + userAreaCode + " belongs to " + i[0])

