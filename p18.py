from utils import *
out = 0
from collections import deque

# used a bunch of chatgpt, didn't want to rewrite BFS and QU for the billionth time

class Vec2D:
	"""From ChatGPT"""
	def __init__(self, x, y):
		"""
		Initialize a 2D vector with x and y coordinates.
		"""
		self.x = x
		self.y = y

	def __add__(self, other):
		"""
		Add two vectors together.
		"""
		if isinstance(other, Vec2D):
			return Vec2D(self.x + other.x, self.y + other.y)
		raise TypeError("Operand must be an instance of Vec2D.")

	def __repr__(self):
		"""
		Represent the vector as a string.
		"""
		return f"Vec2D(x={self.x}, y={self.y})"

	def within_bounds(self, lower_bound, upper_bound):
		"""
		Check if the vector is within the specified bounds.

		:param lower_bound: Vec2D representing the lower bounds (inclusive).
		:param upper_bound: Vec2D representing the upper bounds (inclusive).
		:return: True if within bounds, False otherwise.
		"""
		return (lower_bound.x <= self.x <= upper_bound.x and
				lower_bound.y <= self.y <= upper_bound.y)

def bfs_minimum_path(board, start, goal):
	"""Chatgpt again"""
	"""
	Perform BFS to find the minimum path in a 2D board.
	
	:param board: 2D list representing the grid (0 for free, 1 for blocked).
	:param start: Vec2D object representing the starting position.
	:param goal: Vec2D object representing the goal position.
	:return: Minimum steps to reach the goal, or -1 if unreachable.
	"""
	rows, cols = len(board), len(board[0])
	directions = [Vec2D(0, 1), Vec2D(1, 0), Vec2D(0, -1), Vec2D(-1, 0)]  # Right, Down, Left, Up

	# Check if the starting or goal positions are blocked
	if board[start.x][start.y] == 1 or board[goal.x][goal.y] == 1:
		return -1

	# BFS setup
	queue = deque([(start, 0)])  # (current position, steps)
	visited = set()
	visited.add((start.x, start.y))

	while queue:
		current, steps = queue.popleft()

		# If the goal is reached, return the steps
		if current.x == goal.x and current.y == goal.y:
			return steps

		# Explore neighbors
		for direction in directions:
			neighbor = current + direction

			# Check bounds and if the space is free
			if (0 <= neighbor.x < rows and 0 <= neighbor.y < cols and
				(neighbor.x, neighbor.y) not in visited and board[neighbor.x][neighbor.y] == 0):
				visited.add((neighbor.x, neighbor.y))
				queue.append((neighbor, steps + 1))

	# If the goal is not reachable
	return -1

class QuickUnionWithPathCompression:
	"""Chagpt"""
	def __init__(self):
		# The parent map where keys are Vec2Ds and values are their parent Vec2D
		self.parent = {}

	def find(self, point):
		# Initialize the point if it's not already in the parent map
		if point not in self.parent:
			self.parent[point] = point
		# Perform path compression
		if self.parent[point] != point:
			self.parent[point] = self.find(self.parent[point])
		return self.parent[point]

	def union(self, p, q):
		# Find roots of both points and connect them
		rootP = self.find(p)
		rootQ = self.find(q)
		if rootP != rootQ:
			self.parent[rootP] = rootQ

	def connected(self, p, q):
		# Check if two points have the same root
		return self.find(p) == self.find(q)



# Ok chatgpt stops here

def part1(moves):
	board = [[0 for i in range (71)] for j in range(71)]
	for i in range(1024):
		i,j = map(int, moves[i].split(','))
		board[i][j] = 1

	return bfs_minimum_path(board, Vec2D(0, 0), Vec2D(70, 70))


def part2(moves: list[str]) -> tuple[int, int]:
	SZ = 71
	board = [[0 for i in range (SZ)] for j in range(SZ)]
	for move in moves:
		i,j = map(int, move.split(','))
		board[i][j] += 1
	
	qu = QuickUnionWithPathCompression()
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] > 0:
				continue
			if i < len(board)-1 and board[i+1][j] == 0:
				qu.union((i, j), (i+1, j))
			if j < len(board[0]) - 1 and board[i][j+1] == 0:
				qu.union((i, j), (i, j+1))
	print("\n".join(map(lambda x: "".join(map(str, x)), board)))
	for o, move in enumerate(moves[::-1]):
		i,j = map(int, move.split(','))
		board[i][j] -= 1
		if board[i][j] == 0:
			if i < len(board)-1 and board[i+1][j] == 0:
				qu.union((i, j), (i+1, j))
			if j < len(board[0]) - 1 and board[i][j+1] == 0:
				qu.union((i, j), (i, j+1))
			if i > 0 and board[i-1][j] == 0:
				qu.union((i, j), (i-1, j))
			if j > 0 and board[i][j-1] == 0:
				qu.union((i, j), (i, j-1))
		if qu.connected((0, 0), (SZ-1,SZ-1)):
			return (i, j)

	return (-1, -1)
	


with open("p18.txt", "r") as file:
	lines = file.read().split("\n")
	print(part2(lines))
	
	

