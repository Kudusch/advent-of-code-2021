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
with open("input.txt", "r") as f:
    puzzle_input = [[int(i) for i in list(l.strip())] for l in f.readlines()]

risk_map = puzzle_input.copy()

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
                print(f"\033[1m\033[96m{vertices[f'{y}-{x}']}\033[0m", end = "")
            else:
                print(vertices[f'{y}-{x}'], end = "")
        print("")
    print("")

    print(f"Shortest path has a length of {len(p)} and a total risk level of {risk_level}\n")