import pprint

person = {
    "firstName" : "Sushant",
    "lastName" : "Kadam",
    "age" : 34
}

for i in person.values():
    print(i)

for i in person.keys():
    print(i)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)