import math

def digits(line):
	return list(map(int, filter(lambda x: x.isdigit(), list(line))))

def nums(line, sep=" "):
	return list(map(int, filter(lambda x: x.isnumeric(), line.split(sep))))

def remN (line):
	return [val for val in line if val != ""]

def remSp (line):
	return [val for val in line if val != " "]

def remB (line):
	return remN(remSp(line))
