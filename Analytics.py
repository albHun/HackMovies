# Data analytics on clustered data

import numpy as np
from KMeans import KMeansClustering

def analyze(X, n_clusters):
	"""
	This function takes the vector matrix and number of clusters wanted
	and returns a dictionaries of lists of the vectors.
	"""
	X_labels = KMeansClustering(X, n_clusters)
	wVectorsClustered = dict()
	for i in range(0, n_clusters):
		wVectorsClustered[i] = []
	for j in range(len(X)):
		wVectorsClustered[X_labels[j]].append(X[j])
	return wVectorsClustered

"""
testList = list()
for i in range(0, 50):
	testList.append([i, i])
print(analyze(testList, 8))
"""