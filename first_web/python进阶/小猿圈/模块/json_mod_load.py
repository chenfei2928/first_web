import json

f = open("game.json", "r")
d = json.load(f)
print(d["role"])
