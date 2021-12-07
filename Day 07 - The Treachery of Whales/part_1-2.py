#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import statistics
import math
import time

# Set up data
with open("input.txt", "r") as f:
    puzzle_input = [int(i) for i in f.read().split(",")]

#puzzle_input = [16,1,2,0,4,2,7,1,2,14] # sample input


# Part 1
start_time = time.time()
med = statistics.median(puzzle_input)
print(f"Part 1: {int(sum([abs(i - med) for i in puzzle_input]))}")
print(f"{time.time() - start_time}")

# Part 2
start_time = time.time()
res = []
for n in range(min(puzzle_input), max(puzzle_input)):
    res.append(sum([j * ((j + 1)/2) for j in [abs(i - n) for i in puzzle_input]]))
print(f"\nPart 2: {int(min(res))}")
print(f"{time.time() - start_time}")

# Part 2 (alt)
start_time = time.time()
m_min = math.floor(statistics.mean(puzzle_input))
m_max = math.ceil(statistics.mean(puzzle_input))
print(f"\nPart 2 (alt): {int(min(sum([j * ((j + 1)/2) for j in [abs(i - m_max) for i in puzzle_input]]),sum([j * ((j + 1)/2) for j in [abs(i - m_min) for i in puzzle_input]])))}")
print(f"{time.time() - start_time}")