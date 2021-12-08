#!/usr/bin/env python3

# Advent of Code 2021 - Day 6
# https://adventofcode.com/2021/day/6
import time 
def read_input(file):
    """
        Read input file and return a list of numbers
    """
    with open(file) as data:
        line = data.read()
    return [int(x) for x in line.split(",")]

def part_a(file):
    """
        Naiively count the number of fish that will spawn each day, by maintaining a list, with the size
        being the number of total fish.

        Very slow -- exponential runtime :(
    """
    start_time = time.time()
    days = 80
    input = read_input(file)
    #print(f"initial_{input=}")

    for d in range(0, days):
        max_idx = len(input)
        for idx, day in enumerate(input):
            if idx >= max_idx:
                continue 
            if day == 0:
                input.append(8) # new fish created
                input[idx] = 6 # 
            else:
                input[idx] -= 1
        #print(f"Day {d+1}, {input=} total_fish={len(input)}")

    print(f"After {days} days, total_fish={len(input)}, time={time.time() - start_time}")
    return input


def part_b(file):
    """
        Instead of continually appending to a new list, just track how many new fish will 
        be spawned at each day. 

        Much faster performance than part_a - linear performance instead of exponential
    """
    start_time = time.time()
    days = 256
    fish_to_spawn_each_day = [0] * days 

    input = read_input(file)

    for _, num in enumerate(input):
        #  initialize it!
        fish_to_spawn_each_day[num] += 1
    
    total = len(input)

    for day in range(0, days):
        total += fish_to_spawn_each_day[day]
        try: 
            # original fish will create a new fish after 7 days
            fish_to_spawn_each_day[day + 7] += fish_to_spawn_each_day[day]

            # new fish will create a newer fish after 9 days
            fish_to_spawn_each_day[day + 9] += fish_to_spawn_each_day[day]
        except IndexError:
            # ignore if we go out of bounds
            pass            
            
    print(f"After {days} days, total_fish={total}, time={time.time() - start_time}")
    



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