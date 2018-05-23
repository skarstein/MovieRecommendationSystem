import pandas as pd
import numpy as np
import math
from recommend import parseData

def findNeighbors(k, matrix):
	users = pd.read_csv(
		filepath_or_buffer = "test5.txt",
		sep = " ",
		names = ["userID", "movie", "rating"])

	#for i in range(201,301):
	for i in range(201,202):
		#create immediate user array
		a = users[users.userID == i]
		a = a[a.rating != 0]
		#print(a)
		#for each row in training data
		for j in range(200):
			#create training user array
			u = matrix.iloc[j]
			#print(u)
			#calculate cosine similarity
			dotProduct = 0
			count = 0
			aSquares = 0
			uSquares = 0
			for k in range(len(a)):
				aRating = a.rating.iloc[k]
				uRating = u.iloc[a.movie.iloc[k]]
				if(aRating != 0 and uRating != 0):
					dotProduct += (aRating * uRating)
					aSquares += aRating**2
					uSquares += uRating**2
			print("dotProduct: ", dotProduct)
			print("aSquares: ", aSquares)
			print("uSquares: ", uSquares)
			cosSimilarity = (dotProduct/(math.sqrt(aSquares)+math.sqrt(uSquares)))
			print(cosSimilarity)

		
def weightedAverage():
	return 0

if __name__ == "__main__":
	matrix = parseData()
	findNeighbors(10, matrix)