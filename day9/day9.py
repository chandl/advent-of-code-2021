#!/usr/bin/env python3
# Advent of Code 2021 - Day 9
# https://adventofcode.com/2021/day/9
import sys
import heapq
import math

def parse_input(file):
    with open(file) as data:
        lines = data.read().splitlines()
    
    out = []
    for line in lines:
        out.append([int(x) for x in line])

    # return 2d numpy array (pretty printing)
    return out

def find_low_points(data):
    """
        Helper method that finds the 'low' points in a 2d array.
        Low points are points that have a lower value than all of the surrounding points
        (above, below, left, right)

        This method will return a list of (x,y) points and a list of the values of those points for convenience.
    """
    rows = len(data)
    cols = len(data[0])

    low_points = []
    low_point_vals = []

    for i in range(0, rows):
        for j in range (0, cols):
            curr = data[i][j]

            # Find the surrounding values. If out of bounds, set to sys.maxsize
            left = data[i][j-1] if j-1 >= 0 else sys.maxsize
            right = data[i][j+1] if j+1 < cols else sys.maxsize
            up = data[i-1][j] if i-1 >= 0 else sys.maxsize
            down = data[i+1][j] if i+1 < rows else sys.maxsize

            # Check if the current point is lower than all the surrounding points
            if curr < left and curr < right and curr < up and curr < down:
                low_points.append((i,j))
                low_point_vals.append(curr)

    return low_points, low_point_vals

def part_a(file):
    """
        Find the 'low' points in a 2d array and calculate the total 'risk score'.
    """
    print(f"\n**** Part A; {file=}")
    data = parse_input(file)

    _, low_points = find_low_points(data)
        
    risk_score = len(low_points) + sum(low_points)
    print(f"{len(low_points)=} {risk_score=}")

def ff(i, j, data, visited, prev, basin):
    """
        Recursive flood fill algorithm.
        Creates a 'basin' array that has all of the points in the 'data' array 
        which are in a 'basin' (part b)
    """

    # bounds check, check if visited already, check if value is larger than prev, check if value is 9
    if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]) or visited[i][j] or data[i][j] == 9 or data[i][j] <= prev:
        return

    basin.append((i,j))
    visited[i][j] = True

    ff(i+1, j, data, visited, prev, basin)
    ff(i-1, j, data, visited, prev, basin)
    ff(i, j+1, data, visited, prev, basin)
    ff(i, j-1, data, visited, prev, basin)

def part_b(file):
    """
        Find the 'basins' in a 2d array. 
    """
    print(f"\n**** Part B; {file=}")
    data = parse_input(file)

    # Start with a list of the low points
    low_points, _ = find_low_points(data)

    # Find the size of the basins around all of the low points
    basin_lengths = []
    for point in low_points:
        basin = [] # will be modified by floodfill function
        ff(point[0], point[1], data, [[False for _ in range(0,len(data[0]))] for _ in range(0,len(data))], -1, basin)
        basin_lengths.append(len(basin))

    # Determine the top three basin sizes and the product of those three.
    top_three = heapq.nlargest(3, basin_lengths)
    top_three_prod = math.prod(top_three)
    
    print(f"{top_three=} {top_three_prod=}")

if __name__ == "__main__":
    part_a("./test_input.txt")
    part_a("./input.txt")
    part_b("./test_input.txt")
    part_b("./input.txt")