import pandas as pd
import numpy as np
from recommend import parseData

def findNeighbors(k, matrix):
	users = pd.read_csv(
		filepath_or_buffer = "test5.txt",
		sep = " ",
		names = ["userID", "movie", "rating"])

	users.groupby("userID")

	print (users)
	

	#users = users.values
"""
	for i in range (8496):
		if (users[i][2] != 0 && matrix:
			print("what")
"""	
def weightedAverage():
	return 0

if __name__ == "__main__":
	matrix = parseData()
	findNeighbors(10, matrix)