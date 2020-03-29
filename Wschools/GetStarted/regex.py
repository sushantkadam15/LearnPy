import re
txt = "The rain in spain"
x = re.search("The.*spain$", txt)
print(x)