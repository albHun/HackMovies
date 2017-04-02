# Special thanks to chuansun76 on kaggle for uploading
# the IMDB 5000 movie dataset
import time
import os
# import seaborn as sns
# sns.set(style='white')
import numpy as np
import json
import pandas as pd
from pandas.io.json import json_normalize
import csv
from tempfile import TemporaryFile


from sklearn.preprocessing import MinMaxScaler

#from Analytics import findBestAndWorst
from Analytics import analyze


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
print(df1.shape)

# Eliminating non-numerical fields
df2 = df1.select_dtypes(include=['int64','float64'])
# print(df2)

percentageProfit = 100 * (df2['gross'].values - df2['budget'].values) / df2['budget'].values
# print(percetageProfit[:5])
df2 = df2.drop('gross', 1)
df2 = df2.drop('director_facebook_likes', 1)
print(df2)

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
wordList = list()
wordMatrix = list()
outfile = TemporaryFile()



path = r"F:\MyProjects\MLH_prime\data\reviews_vector\\"

# Creating csv files for pandas to read
"""
for i in os.listdir(path):
    with open(os.path.join(path, i), "r+") as fh:
        with open(os.path.join(path, i.split("_")[0] + ".csv"), 'w') as oh:
            oh.write(fh.read())
            print(1)
"""

with open("data.json") as data_file:

    data = json.load(data_file)
    """
    
    for movie in data:
        commentsh = open(os.path.join(path, movie["id"] + ".csv"))
        for word in commentsh:
            if word.split(",")[0] not in wordList:
                wordList.append(word.split(",")[0])
        print(len(wordList))
    str1 = ','.join(wordList)

    outh = open("wordList.txt", "w")
    outh.write(str1)
    """
    time0 = time.time()
    with open("wordList.txt", "r") as ih:
        for line in ih:
            wordList.append(line.split(","))
        print(len(wordList))

    for movie in data:
        commentsh = open(os.path.join(path, movie["id"] + ".csv"))
        # Preparing for the word matrix
        print(1)
        commentsDict = dict()
        for line in commentsh:

            wordsInLine = line.split(",")
            commentsDict[wordsInLine[0]] = float(wordsInLine[1].strip())
        movieNormalizedVector = []
        total = np.sum(list(commentsDict.values()))
        for word in wordList:
            for singleWord in word:
                movieNormalizedVector.append(commentsDict.get(singleWord, 0) / total)
        wordMatrix.append(movieNormalizedVector)
        print(time.time() - time0)

    
    X=np.array(wordMatrix)
    print(X.shape)
    print(X)

    # Using functions defined in Analytics.py to briefly analyze the data
    result = analyze(X, 8)
    largest = [0, 0]

    for key in result.keys():
        if len(result[key]) > largest[1]:
            largest = [key, len(result[key])]
        print("******************Cluster %s*******************" % str(key+1))
        for value in result[key]:
            for k in data:
                if int(k["rank"]) == value:
                    print("'"+k["film_name"]+"'")

    clu = result[largest[0]]
    print(clu, len(clu))
    cluster = np.array(X[clu])
    print(cluster)
    result = analyze(cluster, 4)
    for key in result.keys():
        print("******************Cluster %s*******************" % str(key+1))
        for value in result[key]:
            for k in data:
                if int(k["rank"]) == value:
                    print("'"+k["film_name"]+"'")



"""
    for key in movieIndicesClustered1.keys():
        print("******************Cluster %s*******************" % str(key+1))
        for value in movieIndicesClustered1[key]:
            for k in data:
                if int(k["rank"]) == value:
                    print(k["film_name"])
"""  