#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import chain
from collections import Counter

# read puzzle input to list of integers
puzzle_input = []
with open("input.txt", "r") as f:
	for l in f.readlines():
		puzzle_input.append(l.strip())

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return f"({self.x},{self.y})"

	def __repr__(self):
		return f"({self.x},{self.y})"

	def __hash__(self):
		return hash(self.x) ^ hash(self.y)

	def __eq__(self, other):
	 	return (self.x == other.x) and (self.y == other.y)

class Line:
	def __init__(self, data):
		self.start, self.stop = [[int(i) for i in p.split(",")] for p in data.split(" -> ")]
		self.start = Point(self.start[0], self.start[1])
		self.stop = Point(self.stop[0], self.stop[1])
		
		if self.start == self.stop:
			self.points = [self.start, self.stop]
		elif self.start.x == self.stop.x:
			self.is_diagonal = False
			if (self.start.y < self.stop.y):
				self.points = [Point(self.start.x, i) for i in range(self.start.y, self.stop.y+1)]
			else:
				self.points = [Point(self.start.x, i) for i in range(self.start.y, self.stop.y-1, -1)]
		elif self.start.y == self.stop.y:
			self.is_diagonal = False
			if (self.start.x < self.stop.x):
				self.points = [Point(i, self.start.y) for i in range(self.start.x, self.stop.x+1)]
			else:
				self.points = [Point(i, self.start.y) for i in range(self.start.x, self.stop.x-1, -1)]
		else:
			self.is_diagonal = True
			step = -1 if self.start.x > self.stop.x else 1
			range_1 = range(self.start.x, self.stop.x+step, step)
			step = -1 if self.start.y > self.stop.y else 1
			range_2 = range(self.start.y, self.stop.y+step, step)
			self.points = [Point(x,y) for x, y in zip(range_1, range_2)]


		self.len = len(self.points)
	def __str__(self):
		return f"{self.start} -> {self.stop}"

lines = []
for l in puzzle_input:
	lines.append(Line(l))

active_points = []
for n, l in enumerate(lines):
	#if not l.is_diagonal:
	active_points.extend(l.points)

over_2 = 0
count = Counter(active_points)
for p, c in count.items():
	if c > 1:
		over_2 += 1

print(over_2)