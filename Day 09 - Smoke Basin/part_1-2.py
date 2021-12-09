#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Set up data
with open("input.txt", "r") as f:
    puzzle_input = [l.strip() for l in f.readlines()]

class Heightmap:
    def __init__(self, data):
        self.points = [[int(p) for p in list(r)] for r in data]
        self.dims = {"y":len(self.points), "x":len(self.points[0])}
        self.locs = [[[y, x] for x in range(self.dims["x"])] for y in range(self.dims["y"])]
        self.locs = []
        for y in range(self.dims["y"]):
            for x in range(self.dims["x"]):
                self.locs.append((y, x))
        
    def __str__(self):
        return f"Heightmap of {self.dims['y']} x {self.dims['x']} points"

    def get_point(self, y, x):
        return(self.points[y][x])

    def get_adj(self, y, x):
        if y > self.dims["y"] or x > self.dims["x"]:
            return None
        adj = {}
        adj[(y-1, x)] = self.points[y-1][x] if y > 0 else None
        adj[(y+1, x)] = self.points[y+1][x] if y < self.dims["y"]-1 else None
        adj[(y, x-1)] = self.points[y][x-1] if x > 0 else None
        adj[(y, x+1)] = self.points[y][x+1] if x < self.dims["x"]-1 else None
        return(adj)

    def is_lowpoint(self, y, x):
        i = self.get_point(y, x)
        adj = self.get_adj(y, x)
        return(all([i<e for e in adj.values() if e is not None]))

    def get_basin_size(self, y, x):
        if not self.is_lowpoint(y, x):
            return(None)

        basin_points = [(y, x)]
        basin_points.extend([d for d, p in self.get_adj(y, x).items() if (p is not None and p < 9)])
        for y, x in basin_points:
            for p, v in self.get_adj(y, x).items():
                if (p[0], p[1]) not in basin_points and v is not None and v < 9:
                    basin_points.append((p[0], p[1]))

        return(len(basin_points))

hmap = Heightmap(puzzle_input)

lowpoints = []
for y, x in hmap.locs:
    if hmap.is_lowpoint(y, x):
        lowpoints.append([y, x])

part_1 = 0
for y, x in lowpoints:
    part_1 += 1+hmap.get_point(y, x)

print(f"Part 1: {part_1}")

part_2 = []
for y, x in lowpoints:
    part_2.append(hmap.get_basin_size(y, x))
    
part_2 = sorted(part_2)
print(f"Part 2: {part_2[-1]*part_2[-2]*part_2[-3]}")