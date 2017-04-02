# K-means minibatch clustering
import time
import numpy as nu
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

# Given a dataset X, return the labels of entries in X
# Default K = 8
def KMeansClustering(X, n_clusters=8, tol = 1e-4):
	time0 = time.time()
	clu = KMeans(n_clusters=n_clusters, verbose = True, tol = tol)
	clu.fit(X)
	print(time.time() - time0)
	return clu.predict(X)

def DBSCANClustering(X):
	time0 = time.time()
	clu = DBSCAN()
	print(time.time() - time0)
	return clu.fit_predict(X)