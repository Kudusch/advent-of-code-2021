#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

# Set up data
with open("input.txt", "r") as f:
    puzzle_input = [l.strip() for l in f.readlines()]

dots = [[int(i) for i in dot.split(",")] for dot in puzzle_input[:puzzle_input.index("")]]
folds = [fold[11:].split("=") for fold in puzzle_input[puzzle_input.index("")+1:]]

for i, fold in enumerate(folds):
    fold_dir, fold_line = fold
    fold_line = int(fold_line)
    new_dots = []
    for x, y in dots:
        if fold_dir == "y":
            if y > fold_line:
                new_dots.append([x, ((fold_line*2)-y)])
            else:
                new_dots.append([x, y])
        else:
            if x > fold_line:
                new_dots.append([(fold_line*2)-x, y])
            else:
                new_dots.append([x, y])
    
    new_dots.sort()
    dots = list(k for k,_ in itertools.groupby(new_dots))

    if i == 0:
        print(f"After the first fold, there are {len(dots)} dots.\n")

print("The activation code is:")
x_max = max([x for x, y in dots])
y_max = max([y for x, y in dots])
print_points = []
for y in range(y_max+1):
    for x in range(x_max+1):
        if [x, y] in dots:
            print("#", end = "")
        else:
            print(" ", end = "")
    print("")
