import re, pyperclip
text = pyperclip.paste()
if(len(text) != 0):
    phoneSearchCriteria = re.compile(r'(\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{4})(\s*)?((ext|ext.|extension|extension.)?(\s*)(\d{2,4}))?')
    phone = phoneSearchCriteria.search(text)
    print(phone)
    emailSearch = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,4}', re.VERBOSE)
    email = emailSearch.search(text)
    print(email)
else:
    print("Emty string")