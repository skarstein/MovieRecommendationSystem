import pandas as pd
import numpy as np

def parseData():
	matrix = pd.read_csv(
		filepath_or_buffer = "train.txt",
		sep = "\t",
		header = None)
	#print (matrix)
	return matrix

def train(matrix):
	return 0

def test():
	return 0

if __name__ == "__main__":
	matrix = parseData()
	train(matrix)
	test()