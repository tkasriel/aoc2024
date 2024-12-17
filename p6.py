from utils import *
out = 0

marks = []
with open("p6.txt", "r") as file:
	board = list(map(list, file.read().split("\n")))
	startx = 0
	starty = 0
	drst = [-1, 0]
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == "^":
				startx = i
				starty = j

	for i in range(len(board)):
		for j in range(len(board[0])):
			stx = startx
			sty = starty
			dr = drst
			if i == stx and j == sty:
				continue
			bb = [board[i][:] for i in range(len(board))]
			bf = [[[False for i in range(len(board[0]))] for j in range(len(board))] for o in range(8)]
			bb[i][j] = "?"
			while 0 <= stx + dr[0] < len(board) and 0 <= sty + dr[1] < len(board[0]):
				# print(stx, sty)
				# print("\n".join(["".join(x) for x in bb]))
				# print()
				if bf[dr[0]*2+dr[1]+3][stx][sty]:
					out += 1
					print(i, j)
					break
				bf[dr[0]*2+dr[1]+3][stx][sty] = True
				nxt = bb[stx + dr[0]][sty + dr[1]]
				if nxt == "#" or nxt == "?":
					dr = [dr[1], -dr[0]]
				stx += dr[0]
				sty += dr[1]
		# 	break
		# break

print(out)