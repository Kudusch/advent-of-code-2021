#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# x position increases by its x velocity.
# y position increases by its y velocity.
# x velocity changes by 1 toward the value 0
# y velocity decreases by 1

# Set up data
target_area = {"x":list(range(137,171+1)), "y":list(range(-98,-73+1))}
#target_area = {"x":list(range(20,30+1)), "y":list(range(-10,-5+1))}

start_pos = [0, 0]


def sim_shot(x, y):
    cur_pos = start_pos.copy()
    start_velo = [x, y]
    cur_velo = start_velo.copy()
    highest_y = []
    flag = True
    while flag:
        cur_pos[0] += cur_velo[0]
        cur_pos[1] += cur_velo[1]
        if cur_velo[0] > 0:
            cur_velo[0] -= 1
        elif cur_velo[0] < 0:
            cur_velo[0] += 1
        cur_velo[1] -= 1
        highest_y.append(cur_pos[1])
        #print(cur_pos)
        if (cur_pos[0] in target_area["x"]) and (cur_pos[1] in target_area["y"]):
            return(start_velo, max(highest_y))
            flag = False
        elif cur_pos[0] > max(target_area["x"]) or cur_pos[1] < min(target_area["y"]):
            flag = False

res = []
for x in range(0, 172):
    for y in range(-98, 98):
        res.append(sim_shot(x, y))


res = [r for r in res if r is not None]
res.sort(key = lambda x: x[1], reverse=True)
print(f"Highest y is {res[0][1]}")
print(f"Total number of distinct initial velocity values is {len(res)}")