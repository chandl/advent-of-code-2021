#!/usr/bin/env python3
# Advent of Code 2021 - Day 5
# https://adventofcode.com/2021/day/5

import numpy as np

def parse_line(line):
    """
        Parse line like '0,9 -> 5,9' into start and end coordinates
    """
    start, end = line.split(" -> ")
    start_x, start_y = [int(x) for x in start.split(",")]
    end_x, end_y = [int(x) for x in end.split(",")]
    return (start_x, start_y, end_x, end_y)

def parse_input(file):
    """
        Parses the input file into a list of start/end coordinates and 
        a 2d array object within the bounds of the lines
    """
    with open(file) as data:
        l = data.read().splitlines()
    lines = [parse_line(x) for x in l]
    
    # get max x(colum) and y(row) values
    columns = rows = 0
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 > columns:
            columns = x1
        if x2 > columns:
            columns = x2 
        if y1 > rows:
            rows = y1 
        if y2 > rows:
            rows = y2
    map = np.zeros(shape=(rows+1,columns+1)).astype('int')
    #print(f"{columns=} {rows=} {map=}")
    return lines, map
    
def parse_horiz_vert(lines, map):
    """
        Iterate through all of the lines and mark all of the points that
        the horizontal and vertical lines overlap on the map.
    """
    for line in lines:
        x1, y1, x2, y2 = line
        #print(f"{x1=} {x2=} {y1=} {y2=}")

        if x1 == x2:
            # vertical
            for num in range(min(y1, y2), max(y1, y2)+1):
                map[num][x1] += 1
            #print(f"Map after vert:{map}")
        elif y1 == y2:
            # horizontal
            for num in range(min(x1, x2), max(x1, x2)+1):
                map[y1][num] += 1
            #print(f"Map after horiz:{map}")

    return map

def parse_diagonal(lines, map):
    """
        Iterate through all of the lines and mark all of the points that
        the diagonal lines overlap on the map.
    """
    # Handle only the diagonals
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 != x2 and y1 != y2:
            # figure out which way to iterate both x and y values
            # They will linearly increase or decrease by 1 each step since
            # The diagonals are only ever 45 degrees.
            increase_x = x1 < x2 
            increase_y = y1 < y2

            x,y = x1,y1
            while x != x2:
                # mark the point on the map
                map[y][x] += 1
                x += 1 if increase_x else -1
                y += 1 if increase_y else -1
            # Mark the final point
            map[y2][x2] += 1
    return map

def count_overlap(map):
    """
        Count the number of points in the 2d map where more than one
        line intersects.
    """
    overlap = 0
    for col, row in np.ndindex(map.shape):
        #print(map[col, row])
        if map[col, row] > 1:
            overlap += 1
    return overlap

def part_a(file):
    lines, map = parse_input(file)
    parse_horiz_vert(lines, map)
    overlap = count_overlap(map)
    print(f"{map=} {overlap=}")

def part_b(file):
    # Same thing as part A, but with diagonals
    lines, map = parse_input(file)
    parse_horiz_vert(lines, map)
    parse_diagonal(lines, map)
    overlap = count_overlap(map)
    print(f"{map=} {overlap=}")

if __name__ == "__main__":
    print("========== Part A ==========")
    print("Test Input:")
    part_a("./test_input.txt")

    print("\nReal Input:")
    part_a("./input.txt")
    
    print("========== Part B ==========")
    print("Test Input:")
    part_b("./test_input.txt")

    print("\nReal Input:")
    part_b("./input.txt")
