# Data analytics on clustered data

import numpy as np
from KMeans import KMeansClustering
from KMeans import DBSCANClustering

def analyze(X, n_clusters = 8):
	"""
	This function takes the vector matrix and number of clusters wanted
	and returns a dictionaries of lists of the indices of movies.
	"""
	X_labels = KMeansClustering(X, n_clusters)
	movieIndicesClustered = dict()
	for i in range(0, n_clusters):
		movieIndicesClustered[i] = []
	for j in range(len(X)):
		movieIndicesClustered[X_labels[j]].append(j)

	return movieIndicesClustered




"""
testList = list()
for i in range(0, 50):
	testList.append([i, i])
print(analyze(testList, 8))
"""