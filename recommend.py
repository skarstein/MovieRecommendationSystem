#import numpy as np

def parseData():
	trainingData = open("train.txt")
	print ("Name of file:", trainingData.name)
	print ("Closed or not:", trainingData.closed)
	print ("Opening mode:", trainingData.mode)
	users = 200
	movies = 1000
	matrix = [[0 for x in range(users)] for y in range(movies)]
	for x in range(users):
		for y in range(movies):
			matrix[x][y] = trainingData.read(1)
	trainingData.close()

if __name__ == "__main__":
	parseData()