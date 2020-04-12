import re
PhoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = PhoneNumberRegex.search('My pjone number is 778-344-4037')
print("The phone number detected in the string " + mo.group())