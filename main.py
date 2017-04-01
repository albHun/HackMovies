import os

import json
import pandas as pd

from Analytics import findBestAndWorst
from Analytics import analyze
"""
path = 'F:\MyProjects\MLH_prime\data\meta'
files = list()
for j in range(1, 251):
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path,i)) and i.startswith("%s_" % j):
            with open(os.path.join(path,i)) as data_file:
                data = json.load(data_file)         
                files.append(data)
with open("data.json", "w") as outfile:
    json.dump(files, outfile)
"""



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
"""