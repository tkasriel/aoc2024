from utils import *
out = 0

with open("p1.txt", "r") as file:
	a = []
	b = []
	lines = file.read().split("\n")
	for line in lines:
		a.append(int(line.split('   ')[0]))
		b.append(int(line.split('   ')[1]))
		a.sort()
		b.sort()
	for x in range(len(a)):
		out += a[x]*b.count(a[x])

print(out)