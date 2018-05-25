import math
import pandas as pd
import numpy as np
from recommend import parseData
from recommend import parseTest

def findNeighbors(testUser, k, matrix):
	testUsers = parseTest()
	trainUsers = pd.DataFrame(dict(userID=[], cosSimilarity=[]), dtype=int)
	neighbors = pd.DataFrame(dict(userID=[], cosSimilarity=[]), dtype=int)
	#DataFrame for immediate user a
	a = testUsers[testUsers.userID == testUser]
	a = a[a.rating != 0]
	for j in range(200):
		u = matrix.iloc[j]
		#calculate cosine similarity
		dotProduct = 0
		aSquares = 0
		uSquares = 0
		for k in range(len(a)):
			aRating = a.rating.iloc[k]
			uRating = u.iloc[a.movie.iloc[k]]
			if(aRating != 0 and uRating != 0):
				dotProduct += (aRating * uRating)
				aSquares += aRating**2
				uSquares += uRating**2
		if(dotProduct != 0):
			cosSimilarity = (dotProduct/(math.sqrt(aSquares) * math.sqrt(uSquares)))
		else:
			cosSimilarity = 0
		trainUsers = trainUsers.append({'userID':j, 'cosSimilarity':cosSimilarity}, ignore_index=True)
	#select and return k neighbors
	print(trainUsers)
	for i in range(k):
		max = trainUsers.userID[trainUsers['cosSimilarity'].idxmax()]
		neighbors = neighbors.append(trainUsers[trainUsers.userID==max], ignore_index=True)
		trainUsers = trainUsers[trainUsers.userID != max]
	print(neighbors)
	return neighbors

def predictRatings(neighbors, testUser, matrix):
	testUsers = parseTest()
	a = testUsers[testUsers.userID == testUser]
	a = a[a.rating == 0]
	print(a)
	#for i in range(len(a)):

	#for each movie
	for i in range(0,len(a)):
		w=0
		wr=0
		#for each neighbor
		for j in range(len(neighbors)):
			movie = a.iloc[i,1]
			print("Movie: ", movie)
			user = int(neighbors.iloc[j,0])
			#print("User: ", user)
			similarity = neighbors.loc[1,'cosSimilarity']
			#print("Similarity: ", similarity)
			score = matrix.iloc[user,movie]
			#print("User score: ", score)
			if(score != 0):
				w += similarity
				wr += (score * similarity)
		if(w==0):
			p=999
		else:
			p = wr/w
		print("PREDICTION: ", p)
		with open('result5.txt', 'a') as dst:
			dst.write("{} {} {}\n".format(testUser, movie, int(round(p))))
	#use with block
	#call file src

	return 0

if __name__ == "__main__":
	matrix = parseData()
	for i in range(201,205):
		neighbors = findNeighbors(i, 10, matrix)
		predictRatings(neighbors, i, matrix)
	#output ratings to results file
