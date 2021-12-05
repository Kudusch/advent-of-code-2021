#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from itertools import chain, compress

# read puzzle input to list of integers
puzzle_input = []
with open("input.txt", "r") as f:
	for n, l in enumerate(f.readlines()):
	    if n == 0:
	    	called_numbers = l.strip().split(",")
	    elif not l.strip() == "":
	    	puzzle_input.append(l.strip())

puzzle_input = [puzzle_input[i:i+5] for i in range(0, len(puzzle_input), 5)]

class Board:
	def __init__(self, data):
		self.rows = []
		self.cols = [[] for i in range(5)]
		self.last_number = 0

		for i, r in enumerate(data):
			self.rows.append(re.split("\s+", r))
			for j, c in enumerate(re.split("\s+", r)):
				self.cols[j].append(c)

		#self.rows_raw = [l.copy() for l in self.rows]
		#self.cols_raw = [l.copy() for l in self.cols]

	def is_solved(self):
		for i, r in enumerate(self.rows):
			if r.count("x") == 5:
				return True
				#return self.rows_raw[i]
		for i, c in enumerate(self.cols):
			if c.count("x") == 5:
				return True
				#return self.cols_raw[i]
		return False

	def mark_number(self, number):
		if self.is_solved() is not True:
			for i, r in enumerate(self.rows):
				for j, c in enumerate(r):
					if c ==  str(number):
						self.rows[i][j] = "x"
						self.cols[j][i] = "x"
			if self.is_solved() is True:
				self.last_number = int(number)
	
	def get_unmarked_numbers(self):
		unmarked_numbers = list(chain.from_iterable(self.rows))
		unmarked_numbers = list(compress(unmarked_numbers, [n != "x" for n in unmarked_numbers]))
		unmarked_numbers = [int(n) for n in unmarked_numbers]
		return unmarked_numbers

	def sum_unmarked_numbers(self):
		return sum(self.get_unmarked_numbers())

	def __str__(self):
		s = "\n".join(["-".join(r) for r in b.rows])
		return s

boards = []
for raw_board in puzzle_input:
	boards.append(Board(raw_board))

winning_boards = []
for i, n in enumerate(called_numbers):
	for j, b in enumerate(boards):
		b.mark_number(n)
		if b.is_solved() is not False:
			if j not in winning_boards:
				winning_boards.append(j)

print("Solution part 1: {}".format(boards[winning_boards[0]].sum_unmarked_numbers()*boards[winning_boards[0]].last_number))
print("Solution part 2: {}".format(boards[winning_boards[-1]].sum_unmarked_numbers()*boards[winning_boards[-1]].last_number))