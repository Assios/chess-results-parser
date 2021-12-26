import pandas as pd
import math
from tabulate import tabulate
import requests
import json


# Rapid: https://chess-results.com/tnr600852.aspx?lan=1&art=1&rd=3&flag=30

url = "https://chess-results.com/tnr600852.aspx?lan=1&zeilen=0&art=4&flag=30&prt=4&excel=2010" 

df = pd.read_excel(url, skiprows=[0, 1, 2, 3])

rows = []
rounds = [str(i) + ".Rd" for i in range(1, 23)]

class Player:
	def __init__(self, name):
		self.name = name
		self.rank = 0
		self.wins = 0
		self.draws = 0
		self.losses = 0
		self.tb1 = 0
		self.tb2 = 0
		self.tb3 = 0

	def __str__(self):
		return "%s – Points: %s" % (self.name, self.wins + self.draws * 0.5)

players = []

for index, row in df.iterrows():
	played_rounds = []

	if pd.isnull(row["Name"]):
		break

	player = Player(row["Name"].strip())

	player.rank = index + 1

	for r in rounds:
		try:
			played_rounds.append(row[r])
		except:
			break

	for r in played_rounds:
		point = str(r)[-1]

		if point == "1" or point == "+":
			player.wins += 1
		elif point == "0" or point == "-":
			player.losses += 1
		elif point == "½":
			player.draws += 1

	player.wins = int(player.wins)
	player.draws = int(player.draws)
	player.losses = int(player.losses)
	player.rank = int(player.rank)

	player.tb1 = row["TB1"]
	player.tb2 = row["TB2"]
	player.tb3 = row["TB3"]

	players.append(player)

with open("results.json", "a") as t:

	t.write("[")

	for i, player in enumerate(players):
		json.dump(player.__dict__, t)

		if (i < len(players)-1):
			t.write(",\n")

	t.write("]")
