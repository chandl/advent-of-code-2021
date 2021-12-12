#!/usr/bin/env python3
# Advent of Code 2021 - Day 12
# https://adventofcode.com/2021/day/12

from typing import List, Set, Dict

class Node():
    """
        A Node object in a graph. Has a name, if it's a 'big' cave (uppercase), and contains a list of its neighbors.
    """
    def __init__(self, name: str):
        self.name = name
        # true if it's a node that's not 'start' or 'end' and it's upper-case
        self.big = name not in ["start", "end"] and name.isupper()
        self.edges = []
    
    def __repr__(self):
        edges = [val.name for val in self.edges]
        return f"{self.name=} {self.big=} {edges=}"

def parse_input(file: str) -> Dict[str, Node]:
    """
        Parse the input file and return a dictionary of node names -> nodes.
    """
    with open(file) as data:
        lines = data.read().splitlines()

    # map name to node 
    graph: Dict[str, Node] = dict() 

    for line in lines:
        node_a, node_b = line.split("-")

        # Create the nodes in the graph if not already there.
        if node_a not in graph: 
            graph[node_a] = Node(node_a)
        if node_b not in graph:
            graph[node_b] = Node(node_b)

        # Add the bi-directional edges between the nodes
        graph[node_a].edges.append(graph[node_b])
        graph[node_b].edges.append(graph[node_a])

    return graph
        
def dfs(curr: Node, goal: Node, visited: List[Node]) -> int:
    """
        Depth-first Search for Part A, find all unique paths from 'start' to 'end' nodes.
        Visits the 'small' nodes at most once.

        Returns the number of total paths.
    """
    if curr == goal:
        return 1
    
    # don't revisit small nodes
    if not curr.big and curr in visited:
        return 0

    total = 0
    visited.append(curr)
    for edge in curr.edges:
        total += dfs(edge, goal, visited)
    
    visited.remove(curr)
    return total

def part_a(file: str) -> None:
    """
        Find the number of unique paths from start->end nodes in a graph.
        Can only visit the 'small' nodes at most once.
    """
    print(f"\n**** Part A; {file=}")
    # depth first search
    graph = parse_input(file)
    count = dfs(graph["start"], graph["end"], [])
    print(f"{count=}")

def dfs_b(curr: Node, goal: Node, visited: List[Node], small: Node, paths: Set[str]) -> None:
    """
        Depth-first Search for Part B, find all unique paths from 'start' to 'end' nodes.
        Will visit the 'small' node at most 2 times.

        Does not return anything, modifies the 'paths' set. 
    """
    # Add the current path to the 'paths' set if we're at the goal. 
    if curr == goal:
        path_str = ",".join([x.name for x in visited] + [curr.name])
        paths.add(path_str)
        return
    
    if curr == small:
        # allow the chosen 'small' value to be visited at most twice
        if visited.count(curr) > 1:
            return 
    else: 
        # don't revisit other small nodes
        if not curr.big and curr in visited:
            return

    visited.append(curr)
    for edge in curr.edges:
        dfs_b(edge, goal, visited, small, paths)
    visited.pop()

def part_b(file: str) -> None:
    """
        Find the number of unique paths from start->end nodes in a graph.
        For each path, can visit ONE of the 'small' nodes at most twice.
    """
    print(f"\n**** Part B; {file=}")
    graph = parse_input(file)

    # get a list of all small caves
    small_ones = list(filter(lambda x: not x.big and x.name not in ["start", "end"], graph.values()))
    
    # keep track of all unique paths
    paths = set()

    # repeat DFS for each small cave
    for small_one in small_ones:
       dfs_b(graph["start"], graph["end"], [], small_one, paths)
    
    print(f"count={len(paths)}")

if __name__ == "__main__":
    part_a("./test_input.txt")
    part_a("./test_2.txt")
    part_a("./test_3.txt")
    part_a("./input.txt")

    part_b("./test_input.txt")
    part_b("./test_2.txt")
    part_b("./test_3.txt")
    part_b("./input.txt")