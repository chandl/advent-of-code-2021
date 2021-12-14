#!/usr/bin/env python3
# Advent of Code 2021 - Day 14
# https://adventofcode.com/2021/day/14

from dataclasses import dataclass 
from typing import Dict, List
from collections import Counter

@dataclass
class Formula:
    polymer: List[str] # list of characters
    rules: Dict[str, str] # pair -> character to insert

def parse_input(file: str) -> Formula:
    """
        Parse the input file and return a data structure to use for the problem.
    """
    with open(file) as data:
        lines = data.read().splitlines()
    
    polymer = [c for c in lines[0]]
    rules = dict()
    for rule in lines[2:]:
        pair,insert = rule.split(" -> ")
        #print(f"{pair=} {insert=}")
        rules[pair] = insert

    return Formula(polymer, rules)

def do_insertion(formula: Formula) -> Formula:
    """
        O(N) algorithm that iterates through the polymer string and performs insertions where possible.
    """
    polymer = formula.polymer.copy()
    out = []
    for i in range(0, len(polymer)-1):
        pair = polymer[i] + polymer[i+1]
        insert = formula.rules.get(pair)
        out.append(polymer[i])
        if insert is not None:
            out.append(insert)

    out.append(polymer[-1])
    #print(f"res={''.join(out)}")
    formula.polymer = out
    

def part_a(file: str) -> None:
    """
        Perform polymer insertion using a List. 
        Determine the most and least frequent letter in the resulting chain after 10 steps.
    """
    print(f"\n**** Part A; {file=}")
    formula = parse_input(file)

    for _ in range(10):
        do_insertion(formula)
 
    ordered = Counter(formula.polymer).most_common()
    most_common = ordered[0]
    least_common = ordered[-1]

    result = most_common[1] - least_common[1]

    print(f"{most_common=} {least_common=} {result=}")


def part_b(file: str) -> None:
    """
        Determine the most and least frequent letter in the resulting chain after 40 steps.
        Instead of using a List, it will count the frequency of pairs of letters during each step.
    """
    print(f"\n**** Part B; {file=}")
    formula = parse_input(file)

    # Keep track of the number of times that pairs of characters appear
    # If we know the number of times each pair appears at each step, we can determine how many
    # 'inserted' pairs will be added during each step.
    pair_counter = Counter() 

    # Populate pair_counter with initial polymer
    polymer = formula.polymer
    for i in range(len(polymer) - 1):
        pair = polymer[i] + polymer[i+1]
        pair_counter[pair] += 1
    # print(f"{pair_counter=}")


    for _ in range(40):
        # Create a new Counter object that will replace the current pair_counter
        pair_counter_tmp = Counter() 
        for pair in pair_counter: 
            # e.g. AB is the pair, AB->R is the rule 

            # first character + rule, e.g. this would be 'AR'
            # Every time the current 'pair' is counted, it will create this new pair (i.e. += pair_counter[pair])
            pair_counter_tmp[pair[0] + formula.rules[pair]] += pair_counter[pair]

            # rule + second character, e.g. this would be 'RB'
            # Every time the current 'pair' is counted, it will create this new pair (i.e. += pair_counter[pair])
            pair_counter_tmp[formula.rules[pair] + pair[1]] += pair_counter[pair]
        
        # replace the current pair_counter with the tmp pair_counter
        pair_counter = pair_counter_tmp

    # Count the number of times each character appears
    char_counter = Counter() 
    for pair in pair_counter: 
        char_counter[pair[0]] += pair_counter[pair]
    
    # The last character in the original polymer string is never counted in the above loop,
    #  so add one to this character's count
    char_counter[polymer[-1]] += 1 

    ordered = char_counter.most_common()
    most_common = ordered[0]
    least_common = ordered[-1]
    result = most_common[1] - least_common[1]
    print(f"{most_common=} {least_common=} {result=}")


if __name__ == "__main__":
    part_a("./test_input.txt")
    part_a("./input.txt")
    part_b("./test_input.txt")
    part_b("./input.txt")