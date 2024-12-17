from utils import *
out = 0

with open("p8.txt", "r") as file:
	lines = file.read().split("\n")
	ants = []
	seen = [[False for l in lines[0]] for j in lines]
	for i, line in enumerate(lines):
		for j, c in enumerate(line):
			if c != ".":
				ants.append([i, j, c])
	# print(ants)
	for i, x in enumerate(ants):
		for y in ants[i+1:]:
			if y[2] != x[2]:
				continue
			# print(x, y)
			ci = x[0]-y[0]
			cj = x[1]-y[1]
			chngi = 0
			chngj = 0
			while 0 <= x[0]+chngi < len(lines) and 0 <= x[1] + chngj < len(lines[0]):
				out += (1 if not seen[x[0]+chngi][x[1]+chngj] else 0)
				seen[x[0]+chngi][x[1]+chngj] = True
				chngi += ci
				chngj += cj
			chngi = 0
			chngj = 0
			while 0 <= y[0]-chngi < len(lines) and 0 <= y[1]-chngj < len(lines[0]):
				out += (1 if not seen[y[0]-chngi][y[1] - chngj] else 0)
				seen[y[0]-chngi][y[1] - chngj] = True
				chngi += ci
				chngj += cj
	board = []
	for i, line in enumerate(lines):
		board.append([])
		for j, c in enumerate(line):
			board[i].append("#" if seen[i][j] else c)
		board[-1] = "".join(board[-1])
	print("\n".join(board))
# print(seen)
print(out)