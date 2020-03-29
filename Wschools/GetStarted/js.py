import json
x = '''{
    "Name" : "Joe",
    "Color" : "White",
    "Height" : 180
}'''
y = json.loads(x)

print(y["Name"])

z = json.dumps(x)
print(z)