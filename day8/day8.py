#!/usr/bin/env python3
# Advent of Code 2021 - Day 8
# https://adventofcode.com/2021/day/8

def parse_input(file):
    """
        Convert the input file into a list of signals and outputs
    """
    with open(file) as data:
        lines = data.read().splitlines()
    
    signals = []
    output = []
    for line in lines:
        s, o = line.split(" | ")
        signals.append(s.split(" "))
        output.append(o.split(" "))

    return signals,output


# two -> uses 5 inputs
# three -> uses 5 inputs 
# five -> uses 5 inputs 

# zero-> uses 6 inputs
# six -> uses 6 inputs 
# nine -> uses 6 inputs

# one -> uses 2 inputs **
# four -> uses 4 inputs **
# seven -> uses 3 inputs  **
# eight -> uses 7 inputs **

def check_signal(signal):
    """
        Method that determines if a signal is a specific number (1,4,7,8) based on the length of the signal
    """
    if len(signal) == 2:
        return [1]
    elif len(signal) == 3:
        return [7]
    elif len(signal) == 4:
        return [4]
    elif len(signal) == 7:
        return [8]
    elif len(signal) == 6:
        return [0, 6, 9]
    elif len(signal) == 5:
        return [2, 3, 5]

def parse_signals(signals):
    """
        Method that programatically determines which letter each signal corresponds to.
        note: I misunderstood the problem and wrote this, when it's major overkill lol (this info is given in part 2)
    """
    # top, top/left, top/right, middle, bottom/left, bottom/right, bottom
    t = tl = tr = m = bl = br = b = None

     
    # count each time a letter appears 
    letter_count = dict()
    for signal in signals:
        for c in signal:
            curr = letter_count.get(c) or 0
            letter_count[c] = curr + 1 

    # we can definitively find top/left, bottom/left, bottom/right
    # based on the number of times it shows up in all 10 samples
    for a,b in letter_count.items():
        # top/left -> shows up 6x
        # bottom/left -> 4x
        # bottom/right -> 9x
        # top -> 8x
        # top/right 8x 
        # middle -> 7x
        # bottom -> 7x

        if b == 6:
            tl = a
        elif b == 4:
            bl = a 
        elif b == 9:
            br = a


    # create the output array
    # each index will contain the characters that make that number
    nums = [[]] * 10

    # see if the number of characters is unique
    # We will find the definite signal for these: 1, 7, 4, 8
    for signal in signals: 
        num = check_signal(signal)
        if len(num) == 1:
            nums[num[0]] = [c for c in signal] 
    
    # we know bottom/right (br) and we know 1
    # so we can determine top right 
    tr = [x[0] for x in filter(lambda a: a not in br, nums[1])][0]
    #print(f"{nums[1]=} {br=} {tr=}")

    # top and top/right show up the same amount of times (8)
    # since we know top/right, we can find out top 
    t = [x[0] for x in filter(lambda a: a[1] == 8 and a[0] != tr, letter_count.items())] 
    #print(f"{t=}")

    # middle is 4 without tl, tr, br
    m = [x for x in filter(lambda a: a not in [tl, tr, br], nums[4])]
    #print(f"{nums[4]=} {m=}")

    # 9 is 8 without bl
    nums[9] = [x for x in filter(lambda a: a not in bl, nums[8])]
    #print(f"{nums[8]=} {nums[9]=}")
    
    # 5 is 9 without tr
    nums[5] = [x for x in filter(lambda a: a not in tr, nums[9])]
    #print(f"{nums[5]=} {nums[9]=}")

    # 6 is 5 with bl 
    nums[6] = nums[5].copy()
    nums[6].append(bl)
    #print(f"{nums[5]=} {nums[6]=}")
    
    # 3 is 8  without tl and bl
    nums[3] = [x for x in filter(lambda a: a not in [tl, bl], nums[8])]
    #print(f"{nums[3]=}")

    # 2 is 8 without tl and br
    nums[2] = [x for x in filter(lambda a: a not in [tl, br], nums[8])]
    #print(f"{nums[2]=}")

    # 0 is all the same as 8 except one (middle)
    nums[0] = [x for x in filter(lambda a: a not in m, nums[8])]
    #print(f"{nums[0]=}")

    # return a map of signal (sorted string) -> num
    out = dict() 
    for idx,val in enumerate(nums): 
        sorted_num_str = [c for c in val]
        sorted_num_str.sort()
        out["".join(sorted_num_str)] = idx
    return out


def parse_output(output, nums):
    """
        Parse output signals into numbers, given the signal->number map
    """
    out_nums = []
    for segment in output:
        chars = [c for c in segment]
        chars.sort() 
        num = nums["".join(chars)]
        out_nums.append(num)

    return out_nums    

def part_a(file):
    """
        Determine the number of times 1,4,7,or 8 appears in the input
    """
    print(f"\n**** Part A; {file=}")
    signals, output = parse_input(file)

    digits = [1,4,7,8]
    count = 0
    for sig,out in zip(signals, output):        
        nums = parse_signals(sig)
        out_nums = parse_output(out, nums)        
        
        for n in out_nums:
            if n in digits:
                count += 1
    
    print(f"{nums=}; {out_nums=}; {count=}")

     

def part_b(file):
    """
        Sum all of the output signal numbers
    """
    print(f"\n**** Part B; {file=}")
    signals, output = parse_input(file)

    sum = 0
    for sig,out in zip(signals, output):        
        nums = parse_signals(sig)
        out_nums = parse_output(out, nums)
        combined_num = int("".join([str(i) for i in out_nums]))
        sum += combined_num

    print(f"{sum=}")

if __name__ == "__main__":
    part_a("./test_input.txt")
    part_a("./input.txt")
    part_b("./test_input.txt")
    part_b("./input.txt")