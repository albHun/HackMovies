from toneAnalyzer import invokeToneConversation
import json


path = r"F:\MyProjects\MLH_prime\data\reviews_vector\\"

wordList = list()
with open("data.json") as oh:
	data = json.load(oh)
	time0 = time.time()
    with open("wordList.txt", "r") as ih:
        for line in ih:
            wordList.append(line.split(","))

	for i in range(len(data)):
		movie = data[i]
		name = movie["film_name"]

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
