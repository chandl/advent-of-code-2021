#!/usr/bin/env python3

# 2021 - advent of code day 3
# https://adventofcode.com/2021/day/3


def calc_occurences(test_input):
    bin_length = len(test_input[0])
    ones = [0] * bin_length
    zeros = [0] * bin_length

     # Count the number of zeros and ones in each index
    for input in test_input:
        for i, v in enumerate(input):
            if v == '0':
                zeros[i] += 1
            else:
                ones[i] += 1
    return (zeros, ones)


def part_a(test_input):
    zeros, ones = calc_occurences(test_input)

    gamma_bin = ""
    epsilon_bin = ""
    for v in zip(ones,zeros):
        if v[0] > v[1]:
            # if total number of ones in this place greater than zero
            gamma_bin += "1"
            epsilon_bin += "0"
        else:
            gamma_bin += "0"
            epsilon_bin += "1"
    # convert binary string to int
    gamma = int(gamma_bin, 2)
    epsilon = int(epsilon_bin, 2)
    # calculate result
    result = gamma * epsilon

    #print(f"{gamma_bin=} {gamma=} {epsilon_bin=} {epsilon=} {result=}")
    return result


def part_b(test_input):
    input_length = len(test_input[0])
    # find oxygen generator rating (most common bits)
    o = None
    curr_o = test_input.copy()

    # find co2 scrubber rating (least common bits)
    co2 = None
    curr_co2 = test_input.copy()

    for bit in range(0, input_length):       
        ones_o = []
        zeros_o = []
        ones_co2 = []
        zeros_co2 = []

        if o is None:
            # calculate bit occurences for oxygen
            for input in curr_o:
                if input[bit] == "0":
                    zeros_o.append(input)
                else:
                    ones_o.append(input)

            # only keep the inputs with the most popular bits (o2 generator rating)
            curr_o = ones_o if len(ones_o) >= len(zeros_o) else zeros_o

        if co2 is None: 
            # calculate bit occurences for co2
            for input in curr_co2:
                if input[bit] == "0":
                    zeros_co2.append(input)
                else:
                    ones_co2.append(input)
            curr_co2 = zeros_co2 if len(zeros_co2) <= len(ones_co2) else ones_co2


        if len(curr_o) == 1:
            o = int(curr_o[0], 2)
            #print(f"Found oxygen generator rating: binary={curr_o[0]}, ({o=})")

        if len(curr_co2) == 1:
            co2 = int(curr_co2[0], 2)
            #print(f"Found co2 scrubber rating: binary={curr_co2[0]}, ({co2=})")


    result = o * co2
    print(f"Oxygen Generator Rating: {o=}, CO2 Scrubber Rating: {co2=}, {result=}")
    
    return result


test_case = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

if __name__ == "__main__":
    with open("input.txt") as data:
        lines = data.read().splitlines()

    print(f"Test A result: {part_a(test_case)}")
    print(f"Part A: {part_a(lines)}")

    print(f"Test B result: {part_b(test_case)}")
    print(f"Part B: {part_b(lines)}")


# Oxygen Generator Rating: o=23, CO2 Scrubber Rating: co2=10, result=230
# Test B result: 230
# Oxygen Generator Rating: o=1459, CO2 Scrubber Rating: co2=3178, result=4636702
# Part B: 4636702