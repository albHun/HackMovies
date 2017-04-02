# Data analytics on clustered data

import numpy as np
from KMeans import KMeansClustering
from KMeans import DBSCANClustering

def analyze(X, n_clusters = 8):
	"""
	This function takes the vector matrix and number of clusters wanted
	and returns a dictionaries of lists of the indices of movies.
	"""
	indicesList = list()
	for i in range(2, 6):
		X_labels = KMeansClustering(X, n_clusters, tol= (0.1**i))
		movieIndicesClustered = dict()
		for i in range(0, n_clusters):
			movieIndicesClustered[i] = []
		for j in range(len(X)):
			movieIndicesClustered[X_labels[j]].append(j)

		indicesList.append(movieIndicesClustered)

	return indicesList



"""
testList = list()
for i in range(0, 50):
	testList.append([i, i])
print(analyze(testList, 8))
"""