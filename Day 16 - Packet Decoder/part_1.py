#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import prod
from itertools import chain

# read puzzle input
with open("input.txt") as f:
    puzzle_input = f.read()    

puzzle_input = [f"{int(i, 16):04b}" for i in list(puzzle_input)]
bit_code = "".join(puzzle_input)

def parse_packet(packet):
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

parsed_packets = []
flag = True
start_pos = 0
version_sum = 0
while flag:
    parsed = parse_packet(bit_code)
    parsed_packets.append(parsed)
    version_sum += parsed["version"]
    start_pos = parsed["len_of_package"]
    bit_code = bit_code[start_pos:]
    if "1" not in bit_code:
        flag = False

print(version_sum)