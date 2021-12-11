#!/usr/bin/env python3
# Advent of Code 2021 - Day 11
# https://adventofcode.com/2021/day/11

def parse_input(file):
    with open(file) as data:
        lines = data.read().splitlines()
    # 2d array 
    return [[int(c) for c in line] for line in lines]

# Floodfill 
def ff(x, y, grid, flashed):
    """
        Modified floodfill algorithm that checks a single index in the grid. Will flood-fill increment 
        adjacent nodes in the grid whenever the current value equals 9.
    """
    # check out of bounds or if the current position already flashed this step
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or (grid[x][y] == 0 and (x, y) in flashed):
        return

    curr = grid[x][y]
    if curr < 9:
        grid[x][y] += 1
        return 

    grid[x][y] = 0
    flashed.append((x,y))
    # recursively call all adjacent directions if curr_val is 9
    # directions is a list of values to add/subtract from x,y
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1,1), (-1, 1), (1, -1), (-1, -1)]
    for d in directions:
        ff(x + d[0], y + d[1], grid, flashed)
     

def part_a(file):
    """
        Count the number of 'flashes' in 100 steps. 
    """
    print(f"\n**** Part A; {file=}")
    grid = parse_input(file)

    steps = 100
    flashes = 0
    for _ in range(0, steps):
        # for each step, we will check each index in the grid and perform floodfill if 
        # the value at the index increases to 9. 
        flashed = []
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                ff(x, y, grid, flashed)
        flashes += len(flashed)

    print(f"After {steps=}: {flashes=}")

def part_b(file):
    """
        Find the first step where all of the nodes flash at the same time. 
    """
    print(f"\n**** Part B; {file=}")
    grid = parse_input(file)
    
    flash_goal = len(grid) * len(grid[0])
    step = 0
    while(1):
        flashed = []
        # Increment each grid node by one, apply floodfill if node increases to 9
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                ff(x, y, grid, flashed)
        
        step += 1
        # see if every node of the grid flashed
        if len(flashed) == flash_goal: 
            print(f"{step=} flashes={len(flashed)} {flash_goal=}")
            return

if __name__ == "__main__":
    part_a("./test_input.txt")
    part_a("./input.txt")
    part_b("./test_input.txt")
    part_b("./input.txt")