#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import igraph

def get_adj(v):
    y, x = [int(i) for i in v.split("-")]
    if y > dims["y"] or x > dims["x"]:
        return None
    adj = []
    if y < dims["y"]-1:
        adj.append(f"{y+1}-{x}")
    if x < dims["x"]-1:
        adj.append(f"{y}-{x+1}")
    if x > 0:
        adj.append(f"{y}-{x-1}")
    if y > 0:
        adj.append(f"{y-1}-{x}")
    return(adj)

# Set up data
with open("input_sample.txt", "r") as f:
    puzzle_input = [[int(i) for i in list(l.strip())] for l in f.readlines()]

risk_map = []
incrementer = sorted([i%5 for i in range(len(puzzle_input[0])*5)])
for r in puzzle_input:
    risk_map.append([i-9 if i>9 else i for i in [x + y for x, y in zip([int(i) for i in r]*5, incrementer)]])

first_row = risk_map.copy()
for j in range(1, 5):
    for r in first_row:
        risk_map.append([(i+j)-9 if (i+j)>9 else i+j for i in r])

dims = {"x":len(risk_map[0]), "y":len(risk_map)}

vertices = {}
for y, r in enumerate(risk_map):
    for x, i in enumerate(r):
        vertices[f"{y}-{x}"] = i

g = igraph.Graph(directed=True)

g.add_vertices(list(vertices.keys()))

edges = []
edge_weights = []
for v, risk_level in vertices.items():
    all_adj = get_adj(v)
    for adj in all_adj:
        edges.append((v, adj))
        edge_weights.append(vertices[adj])

g.add_edges(edges, attributes = {"weight":edge_weights})

paths = g.get_shortest_paths("0-0", to=f"{dims['y']-1}-{dims['x']-1}", weights = "weight")

for p in paths:
    risk_level = sum([vertices[g.vs[i]["name"]] for i in p[1:]])
    path_nodes = [g.vs[i]["name"] for i in p]

    for y in range(dims["y"]):
        for x in range(dims["x"]):
            if f"{y}-{x}" in path_nodes:
                print(vertices[f"{y}-{x}"], end = "")
            else:
                print(".", end = "")
        print("")
    print("")

    print(f"Shortest path has a length of {len(p)} and a total risk level of {risk_level}\n")
