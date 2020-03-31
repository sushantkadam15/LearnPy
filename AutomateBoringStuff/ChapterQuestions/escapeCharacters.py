charWithQuotes = "Sushant\'s tickets are pending "
print(charWithQuotes)
charWithBackslash = "The date is 31\\04\\2020"
print(charWithBackslash)


#Others

#Indent
charWithIndent = "\t Name: \t Sushant"
print(charWithIndent)

charAtNewLine = "Please follow the steps below: \n \t Step1: Null"
print(charAtNewLine)

MultiLineString = """ Twinkle Twinkel Little Star
\t How I wonder what you are?"""

print(MultiLineString)

charLen = len(MultiLineString)
print(charLen)
print(MultiLineString[9:30])
if "Twinkle" in MultiLineString:
    print("Yes")

# String Manupulation
name = "Sushant"
age = 18
# Manupulating using %s
print("Hello! my name is %s and my age is %s" %(name,age))

#Manupulating using f-string
print(f'My name is {name} and age is {age+1} ')

