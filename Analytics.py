# Data analytics on clustered data

import numpy as np
from KMeans import KMeansClustering

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

def findBestAndWorst(X, ratings):
	"""
	Returning the indices of best-rated and worst-rated movies.
	"""
	ratingsSorted = sorted(ratings)
	int highRating = ratingsSorted[int(len(ratings) * 0.2)]
	int lowRating = ratingsSorted[int(len(ratings) * 0.8)]
	bestIndices = [i for i in range(0, len(ratings)) if ratings[i] > highRating]
	worstIndices = [i for i in range(0, len(ratings)) if ratings[i] < lowRating]
	return bestIndices, worstIndices



"""
testList = list()
for i in range(0, 50):
	testList.append([i, i])
print(analyze(testList, 8))
"""