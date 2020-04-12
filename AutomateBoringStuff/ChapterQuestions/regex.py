import re
phoneNumberRegex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo = phoneNumberRegex.search("My phone number is 778-344-4037")
print(mo.group())

# Using escape characters in regex to search special characters
escape = re.compile(r"\(\d{3}\) \d{3}-\d{4}")
specialCharString = escape.search("My phone number is (778) 344-4037")
print(specialCharString.group())

# Using | to match multiple characters. Returns the first matched character
searchCriteria1 = re.compile(r"Batman|Tina Fey")
text1 = searchCriteria1.search("Batman and Tina Fey are good actors.")
text2 = searchCriteria1.search("Tina Fey and Batman are good actors.")
print(text1.group(), text2.group())

#Searching strings that have common beginnings
searchCriteria2 = re.compile(r"Bat(man|woman|mobile)")
text3 = searchCriteria2.search("Batman loves Batmobile and Batwoman")
print(text3.group())

#Optional search with ?
searchCriteria3 = re.compile(r"Bat(wo)?man")
text4 = searchCriteria3.search("This is Batman")
print(text4.group())
text5 = searchCriteria3.search("This is Batwoman")
print(text5.group())

# Matching 0 or more with * (repeating characters in string)
searchCriteria4 = re.compile(r"Bat(wo)*man")
text6 = searchCriteria4.search("This is Batwowoman")
print(text6.group())