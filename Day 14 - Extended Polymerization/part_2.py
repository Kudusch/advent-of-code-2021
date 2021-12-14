#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

# Set up data
with open("input.txt", "r") as f:
    puzzle_input = [l.strip() for l in f.readlines()]

insertions = {}
for l in puzzle_input[2:]:
    key, val = l.split(" -> ")
    insertions[key] = val

polymer_pairs = []
polymer = list(puzzle_input[0])
for i, p in enumerate(polymer):
    if i < len(polymer)-1:
        cur_pair = "".join([polymer[i], polymer[i+1]])
        polymer_pairs.append(cur_pair)

polymer_pairs = Counter(polymer_pairs)
new_polymer_pairs = polymer_pairs.copy()

for step in range(40):
    new_polymer_pairs = {}
    for p, v in polymer_pairs.items():
        if v > 0:
            pair_1 = "".join([p[0], insertions[p]])
            pair_2 = "".join([insertions[p], p[1]])
            try:
                new_polymer_pairs[pair_1] += v
            except:
                new_polymer_pairs[pair_1] = v
            
            try:
                new_polymer_pairs[pair_2] += v
            except:
                new_polymer_pairs[pair_2] = v

    polymer_pairs = new_polymer_pairs.copy()

print(f"The final polymer has a length of {sum([v for p, v in polymer_pairs.items()])}.")

letters = Counter([polymer[0], polymer[-1]])
polymer_pairs["".join([polymer[0], polymer[-1]])] -= 1
for p, v in polymer_pairs.items():
    try:
        letters[p[1]] += v
    except:
        letters[p[1]] = v

print(f"After step {step+1} the answer is: {max(letters.values())-min(letters.values())}")