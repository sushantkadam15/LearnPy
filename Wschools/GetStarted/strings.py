a = "This is a string  "
print(a[0:9])
b = len(a)
print(b)
s = a.strip(), a.lower(), a.upper(), a.replace("i","o")
print(s)


#escape characters in string

txt = "2 \\ 5"
print(txt)

txt = "2 \n 5"
print(txt)

txt = "this \r is text"
print(txt)

txt = "this \t is text"
print(txt)

txt = "this \bis text"
print(txt)

txt = "this is a title"
print(txt.title())