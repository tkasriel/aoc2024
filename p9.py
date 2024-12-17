from utils import *

class LL:
	def __init__(self, length, stind, isBlank, idSpace=0):
		self.l = length
		self.ib = isBlank
		self.ind = stind
		self.id = idSpace
		self.next = None
		self.prev = None
	def calcSum (self):
		return sum(range(self.ind, self.ind + self.l)) * self.id
	def __str__(self):
		return (str(self.id)*self.l if not self.ib else "."*self.l) + (str(self.next) if self.next else "")

	__repr__ = __str__

out = 0
with open("p9.txt", "r") as file:
	l = file.read().split("\n")[0]
	ll = LL(int(l[0]), 0, False, 0)
	curr = ll
	curr_id = 1
	tot = int(l[0])
	for i, x in enumerate(l[1:]):
		if i % 2 == 0:
			curr.next = LL(int(x), tot, True)
		else:
			curr.next = LL(int(x), tot, False, curr_id)
			curr_id += 1
		curr = curr.next
		tot += int(x)
	curr = ll
	while curr.next:
		curr.next.prev = curr
		curr = curr.next
	# print(ll)

	beg = ll.next
	skipped = []
	end = curr
	while end.prev and beg.next:
		if not beg.ib:
			break
		if beg.l < end.l:
			skipped.append(beg)

			end.l -= beg.l
			beg.id = end.id
			beg.ib = False
			if beg.next.next:
				beg = beg.next.next
				continue
			break
		tmp = beg.prev
		beg.prev = LL(end.l, beg.ind, False, end.id)
		beg.prev.next = beg
		tmp.next = beg.prev
		beg.l -= end.l
		beg.ind += end.l
		end.prev.next = None
		end = end.prev.prev
	curr = ll
	while curr:
		out += curr.calcSum()
		curr = curr.next
	print(out)






# print(out)