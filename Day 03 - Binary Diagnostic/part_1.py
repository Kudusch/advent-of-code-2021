#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append(l.strip())

result = [0]*len(puzzle_input[0])

for number in puzzle_input:
	for i, b in enumerate(number):
		if b == "1":
			result[i] += 1
			
result = [(d/len(puzzle_input))>0.5 for d in result]

gamma = int(''.join(['1' if i else '0' for i in result]), 2)
epsilon = int(''.join(['0' if i else '1' for i in result]), 2)

print(gamma, epsilon)
print(gamma*epsilon)
