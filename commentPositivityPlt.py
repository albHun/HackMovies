import matplotlib.pyplot as plt
from toneAnalyzer import invokeToneConversation

def emotionPoint(text):
	tone = invokeToneConversation(text)
	docToneCat = tone['document_tone']['tone_categories']
	emotions = False
	for emoTone in docToneCat:
		if emoTone["category_id"] == 'emotion_tone':
			emotions = emoTone['tones']
	posEmotionScore = 0
	negEmotionScore = 0
	for emotion in emotions:
		if emotion['tone_id'] == 'joy':
			posEmotionScore = emotion['score']
		elif emotion['score'] > negEmotionScore:
			negEmotionScore = emotion['score']
	return posEmotionScore - negEmotionScore


def plotPositivityTimeline(comments):
	# time_interval waits to be decided
	time_interval = 50

	# The comments of a movie sorted in the time order
	comment_timeline = sorted(comments, key=lambda comment: comment["time"])
	
	# Get the time at which comments commencing
	start_time = comment_timeline[0]["time"]

	emotions = list()
	for i in range(0, 10):
		emotionSum = 0
		time_range = [start_time, start_time+time_interval]
		time_start += 1
		# emotionPoint function waits to be done
		for comment in comment_timeline:
			if (comment["time"]>time_range[0] and comment["time"]<time_range[1]):
				emotionSum += emotionPoint(comment) 
		emotions.append(emotionSum)

	plt.plot(np.arrage(comment_timeline[0]["time"], comment_timeline[0]["time"] + 9 * time_interval, time_interval), emotionSum)

text = "I am happy. I feel joyful. I feel excited."
print(emotionPoint(text))