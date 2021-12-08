#!/usr/bin/env python3
# Template
# Advent of Code 2021 - Day N
# https://adventofcode.com/2021/day/<N>

def parse_input(file):
    with open(file) as data:
        #line = data.read()
        #lines = data.read().splitlines()
        pass

def part_a(file):
    print(f"\n**** Part A; {file=}")
    data = parse_input(file)

def part_b(file):
    print(f"\n**** Part B; {file=}")
    data = parse_input(file)

if __name__ == "__main__":
    part_a("./test_input.txt")
    #part_a("./input.txt")
    #part_b("./test_input.txt")
    #part_b("./input.txt")