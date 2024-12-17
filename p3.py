from utils import *
import re
out = 0

with open("p3.txt", "r") as file:
	l = file.read()
	test = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", l)
	print(test)
	en = True
	for m in test:
		if m == "do()":
			en = True
			continue
		if m == "don't()":
			en = False
			continue
		if en:
			print(".", m)
			n1 = m.split(",")[0][4:]
			n2 = m.split(",")[1][:-1]
			out += int(n1)*int(n2)

print(out)