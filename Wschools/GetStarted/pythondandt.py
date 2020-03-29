import datetime 

date = datetime.datetime.now()
year = date.year
month = date.month
tday = date.day
print(tday, "/", month, "/", year)

Day = date.strftime("%A")
print(Day)
