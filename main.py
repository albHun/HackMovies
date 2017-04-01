from json import json

from Analytics import findBestAndWorst
from Analytics import analyze



# Opening the json file and parsing it
with open("data.json") as data_file:
	data = json.load(data_file)

# Getting the information out from file
"""
This waits to be specified with the incoming data.
"""

X = data["word vectors"]
ratings = data["movie ratings"]

# Using functions defined in Analytics.py to briefly analyze the data
movieIndicesClustered = analyze(X)
bestIndices, worstIndices = findBestAndWorst(X, ratings)

print("Clusters best movies belong to")
for i in bestIndices:
	for cluster, indiceList in movieIndicesClustered.iteritems():
		if i in indiceList:
			print(cluster)

print("Clusters worst movies belong to")
for i in worstIndices:
	for cluster, indiceList in movieIndicesClustered.iteritems():
		if i in indiceList:
			print(cluster)