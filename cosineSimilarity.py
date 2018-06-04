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
	#for each training user
	for j in range(200):
		u = matrix.iloc[j]
		#print("training user: ",j)
		#calculate cosine similarity
		dotProduct = 0
		aSquares = 0
		uSquares = 0
		#counter for movies both ranked
		count = 0
		#for each ranked movie
		for m in range(len(a)):
			#print("movie: ",a.movie.iat[m])
			aRating = a.rating.iat[m]
			#print("aRating: ",aRating)
			#added the -1 here because index of movie is 1 less than movieID
			uRating = u.iloc[a.movie.iat[m]-1]
			#print("uRating: ",uRating)
			if(aRating != 0 and uRating != 0):
				dotProduct += (aRating * uRating)
				aSquares += aRating**2
				uSquares += uRating**2
				count = count + 1
		if(dotProduct != 0 and count > 1):
			cosSimilarity = (dotProduct/(math.sqrt(aSquares) * math.sqrt(uSquares)))
			#print("cosSimilarity = ",cosSimilarity)
		else:
			cosSimilarity = 0
			#print("cosSimilarity = 0")
		trainUsers = trainUsers.append({'userID':j, 'cosSimilarity':cosSimilarity}, ignore_index=True)
	#select and return k neighbors
	print(trainUsers)
	#trainUsers = trainUsers[trainUsers.cosSimilarity != 1.000000]
	for i in range(k):
		max = trainUsers.userID[trainUsers['cosSimilarity'].idxmax()]
		neighbors = neighbors.append(trainUsers[trainUsers.userID==max], ignore_index=True)
		trainUsers = trainUsers[trainUsers.userID != max]
	print(neighbors)
	return neighbors

def predictRatings(neighbors, testUser, matrix):
	testUsers = parseTest()
	a = testUsers[testUsers.userID == testUser]
	b = a[a.rating != 0]
	avg = b['rating'].mean()
	a = a[a.rating == 0]
	print(a)
	#for i in range(len(a)):

	#for each movie the immediate user has not rated
	for i in range(0,len(a)):
		w=0
		wr=0
		#for each neighbor
		for j in range(len(neighbors)):
			movie = a.iloc[i,1]
			user = int(neighbors.iloc[j,0])
			#print("User: ", user)
			similarity = neighbors.loc[1,'cosSimilarity']
			#print("Similarity: ", similarity)
			score = matrix.iloc[user,movie - 1]
			#print("User score: ", score)
			if(score != 0):
				w += similarity
				wr += (score * similarity)
		if(w==0):
			print("mean:")
			p=avg
		else:
			p = wr/w
		print("PREDICTION: ", p)
		with open('result20.txt', 'a') as dst:
			dst.write("{} {} {}\n".format(testUser, movie, int(round(p))))

if __name__ == "__main__":
	matrix = parseData()
	for i in range(401,501):
		neighbors = findNeighbors(i, 35, matrix)
		predictRatings(neighbors, i, matrix)
