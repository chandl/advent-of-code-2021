#!/usr/bin/env python3 

# 2021 - advent of code day 2
# https://adventofcode.com/2021/day/2

def part_a():
    horiz_pos = depth = 0

    with open("input.txt") as data:
        lines = data.readlines()

    for line in lines: 
        (dir, num) = line.replace("\n", "").split(" ")
        
        if dir == "forward":
            horiz_pos += num 
        elif dir == "down": 
            depth += num
        elif dir == "up":
            depth -= num
        else:
            print(f"unknown dir: {dir}")
        #print(f"{dir=} {num=}")
    res = horiz_pos * depth
    #print(f"{horiz_pos=} {depth=}, {res=}")
    return res
     
def part_b():
    horiz_pos = depth = aim = 0

    with open("input.txt") as data:
        lines = data.readlines()

    for line in lines: 
        (dir, num) = line.replace("\n", "").split(" ")
        
        if dir == "forward":
            horiz_pos += num 
            depth += aim * num
        elif dir == "down": 
            aim += num
        elif dir == "up":
            aim -= num
        else:
            print(f"unknown dir: {dir}")
    res = horiz_pos * depth
    # print(f"{horiz_pos=} {depth=}, {aim=}, {res=}")
    return res

print(f"Part A: {part_a()}")
print(f"Part B: {part_b()}")