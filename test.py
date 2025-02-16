import json as js
filename = "wholeJSON.json"
myfile = open(filename, mode="w", encoding="Latin-1")

player = {
    'PlayerName': "Rishat",
    'Points': 100
}
player2 = {
    'PlayerName': "Rist",
    'Points': 100
}

js.dump(player, myfile)
js.dump(player2, myfile)
myfile.close()