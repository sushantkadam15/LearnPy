import random, pyinputplus, os, pathlib, time
capitals = {'Alabama': 'Montgomery', 
 'Alaska': 'Juneau', 
 'Arizona': 'Phoenix',
 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
 'Connecticut': 'Hartford', 
 'Delaware': 'Dover', 
 'Florida': 'Tallahassee',
 'Georgia': 'Atlanta', 
 'Hawaii': 'Honolulu', 
 'Idaho': 'Boise', 
 'Illinois': 'Springfield', 
 'Indiana': 'Indianapolis', 
 'Iowa': 'Des Moines', 
 'Kansas': 'Topeka', 
 'Kentucky': 'Frankfort', 
 'Louisiana': 'Baton Rouge', 
 'Maine': 'Augusta', 
 'Maryland': 'Annapolis', 
 'Massachusetts': 'Boston', 
 'Michigan': 'Lansing', 
 'Minnesota': 'Saint Paul', 
 'Mississippi': 'Jackson', 
 'Missouri': 'Jefferson City', 
 'Montana': 'Helena', 
 'Nebraska': 'Lincoln', 
 'Nevada': 'Carson City', 
 'New Hampshire': 'Concord', 
 'New Jersey': 'Trenton', 
 'New Mexico': 'Santa Fe', 
 'New York': 'Albany',
 'North Carolina': 'Raleigh', 
 'North Dakota': 'Bismarck', 
 'Ohio': 'Columbus', 
 'Oklahoma': 'Oklahoma City',
 'Oregon': 'Salem', 
 'Pennsylvania': 'Harrisburg', 
 'Rhode Island': 'Providence',
 'South Carolina': 'Columbia', 
 'South Dakota': 'Pierre', 
 'Tennessee': 'Nashville', 
 'Texas': 'Austin', 
 'Utah': 'Salt Lake City', 
 'Vermont': 'Montpelier', 
 'Virginia': 'Richmond', 
 'Washington': 'Olympia', 
 'West Virginia': 'Charleston', 
 'Wisconsin': 'Madison', 
 'Wyoming': 'Cheyenne'
 }

def quizTest():
    question = 0
    totalScore = 0
    Leng = len(capitals)
    conList = list(capitals.keys())
    capList = list(capitals.values())
    IndexVal = Leng - 1
    while True:
        curCont = conList[random.randint(0 , IndexVal)]
        finalAns = capitals.get(curCont)
        options =  random.sample(set(capList), 3)
        while finalAns in options:
            options = random.sample(set(capList), 3)
        ansList = [finalAns]
        for i in options:
            ansList.append(i) 
        curQuestion = "\nWhat is the capital of " + curCont + " ? \n"
        createUserTest.write(curQuestion + "\n")
        print(curQuestion)
        random.shuffle(ansList)
        writeOptions = ""
        for i in ansList:
            writeOptions = writeOptions + "* " +i + "\n"
        createUserTest.write(writeOptions + "\n")
        userAnswer = pyinputplus.inputMenu(ansList, lettered=True)
        if userAnswer == finalAns:
            totalScore += 1
            print("\nCorrect answer!\n")
            createUserTest.write(f"\nAnswer Selected: {userAnswer}")
        else:
            print(f"\nIncorrect answer. The correct answer is {finalAns} \n")
            createUserTest.write("\nAnswer Selected: " + userAnswer + ". Correct Answer: " + finalAns + "\n" )
        question += 1
        if question > 20:
            break
    if totalScore >= 10:
        print("Congratulations you passed! Your score is", totalScore)
        createUserTest.write(f"Candidate passed with final score of: {totalScore}")
    else:
        print("Attempt failed! Your score is", totalScore)
        createUserTest.write(f"\n\nCandidate failed with final score of: {totalScore}") 

print("Welcome to the Geography test.")
print("Please enter your Fullname")
studentName = pyinputplus.inputStr(">> ")
print("Please enter your studentID ")
studentID = pyinputplus.inputInt(">> ", min=1, max=50)
currentPath = pathlib.Path.cwd()
testFolder = pathlib.Path(currentPath, "testResults")
os.chdir(testFolder)
folderName = f"{str(studentID)}-{str(studentName)}.txt"
dirFile = os.listdir()
if folderName in dirFile:
        print("You have already submitted your test.")
else:
    createUserTest = open(f"{str(studentID)}-{str(studentName)}.txt", "w")
    print("You will now be prompted with 20 quiz questions. This test can only be submitted once. All the best. \n")
    createUserTest.close()
    createUserTest = open(f"{str(studentID)}-{str(studentName)}.txt", "a")
    createUserTest.write(f"Student ID: {studentID} \n")
    createUserTest.write(f"Student Name: {studentName} \n")  
    quizTest()









