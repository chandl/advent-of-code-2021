#!/usr/bin/env python3
# Advent of Code 2021 - Day 13
# https://adventofcode.com/2021/day/13

import numpy as np
import numpy.typing as npt 
from typing import List 
from dataclasses import dataclass


@dataclass 
class Fold:
    """
        Represent a fold instruction (axis and index)
    """
    axis: str # x or y
    index: int

@dataclass
class Board:
    """
        Represent the input (graph and a list of folds)
    """
    graph: npt.NDArray
    folds: List[Fold]


def parse_input(file: str) -> Board:
    """
        Parse the input file and return a data structure to use for the problem.
    """
    with open(file) as data:
        lines = data.read().splitlines()

    # find max x and y values
    max_x = max_y = 0
    points = []
    checking_folds = False
    folds: List[Fold] = []
    for line in lines:
        if line == "":
            checking_folds = True
            continue 

        if not checking_folds:
            y,x = line.split(",")
            max_x = max(int(x) + 1, max_x)
            max_y = max(int(y) + 1, max_y)
            points.append((int(x), int(y)))
        else:
            axis_data,idx = line.split("=")
            axis = axis_data[-1]
            folds.append(Fold(axis, int(idx)))

    graph = np.zeros((max_x, max_y))

    # mark the points on the graph 
    for x,y in points:
        graph[x][y] = 1
    
    #print(f"{max_x=} {max_y=} {graph=} {folds=} {points=}")
    return Board(graph, folds)

def do_fold(graph: npt.NDArray, fold:Fold) -> npt.NDArray:
    """
        Perform the 'fold' on the graph and return the updated graph.
    """
    if fold.axis == "y":
        # horizontal split 
        top = graph[0:fold.index]
        bottom = graph[fold.index+1:]

        # vertically flip the bottom piece and add it to the top
        bottom_flipped = np.flip(bottom, 0)
        combined = top + bottom_flipped

        #print(f"{fold.index=} {top=} {bottom=} {bottom_flipped=} \n{combined=}")
        graph = combined
    else:
        # vertical split 
        left = graph[:, 0:fold.index]
        right = graph[:, fold.index+1:]

        # horizontally flip the right side and add it to the left
        right_flipped = np.flip(right, 1)
        combined = left + right_flipped

        #print(f"{fold.index=} {left=} {right=} {right_flipped=} \n{combined=}")
        graph=combined

    return graph 

def part_a(file: str) -> None:
    print(f"\n**** Part A; {file=}")
    board = parse_input(file)

    # How many dots are visible after completing just the first fold instruction on your transparent paper?
    first_fold = board.folds[0]
    graph_after_fold = do_fold(board.graph, first_fold)

    # count total num of visible 'dots' in graph.
    dot_count = 0
    for num in np.nditer(graph_after_fold):
        if num > 0:
            dot_count += 1

    print(f"{dot_count=}")

def part_b(file: str) -> None:
    print(f"\n**** Part B; {file=}")
    board = parse_input(file)
    graph = board.graph.copy()

    # Do all of the required folds
    for fold in board.folds:
        #print(f"{len(graph)=} {len(graph[0])=}")
        #print(f"{fold=}")
        graph = do_fold(graph, fold)
        
    # print out the graph, it will return ASCII art capital letters
    for row in graph:
        print(" ".join(["#" if x > 0 else " " for x in row]))

if __name__ == "__main__":
    part_a("./test_input.txt")
    part_a("./input.txt") # 622
    part_b("./test_input.txt")
    part_b("./input.txt") # HKUJGAJZ