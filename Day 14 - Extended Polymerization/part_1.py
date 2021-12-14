#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

# Set up data
with open("input.txt", "r") as f:
    puzzle_input = [l.strip() for l in f.readlines()]

polymer = list(puzzle_input[0])
insertions = {}
for l in puzzle_input[2:]:
    key, val = l.split(" -> ")
    insertions[key] = val

for step in range(1, 11):
    new_polymer = []
    for i, p in enumerate(polymer):
        if i < len(polymer)-1:
            cur_pair = "".join([polymer[i], polymer[i+1]])
            new_polymer.append(polymer[i])
            if cur_pair in insertions.keys():
                new_polymer.append(insertions[cur_pair])
        else:
            new_polymer.append(polymer[i])
    polymer = new_polymer.copy()

    counted = Counter(polymer).most_common()
    print(f"{step=} {counted[0][1]-counted[-1][1]}")

print("")
print(f"The final polymer has a length of {len(polymer)}.")