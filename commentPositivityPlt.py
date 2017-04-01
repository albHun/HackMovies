import matplotlib.pyplot as plt

def plotPositivityTimeline(movie, comments):
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
		emotionSum += emotionPoint(comment) for comment in comment_timeline if (comment["time"]>time_range[0] and comment["time"]<time_range[1])
		emotions.append(emotionSum)

	plt.plot(np.arrage(comment_timeline[0]["time"], comment_timeline[0]["time"] + 9 * time_interval, time_interval), emotionSum)