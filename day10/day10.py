#!/usr/bin/env python3
# (python >= 3.8 required)

# Advent of Code 2021 - Day 10
# https://adventofcode.com/2021/day/10

# Map of opening to closing parentheses
char_map = {
    "(" : ")",
    "{" : "}",
    "<" : ">",
    "[" : "]",
}

def parse_input(file):
    """
        Read an input file and return a list of the lines, where each line is the list of chars.
    """
    with open(file) as data:
        lines = data.read().splitlines()
    return [[c for c in line] for line in lines]

def part_a(file):
    """
        Find invalid parentheses. 
    """
    print(f"\n**** Part A; {file=}")
    value_map = {
        ")" : 3,
        "}" : 1197,
        ">" : 25137,
        "]" : 57
    }

    data = parse_input(file)
    #print(f"{data=}")
    score = 0
    for line in data:
        stack = []
        for char in line:
            if char in char_map.keys():
                stack.append(char)
            else: 
                expected_char = char_map[stack.pop()]
                if char != expected_char:
                    #print(f"illegal char: {char}, {value_map[char]=}")
                    score += value_map[char] 
    print(f"{score=}")

def part_b(file):
    """
        Find the incomplete lines and find the correct ending characters.
    """
    print(f"\n**** Part B; {file=}")
    value_map = {
        ")" : 1,
        "}" : 3,
        ">" : 4,
        "]" : 2
    }
    data = parse_input(file)
    
    # find the incomplete lines
    scores = []
    for line in data:
        stack = []
        invalid = False
        for char in line:
            if char in char_map.keys():
                stack.append(char)
            else: 
                expected_char = char_map[stack.pop()]
                if char != expected_char:
                    # ignore invalid lines 
                    invalid = True
                    break 
        
        # find the closing characters for the incomplete line
        if len(stack) > 0 and not invalid:
            closing_chars = [char_map[c] for c in reversed(stack)]

            # python 3.8 assignment expressions !!
            score = 0
            [score := score * 5 + value_map[n] for n in closing_chars]
            scores.append(score)
            #print(f"{closing_chars=} {score=}")

    # return the middle score in the list of sorted scores
    scores.sort()
    middle_score = scores[int(len(scores) / 2)]
    print(f"{middle_score=}")

if __name__ == "__main__":
    part_a("./test_input.txt")
    part_a("./input.txt")
    part_b("./test_input.txt")
    part_b("./input.txt")