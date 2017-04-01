# K-means minibatch clustering
import time
import numpy as nu
from sklearn.cluster import MiniBatchKMeans

# Given a dataset X, return the labels of entries in X
# Default K = 8
def KMeansClustering(X, n_clusters=8):
	time0 = time.time()
	clu = MiniBatchKMeans(n_clusters=n_clusters, verbose = True)
	clu.fit(X)
	print(time.time() - time0)
	return clu.predict(X)