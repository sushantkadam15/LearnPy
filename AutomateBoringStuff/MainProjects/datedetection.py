import re, pyperclip
date = pyperclip.paste()

searchCriteria = re.compile(r"(\d{2}(-|\/)\d{2}(-|\/)(\d{4}|\d{2}))")
#(/d{2}|/d{4})")
#([0-3][0-9][-|/][0-1][0-9][-|/][0-3][0-9][0-9][0-9]|[0-9][0-9])
dateSearch = searchCriteria.findall(date)
for i in dateSearch:
    print(i[0])