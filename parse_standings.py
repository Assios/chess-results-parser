import pandas as pd
import math
from tabulate import tabulate
import requests

ROUND_NUMBER = 9

url = "http://chess-results.com/tnr499129.aspx?lan=1&zeilen=99999&art=1&rd=%s&flag=30&prt=4" % ROUND_NUMBER

try:
	df = pd.read_excel(url, skiprows=[0, 1, 2, 3])

	rows = []

	for index, row in df.iterrows():
		rank = index + 1

		if pd.isnull(row["Name"]):
			break

		rows.append([rank, row["FED"], row["Unnamed: 3"], row["Name"], row[7]])

	with open("round_%s.md" % ROUND_NUMBER, "w") as f:
		f.write(tabulate(rows, headers=["Ranking","FED", "Title", "Name", "Points"], tablefmt="github"))
except:
	print("Round %s not available" % ROUND_NUMBER)
