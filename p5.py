from utils import *
out = 0

with open("p5.txt", "r") as file:
	lines = file.read().split("\n")
	rules = []
	ruleend = False
	for line in lines:
		if line == "":
			ruleend = True
			continue
		if ruleend:
			numline = nums(line, ",")
			l = True
			w = False
			while l:
				l = False
				for i, n in enumerate(numline):
					for r in rules:
						if r[0] == n and r[1] in numline[:i]:
							x = numline.index(r[1])
							numline[i] = r[1]
							numline[x] = r[0]
							l = True
							w = True
							break
					if l:
						break
			print(numline)
			if w:
				out += numline[len(numline)//2 ]

		else:
			rules.append(list(map(int, line.split("|"))))

print(out)