dictn = {
    "Manufacture" : "Ford",
    "Model" : "Fusion",
    "Year" : 2013,
    "DriveType" : "Rare wheel drive"
    }
print(dictn)
print(dictn["Model"])
print(dictn.get("Year"))
dictn["Year"] = 2017
print(dictn.get("Year"))

