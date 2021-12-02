#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append(l.strip().split(" "))

position = {"horizontal":0, "depth":0, "aim":0}

for direction, value in puzzle_input:
    if direction == "forward":
        position["horizontal"] += int(value)
        position["depth"] += (position["aim"]*int(value))
    elif direction == "up":
        position["aim"] -= int(value)
    elif direction == "down":
        position["aim"] += int(value)

print(f"{position=}")
print(f"{position['horizontal']*position['depth']}")