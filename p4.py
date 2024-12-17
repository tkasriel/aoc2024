from utils import *
import numpy as np
import re
out = 0

with open("p4.txt", "r") as file:
	lines = list(map(list, file.read().split("\n")))

	for i in range(len(lines)-2):
		for j in range(len(lines[0])-2):
			if lines[i+1][j+1] == "A" and lines[i][j] in ["S", "M"] and lines[i+2][j+2] in ["S", "M"] and lines[i][j] != lines[i+2][j+2] and (\
				(lines[i][j] == lines[i+2][j] and lines[i][j+2] == lines[i+2][j+2]) or \
				(lines[i][j] == lines[i][j+2] and lines[i+2][j] == lines[i+2][j+2]) \
				):
				out += 1


	# part 1
# 	out += len(re.findall(r"XMAS", ".".join(lines)))
# 	out += len(re.findall(r"XMAS", ".".join(lines)[::-1]))
# 	tp = list(map(lambda x: "".join(x), (np.array(list(map(list, lines))).transpose()).tolist()))
# 	# print(tp)
# 	out += len(re.findall(r"XMAS", ".".join(tp)))
# 	# print(out)
# 	out += len(re.findall(r"XMAS", ".".join(tp)[::-1]))
# 	# print(out)
# 	nn = np.array(list(map(list, lines)))
# 	for i in range(-len(nn)+1, len(nn)):
# 		d1 = "".join(nn.diagonal(i))
# 		out += len(re.findall(r"XMAS", d1))
# 		out += len(re.findall(r"XMAS", d1[::-1]))
		
# 		d2 = "".join(np.fliplr(nn).diagonal(i))
# 		out += len(re.findall(r"XMAS", d2))
# 		out += len(re.findall(r"XMAS", d2[::-1]))
	

# 	# c2 = np.sum(np.strings.count(np.flip(np.split(lines)), "XMAS"))

# 	# print(c1)

print(out)