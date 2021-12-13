#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import chain

# Set up data
with open("input.txt", "r") as f:
    puzzle_input = [l.strip() for l in f.readlines()]

class Grid:
    def __init__(self, data):
        self.points = [[int(p) for p in list(r)] for r in data]
        self.flashed_points = []
        self.dims = {"y":len(self.points), "x":len(self.points[0])}
        #self.locs = [[[y, x] for x in range(self.dims["x"])] for y in range(self.dims["y"])]
        self.locs = []
        for y in range(self.dims["y"]):
            for x in range(self.dims["x"]):
                self.locs.append((y, x))
        
    def __str__(self):
        s = ""
        for r in self.points:
            s += "".join([str(i) for i in r]) + "\n"
        return f"Grid of {self.dims['y']} x {self.dims['x']} points\n{s}"

    def increase_energy(self):
        self.points = [[p+1 for p in r] for r in self.points]

    def get_point(self, y, x):
        if y > self.dims["y"] or x > self.dims["x"]:
            return None
        else:
            return(self.points[y][x])

    def set_point(self, y, x, val):
        self.points[y][x] = val
            
    def get_adj(self, y, x):
        if y > self.dims["y"] or x > self.dims["x"]:
            return None
        adj = {}
        adj[(y-1, x)] = self.points[y-1][x] if y > 0 else None
        adj[(y+1, x)] = self.points[y+1][x] if y < self.dims["y"]-1 else None
        adj[(y, x-1)] = self.points[y][x-1] if x > 0 else None
        adj[(y, x+1)] = self.points[y][x+1] if x < self.dims["x"]-1 else None

        adj[(y-1, x-1)] = self.points[y-1][x-1] if y > 0 and x > 0 else None
        adj[(y+1, x+1)] = self.points[y+1][x+1] if (y < self.dims["y"]-1) and (x < self.dims["x"]-1) else None
        adj[(y+1, x-1)] = self.points[y+1][x-1] if x > 0 and (y < self.dims["y"]-1) else None
        adj[(y-1, x+1)] = self.points[y-1][x+1] if y > 0 and (x < self.dims["x"]-1) else None
        return(adj)

    def get_flash_points(self):
        flash_points = []
        for i, p in enumerate(chain.from_iterable(self.points)):
            if p is not None and p > 9:
                flash_points.append(((i)//self.dims["y"], (i)%self.dims["x"]))
        return(flash_points)

    def flash_point(self, y, x):
        for loc, p in self.get_adj(y, x).items():
            y_loc, x_loc = loc
            if p is not None:
                 self.points[y_loc][x_loc] += 1
        self.flashed_points.append((y, x))
        self.points[y][x] = None

    def is_synchronized(self):
        return(all(chain.from_iterable([[p==0 for p in r] for r in self.points])))

grid = Grid(puzzle_input)
print(grid)

flash_count = 0
first_sync = 0
for step in range(1000):
    grid.increase_energy()
    flag = True if len(grid.get_flash_points()) > 0 else False
    while flag:
        for y, x in grid.get_flash_points():
            grid.flash_point(y, x)
            flash_count += 1
        flag = True if len(grid.get_flash_points()) > 0 else False
    for y, x in grid.flashed_points:
        grid.set_point(y, x, 0)
    grid.flashed_points = []
    if (grid.is_synchronized() and first_sync == 0):
        first_sync = step+1
        break
    if (step+1 == 100):
        flash_100 = flash_count
    print(f"After {step+1}:")
    print(grid)

print(f"After 100 steps there were {flash_100} flashes.")
print(f"The grid synchronizes after {first_sync} steps.")