#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import igraph

# Set up data
with open("input.txt", "r") as f:
    edge_list = [l.strip().split("-") for l in f.readlines()]

vertex_list = []
[vertex_list.extend(edge) for edge in edge_list]
vertex_list = list(set(vertex_list))

g = igraph.Graph()

g.add_vertices(vertex_list, attributes = {"is_big":[v.isupper() for v in vertex_list]})
for source, target in edge_list:
    g.add_edge(source, target)

def walk_caves_simple(walked_path):
    if walked_path[-1] == "end":
        solved_walks.append(walked_path)
        return walked_path
    else:
        for next_step in g.vs[g.neighbors(walked_path[-1])]:
            if next_step["is_big"] or next_step["name"] not in walked_path:
                walk_caves_simple(walked_path + [next_step["name"]])

def walk_caves(walked_path, chosen):
    if walked_path[-1] == "end":
        if walked_path not in solved_walks:
            solved_walks.append(walked_path)
        return walked_path
    else:
        for next_step in g.vs[g.neighbors(walked_path[-1])]:
            if next_step["is_big"]:
                walk_caves(walked_path + [next_step["name"]], chosen)
            elif next_step["name"] == chosen and walked_path.count(next_step["name"]) < 2:
                walk_caves(walked_path + [next_step["name"]], chosen)
            elif walked_path.count(next_step["name"]) < 1:
                walk_caves(walked_path + [next_step["name"]], chosen)

solved_walks = []
walked_path = ["start"]
walk_caves_simple(walked_path)
print(f"There are {len(solved_walks)} paths under simple rules.")

solved_walks = []
small_caves = [v["name"] for v in g.vs if not v["is_big"] and v["name"] not in ["start", "end"]]
for i, chosen_cave in enumerate(small_caves):
    print(chosen_cave, i/len(small_caves), end="\r")
    walk_caves(walked_path, chosen_cave)

print(f"There are {len(solved_walks)} paths under complex rules.")