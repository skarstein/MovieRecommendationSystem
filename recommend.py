import pandas as pd
import numpy as np

def parseData():
	matrix = pd.read_csv(
		filepath_or_buffer = "train.txt",
		sep = "\t",
		header = None)
	print (matrix)

if __name__ == "__main__":
	parseData()