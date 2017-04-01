# K-means minibatch clustering
import time
import numpy as nu
from sklearn.cluster import MiniBatchKMeans


def KMeansClustering(X):
	clu = MiniBatchKMeans(n_clusters=8, verbose = True)
	clu.fit(X)
	return clu.predict(X)
