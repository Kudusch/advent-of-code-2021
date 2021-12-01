#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append(int(l))

#measurements = puzzle_input
measurements = []
for i in range(0, len(puzzle_input)-2):
    measurements.append(sum(puzzle_input[i:i+3]))

counter = 0
for i, v in enumerate(measurements):
    if i > 0:
        if measurements[i] > measurements[i-1]:
            counter += 1
            print(f"{v} (increased)")
        elif measurements[i] == measurements[i-1]:
            print(f"{v} (no change)")
        else:
            print(f"{v} (decreased)")
    else:
        print(f"{v} (N/A - no previous measurement)")

print(f"There were {counter} increases")