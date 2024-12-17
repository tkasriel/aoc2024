from utils import *
out = 0

with open("p2.txt", "r") as file:
	lines = file.read().split("\n")
	for l in lines:
		linet = nums(l)
		for x in range(len(linet)):
			line = linet[:x] + linet[x+1:]
			if sorted(line) != line and sorted(line)[::-1] != line:
				continue
			# print(l)
			prev = line[0]
			n = True
			for a in line[1:]:
				if abs(a-prev) < 1 or abs(a-prev) > 3:
					n = False
				prev = a
			if n:
				out += 1
				break

print(out)