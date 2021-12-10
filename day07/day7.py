#!/usr/bin/env python3
# Advent of Code 2021 - Day 7
# https://adventofcode.com/2021/day/7
import statistics 
import math 
def read_input(file):
    """
        Read input file and return a list of numbers
    """
    with open(file) as data:
        line = data.read()
    return [int(x) for x in line.split(",")]

def part_a(file):
    """
        Find the median of a list and then count the distance of each point to the median.
    """
    print(f"\n**** Part A; {file=}")

    data = read_input(file)
    data.sort()

    # find median
    median = statistics.median(data)

    # see how far away each data point is away from median 
    total_cost = 0

    for pos in data:
        total_cost += abs(pos-median) #if pos > median else (median-pos)

    print(f"{median=} {total_cost=}")


def part_b(file):
    """
        Find the mean of the input list and determine the lowest cost to move each point
        to the mean, using the updated cost function.
    """
    print(f"\n**** Part B; {file=}")
    data = read_input(file)

    # find mean; round up and down, see which result has lower cost
    raw_mean = statistics.mean(data)
    mean_floor = math.floor(raw_mean)
    mean_ceil = math.ceil(raw_mean)

    # see how far away each data point is away from both means
    total_cost_floor = 0
    total_cost_ceil = 0

    for pos in data:
        # difference between position and floor()'d mean 
        diff_f = abs(pos-mean_floor)
        cost = 1
        for _ in range(0, diff_f):
            total_cost_floor += cost
            cost += 1 # (part b) each extra step costs one additional fuel

        # difference between position and ceil()'d mean 
        diff_c = abs(pos-mean_ceil)
        cost = 1
        for _ in range(0, diff_c):
            total_cost_ceil += cost 
            cost += 1 # (part b) each extra step costs one additional fuel

    print(f"{raw_mean=} {total_cost_floor=} {total_cost_ceil=} answer={min(total_cost_floor, total_cost_ceil)}")

if __name__ == "__main__":

    part_a("./test_input.txt")
    part_a("./input.txt")

    part_b("./test_input.txt")
    part_b("./input.txt")