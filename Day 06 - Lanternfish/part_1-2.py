#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
start_time = time.time()
from collections import Counter

# read puzzle input
puzzle_input = [int(i) for i in "5,1,2,1,5,3,1,1,1,1,1,2,5,4,1,1,1,1,2,1,2,1,1,1,1,1,2,1,5,1,1,1,3,1,1,1,3,1,1,3,1,1,4,3,1,1,4,1,1,1,1,2,1,1,1,5,1,1,5,1,1,1,4,4,2,5,1,1,5,1,1,2,2,1,2,1,1,5,3,1,2,1,1,3,1,4,3,3,1,1,3,1,5,1,1,3,1,1,4,4,1,1,1,5,1,1,1,4,4,1,3,1,4,1,1,4,5,1,1,1,4,3,1,4,1,1,4,4,3,5,1,2,2,1,2,2,1,1,1,2,1,1,1,4,1,1,3,1,1,2,1,4,1,1,1,1,1,1,1,1,2,2,1,1,5,5,1,1,1,5,1,1,1,1,5,1,3,2,1,1,5,2,3,1,2,2,2,5,1,1,3,1,1,1,5,1,4,1,1,1,3,2,1,3,3,1,3,1,1,1,1,1,1,1,2,3,1,5,1,4,1,3,5,1,1,1,2,2,1,1,1,1,5,4,1,1,3,1,2,4,2,1,1,3,5,1,1,1,3,1,1,1,5,1,1,1,1,1,3,1,1,1,4,1,1,1,1,2,2,1,1,1,1,5,3,1,2,3,4,1,1,5,1,2,4,2,1,1,1,2,1,1,1,1,1,1,1,4,1,5".split(",")]
puzzle_input = [int(i) for i in "3,4,3,1,2".split(",")]

puzzle_input = Counter(puzzle_input)

old_fishes = [0]*9

for i in range(0,9):
    if i in puzzle_input.keys():
        old_fishes[i] = puzzle_input[i]

for day in range(1, 257):
    new_fishes = old_fishes.copy()
    for i in range(0,9):
        new_fishes[i] = old_fishes[(i+1)%9]
        if i == 6:
            new_fishes[i] = new_fishes[i] + old_fishes[0]
    old_fishes = new_fishes.copy()
    if day == 256 or day == 80 or day%10 == 0:
        print(f"{sum(old_fishes):12} at day{day:4}")

print("\n--- %s seconds ---" % (time.time() - start_time))