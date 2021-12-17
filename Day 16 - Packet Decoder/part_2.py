#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import prod

def parse_hex(hex_code):
    hex_code = [f"{int(i, 16):04b}" for i in list(hex_code)]
    bit_code = "".join(hex_code)
    return(bit_code)

def gt(l):
    return(int(l[0]>l[1]))

def lt(l):
    return(int(l[0]<l[1]))

def eq(l):
    return(int(l[0]==l[1]))

def parse_packet(packet, offset=0):
    #print(packet)
    packet = packet[offset:]
    parsed = {}
    parsed["version"] = int(packet[0:3], 2)
    parsed["id"] = type_ids[int(packet[3:6], 2)]
    if parsed["id"] == "lit":
        payload = []
        for p in [packet[6:][x:x+5] for x in range(0, len(packet[6:]), 5)]:
            payload.append(p)
            if p[0] == "0":
                break
        parsed["payload"] = [list(p)[1:] for p in payload if list(p)[0] == "1"]
        parsed["payload"].append(list(payload[len(parsed["payload"])][1:]))
        parsed["payload"] = "".join(["".join(p) for p in parsed["payload"]])
        parsed["payload"] = int(parsed["payload"], 2)
        parsed["len_of_package"] = 6 + (len(payload)*5)
    else:
        parsed["length_type"] = int(packet[6])
        if parsed["length_type"] == 0:
            parsed["sub_len"] = int("".join(packet[7:22]), 2)
            parsed["len_of_package"] = 22
            parsed["length_type"] = "len"
        else:
            parsed["sub_len"] = int("".join(packet[7:18]), 2)
            parsed["len_of_package"] = 18
            parsed["length_type"] = "count"
    return(parsed)

def solve_code(bit_code, offset=0):
    p = parse_packet(bit_code, offset)
    if p["id"] == "lit":
        return(p["payload"], offset+p["len_of_package"])
 
    results = []
    initial_offset = offset
    end = -1
 
    if p["length_type"] == "len":
        total_len = p["sub_len"]
        offset += p["len_of_package"]
        while total_len > 0:
            expr_res, end = solve_code(bit_code, offset)
            results.append(expr_res)
            total_len -= end - offset
            offset = end
    else:
        total_count = p["sub_len"]
        offset += p["len_of_package"]
 
        for _ in range(total_count):
            expr_res, end = solve_code(bit_code, offset)
            results.append(expr_res)
            offset = end

    return(p["id"](results), end)

type_ids = {
    0:sum,
    1:prod,
    2:min,
    3:max,
    4:"lit",
    5:gt,
    6:lt,
    7:eq
}


# read puzzle input
with open("input.txt") as f:
   puzzle_input = f.read()    

bit_code = parse_hex(puzzle_input)
print(solve_code(bit_code)[0])