#!/usr/bin/env python3

# 2021 - advent of code day 1
# https://adventofcode.com/2021/day/1

# Part a
def part_a():
    with open("input.txt") as fp:
        Lines = fp.readlines()
        count = 0
        last = None
        for line in Lines:
            if not last:
                last = int(line)
                continue 
            if int(line) > last:
                #print(f"{int(line)} > {last}")
                count += 1
            last = int(line)
        return count


# sliding window
def part_b(): 
    with open("input.txt") as fp:
        lines = fp.readlines()

    # calculate sliding window values 
    sliding_window_values = []

    for num in range(0, len(lines) - 2):
        
        sliding_window_values.append(0)
        val = int(lines[num]) + int(lines[num + 1]) + int(lines[num + 2])
        # print(f"val= {int(lines[num])} + {int(lines[num+ 1])} + {int(lines[num+ 2])}")
        # print(f"setting {val=} for {num=}")
        sliding_window_values[num] = val

    count = 0
    last = None 
    for l in sliding_window_values:
        if not last:
            last = int(l)
            continue
        if int(l) > last:
            count += 1
        last = int(l)
    return count

print(f"Part A: {part_a()}")
print(f"Part B: {part_b()}")