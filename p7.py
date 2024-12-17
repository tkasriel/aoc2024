from utils import *
out = 0
def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))



with open("p7.txt", "r") as file:
	lines = file.read().split("\n")
	for line in lines:
		a = list(map(int, line.split(" ")[1:]))
		goal = int(line.split(" ")[0][:-1])
		# print(bin(2)[2])
		for i in range(3**(len(a)-1)):
			
			x = "0" * (len(a) - len(ternary(i)) - 1) + ternary(i)
			tot = a[0]
			# print(x)
			j = 0
			for j in range(len(x)):
				num = str(a[j+1])
				if x[j] == "0":
					tot += int(num)
				elif x[j] == "1":
					tot *= int(num)
				elif x[j] == "2":
					tot = tot * 10**len(num) + int(num)
				j+= 1
			if tot == goal:
				print(goal)
				out += goal
				break
			# for j in range(0, 2**(a-1))
		# print('//')

print(out)