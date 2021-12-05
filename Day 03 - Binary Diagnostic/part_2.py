#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import compress

# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append(l.strip())

def get_bit_critical(lines, pos, type):
	n_1 = [number[pos] for number in lines].count('1')
	n_0 = [number[pos] for number in lines].count('0')
	if type == "ox":
		if (n_1 >= n_0):
			return '1' 
		else:
			return '0'
	else: 
		if (n_0 <= n_1):
			return '0' 
		else:
			return '1'

filtered_list = puzzle_input.copy()
for i in range(0, len(puzzle_input[0])):
	if len(filtered_list) == 1:
		break
	bit_critical = get_bit_critical(filtered_list, i, "ox")
	f = [s[i] == bit_critical for s in filtered_list]
	filtered_list = (list(compress(filtered_list, f)))
	
	
ox = int(filtered_list[0], 2)

filtered_list = puzzle_input.copy()
for i in range(0, len(puzzle_input[0])):
	if len(filtered_list) == 1:
		break
	bit_critical = get_bit_critical(filtered_list, i, "co")
	f = [s[i] == bit_critical for s in filtered_list]
	filtered_list = (list(compress(filtered_list, f)))
	
	
co = int(filtered_list[0], 2)

print(ox, co)
print(ox*co)
