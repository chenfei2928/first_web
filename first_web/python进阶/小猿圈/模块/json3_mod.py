import json


d = {
    "name":"chen",
    "role":"police",
    "blood": 76,
    "weapon":"ak47"
}

alive_palyers = ['alex','jack','rain']


print(json.dumps(d))

print(type(json.dumps(d)))


f = open("game.json", 'w')
json.dump(d,f)
#json.dump(alive_palyers,f)   #多次dump后，load时会报错



