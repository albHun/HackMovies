# Special thanks to chuansun76 on kaggle for uploading
# the IMDB 5000 movie dataset

import os
# import seaborn as sns
# sns.set(style='white')

import json
import pandas as pd
from pandas.io.json import json_normalize
from sklearn.preprocessing import MinMaxScaler

#from Analytics import findBestAndWorst
#from Analytics import analyze


"""
# Dumping json that stores everything
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

# Supervised Learning
df = pd.read_csv("movie_metadata.csv")
print(df.shape)

df1 = df.dropna()
print(df1.shape)
print(df1.dtypes)

# Eliminating non-numerical fields
df2 = df1.select_dtypes(include=['int64','float64'])
# print(df2)

percentageProfit = 100 * (df2['gross'].values - df2['budget'].values) / df2['budget'].values
# print(percetageProfit[:5])
df2 = df2.drop('gross', 1)
df2 = df2.drop('director_facebook_likes', 1)

matrixed = df2.as_matrix()

minMaxScaler = MinMaxScaler()
df2_scaled = minMaxScaler.fit_transform(df2)
print(df2_scaled)


# df2.loc[:,'percentageProfit'] = pd.Series(percentageProfit, index=df2.index)
# g = sns.jointplot(x="title_year", y="percentageProfit",kind='scatter',size=10,\
#                   ylim = [0,110],xlim=[1980,2020],data=df2)
# g = sns.pairplot(df1,hue='content_rating')

# Unsupervised learning
# Getting the comment information out from file

"""
This waits to be specified with the incoming data.
"""




X = data["word vectors"]
ratings = data["movie ratings"]

# Using functions defined in Analytics.py to briefly analyze the data
movieIndicesClustered = analyze(X)
bestIndices, worstIndices = findBestAndWorst(X, ratings)


"""
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