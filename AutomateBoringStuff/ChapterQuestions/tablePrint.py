picnicItems = {
    "sandwhiches" : 4, 
    "apples" : 12,
    "cups": 4,
    "cookies": 80
}
title = " Picnic Items "
print((title.upper()).center(40, "*"))
for i in picnicItems:
    val = (picnicItems[i])
    itm = (i)
    print((str(itm).ljust(15) + str(val).rjust(15)).center(40))

