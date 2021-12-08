#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import compress

# Set up data
puzzle_input = []
with open("input.txt", "r") as f:
    for l in f.readlines():
        l = l.strip()
        unique_patterns, output_value = l.split(" | ")
        puzzle_input.append([unique_patterns.split(" "), output_value.split(" ")])

# 0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6
segment_numbers = {
    6:[0, 6, 9],
    5:[2, 3, 5],
    2:[1],
    4:[4],
    3:[7],
    7:[8]
}

part_1 = 0
for l in puzzle_input:
    part_1 += [len(out_val) in [2, 3, 4, 7] for out_val in l[1]].count(True)

print(f"Part 1: {part_1}")

part_2 = 0
for l in puzzle_input:
    solved_patterns = {}
    unique_patterns = [sorted(list(pat)) for pat in l[0]]
    solved_patterns["1"] = list(compress(unique_patterns, [len(pat) == 2 for pat in unique_patterns]))[0]
    solved_patterns["4"] = list(compress(unique_patterns, [len(pat) == 4 for pat in unique_patterns]))[0]
    solved_patterns["7"] = list(compress(unique_patterns, [len(pat) == 3 for pat in unique_patterns]))[0]
    solved_patterns["8"] = list(compress(unique_patterns, [len(pat) == 7 for pat in unique_patterns]))[0]

    solved_patterns["3"] = list(compress(unique_patterns, [len(pat) == 5 for pat in unique_patterns]))
    solved_patterns["3"] = [pat for pat in solved_patterns["3"] if all(map(lambda v: v in pat, solved_patterns["1"]))][0]

    solved_patterns["6"] = list(compress(unique_patterns, [len(pat) == 6 for pat in unique_patterns]))
    solved_patterns["6"] = [pat for pat in solved_patterns["6"] if any(map(lambda v: v not in pat, solved_patterns["1"]))][0]

    solved_patterns["9"] = list(compress(unique_patterns, [len(pat) == 6 for pat in unique_patterns]))
    solved_patterns["9"] = list(compress(solved_patterns["9"], [list(map(lambda v: v not in pat, solved_patterns["3"])).count(True)  == 0 for pat in solved_patterns["9"]]))[0]

    solved_patterns["0"] = list(compress(unique_patterns, [len(pat) == 6 and pat not in solved_patterns.values() for pat in unique_patterns]))[0]

    solved_patterns["5"] = list(compress(unique_patterns, [len(pat) == 5 and pat not in solved_patterns.values() for pat in unique_patterns]))
    solved_patterns["5"] = list(compress(solved_patterns["5"], [all([p in solved_patterns["6"] for p in pat]) for pat in solved_patterns["5"]]))[0]

    solved_patterns["2"] = list(compress(unique_patterns, [pat not in solved_patterns.values() for pat in unique_patterns]))[0]
    
    output_value = [sorted(list(pat)) for pat in l[1]]
    signal = []
    for pat in output_value:
        signal.extend([k for k, v in solved_patterns.items() if v == pat])

    part_2 += int("".join(signal))


print(f"Part 2: {part_2}")