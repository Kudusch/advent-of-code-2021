#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Set up data
with open("input.txt", "r") as f:
    puzzle_input = [list(l.strip()) for l in f.readlines()]

brackets = {
    "[":"]", 
    "(":")", 
    "{":"}", 
    "<":">"
}
error_points = {
    "]":57,
    ")":3, 
    "}":1197, 
    ">":25137
}
autocomplete_points = {
    ")":1, 
    "]":2,
    "}":3, 
    ">":4
}

def find_unmatched(line):
    open_chunks = []
    for c in line:
        if c in brackets.keys():
            open_chunks.append(c)
        elif brackets[open_chunks[-1]] == c:
            open_chunks.pop()
        else:
            return(c)
    return(open_chunks)

part_1 = 0
incomplete_lines = []
for line in puzzle_input:
    check = find_unmatched(line)
    if isinstance(check, str):
        part_1 += error_points[check]
    else:
        incomplete_lines.append(check)

print(f"Part 1: {part_1}")

part_2 = []
for line in incomplete_lines:
    score = 0
    for c in [brackets[c] for c in reversed(line)]:
        score = score*5
        score += autocomplete_points[c]
    part_2.append(score)

print(f"Part 2: {sorted(part_2)[int(len(part_2)/2)]}")