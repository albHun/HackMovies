from toneAnalyzer import invokeToneConversation
import json
import os


path = r"F:\MyProjects\MLH_prime\data\reviews_vector\\"

movieEmotions = dict()
with open("data.json") as oh:
    data = json.load(oh)

    for i in range(len(data)):
        movie = data[i]
        name = movie["film_name"]

        commentsh = open(os.path.join(path, movie["id"] + ".csv"))
        comments = ""
        count = 0
        for word in commentsh:
            comments += word.split(",")[0] * int(float(word.split(",")[1].strip()) / 100)
            count += 1
            if count > 100:
                break
        tone = invokeToneConversation(comments)['document_tone']['tone_categories']
        for emoTone in tone:
            if emoTone["category_id"] == 'emotion_tone':
                emotions = emoTone['tones']
        movieEmotions[movie["id"]] = emotions
with open("movieEmotions.json", "w") as fout:
    json.dump(json.dumps(movieEmotions), fout)

        
