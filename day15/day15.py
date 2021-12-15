#!/usr/bin/env python3
# Advent of Code 2021 - Day 15
# https://adventofcode.com/2021/day/15
import sys 
from typing import List,Tuple,Dict
from queue import PriorityQueue
import math

def parse_input(file: str) -> List[List[int]]:
    """
        Parse the input file and return a data structure to use for the problem.
    """
    with open(file) as data:
        lines = data.read().splitlines()
    # return 2d grid 
    return [[int(c) for c in line] for line in lines]

def print_graph(graph: List[List[int]]) -> None: 
    """
        Helper method to print graph the same way it's displayed on the site.
    """
    for row in graph: 
       print("".join([str(x) for x in row]))

def get_neighbors(graph: List[List[int]], curr_node: Tuple[int,int]) -> List[Tuple[int,int]]:
    """
        Helper function to return valid neighbors of any point in a graph.
        Does bounds checking.
    """
    curr_row,curr_col = curr_node

    neighbors = []
    
    if curr_row-1 >= 0:
        neighbors.append((curr_row-1, curr_col))

    if curr_row+1 < len(graph):
        neighbors.append((curr_row+1, curr_col))

    if curr_col-1 >= 0:
        neighbors.append((curr_row, curr_col-1))

    if curr_col+1 < len(graph[0]):
        neighbors.append((curr_row, curr_col+1))

    return neighbors

def dijkstra(graph, start_node):
    """
        Dijkstra's shortest path algorithm. Used for Part A but way too slow for part B. 
    """
    # nodes represented by tuple(row,col)
    unvisited_nodes = [] #[[(row,col) for col in row] for row in graph]
    for i in range(len(graph)) :
        for j in range(len(graph[i])):
            unvisited_nodes.append((i,j))

    shortest_path = {}
    previous_nodes = {}

    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None 
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node 
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node 
        
        neighbors = get_neighbors(graph, current_min_node)
        for neighbor in neighbors:
            # how expensive would it be to go to this neighbor 
            tmp = shortest_path[current_min_node] + graph[neighbor[0]][neighbor[1]]
            if tmp < shortest_path[neighbor]:
                shortest_path[neighbor] = tmp 
                previous_nodes[neighbor] = current_min_node
        
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path

def heuristic(position: Tuple[int,int], goal: Tuple[int,int]) :
    """
        Heuristic function for A-star algorithm. 
        Will return the straight line distance between the current point and the end point.
    """
    x1,y1 = position 
    x2,y2 = goal
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def astar(graph: List[List[int]], start: Tuple[int,int], goal: Tuple[int,int]) -> Tuple[Dict[int, int], Dict[int,int]]:
    """
        A-star path finding algorithm. Determine the shortest path between two points with a
        heuristic function.

        shout out to https://www.redblobgames.com/pathfinding/a-star/implementation.html
    """

    # Use priority queue to explore the 'most promising' nodes first. 
    frontier = PriorityQueue()

    # Keep track of where the shortest path comes from at each point
    path = {}

    # Keep track of the current lowest cost to get to each point.
    cost = {}

    frontier.put(start, 0)
    path[start] = None 
    cost[start] = 0

    while not frontier.empty():
        curr = frontier.get()

        if curr == goal:
            break
        
        for next in get_neighbors(graph, curr):
            new_cost = cost[curr] + graph[next[0]][next[1]]
            if next not in cost or new_cost < cost[next]:
                cost[next] = new_cost 
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                path[next] = curr
    return path, cost

def expand_graph(graph: List[List[int]]) -> List[List[int]]: 
    """
        Helper method for Part B that expands the input graph by 5x.
    """
    output = [[0 for _ in range(len(graph[0]) * 5)] for _ in range(len(graph) * 5)]    

    row_offset = len(graph)
    col_offset = len(graph[0])

    # copy the rows down first
    for i, row in enumerate(graph):
        for j,col in enumerate(row):
            cost = int(col)
            output[i][j] = cost 
            for x in range(0, 5):
                output[i + (row_offset * x)][j] = cost
                cost = cost + 1 if cost < 9 else 1

    # then copy the columns over
    for i,row in enumerate(output):
        for j in range(col_offset, len(output[i])):
            prev_value = row[j-col_offset]
            row[j] = prev_value + 1 if prev_value < 9 else 1

    return output 



def part_a(file: str) -> None:
    """
        Pathfinding a limited size graph.
        Used Dijkstra's algorithm to path find. This ended up being pretty slow. 
    """
    print(f"\n**** Part A; {file=}")
    data = parse_input(file)

    # rows, cols
    end_node = ((len(data)-1, len(data[0])-1))

    _, shortest_paths = dijkstra(data, (0, 0))
    shortest_path_to_end_node = shortest_paths[end_node]

    print(f"{end_node=} {shortest_path_to_end_node=}")


def part_b(file: str) -> None:
    """
        Part B involved multiplying the size of the graph by 5, so Dijkstra's algo
        would not be feasible. Implemented A* algo to speed up the search.
    """
    print(f"\n**** Part B; {file=}")
    graph = expand_graph(parse_input(file))

    end_node = ((len(graph)-1, len(graph[0])-1))
    _, cost = astar(graph, (0, 0), end_node)
    cost_to_end_node = cost[end_node]

    print(f"{end_node=} {cost_to_end_node=}")


if __name__ == "__main__":
    part_a("./test_input.txt")
    part_a("./input.txt")
    part_b("./test_input.txt")
    part_b("./input.txt")