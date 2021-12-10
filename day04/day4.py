#!/usr/bin/env python3
# Advent of Code 2021 - Day 4
# https://adventofcode.com/2021/day/4

class Board():
    """
        Bingo board data struct
    """
    def __init__(self, raw, num):
        self.columns = self.parse_cols(raw)
        self.rows = raw
        self.num = num
        self.winner = False

    def parse_cols(self, input):
        """
            Parse the columns in a board
        """
        cols = []
        tmp = []
        for i in range(0, len(input[0])):
            for k in range(0, len(input)):
                tmp.append(input[k][i])
            cols.append(tmp.copy())
            tmp = []
        return cols
    
    def __repr__(self):
        return "Board {}; rows={}".format(self.num, self.rows)


def parse_input(file):
    # read the input file
    with open(file, "r") as data:
        lines = data.read().splitlines()

    # parse out the draw numbers
    draw_numbers = [int(x) for x in lines[0].split(",")]

    # parse out the boards
    boards = []
    tmp = []
    board_num = 0
    for i,v in enumerate(lines):
        # skip the draw numbers and the line after
        if i < 2: 
            continue 

        # see if a board has ended (empty line)
        if v == "":
            boards.append(Board(tmp.copy(), board_num))
            tmp = []
            board_num += 1
            continue
        
        # parse out numbers in the current row
        parsed = [int(x) for x in v.split()]

        # add to tmp board
        tmp.append(parsed)

    # add the last board 
    boards.append(Board(tmp.copy(), board_num))

    return (draw_numbers, boards)

def intersection(lst1, lst2):
    """
        Return the intersecting values in two lists
    """
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def check_board(board: Board, drawn_nums):
    """
        Brute force verify if a board is a winner
    """
    # check rows 
    for row in board.rows:
        if len(intersection(drawn_nums, row)) == 5:
            print(f"BINGO: {board.num=} {row=}")
            return True

    # check columns
    for col in board.columns:
        if len(intersection(drawn_nums, col)) == 5:
            print(f"BINGO: {board.num=} {col=}")   
            return True 

    return False

def get_unmarked_sum(board: Board, drawn_nums):
    """
        Return the sum of unmarked numbers on the board
    """
    sum = 0
    for row in board.rows:
        for num in row:
            if num not in drawn_nums:
                sum += num
    return sum


def find_winning_board(draw_numbers, boards):
    """
        Find the board that wins first
    """
    nums = []
    for num in draw_numbers:
        nums.append(num)
        for board in boards:
            if check_board(board, nums):
                unmarked_sum = get_unmarked_sum(board, nums)
                final_score = num * unmarked_sum
                print(f"{unmarked_sum=}, last_called={num}, final_score={final_score}")
                return

def find_losing_board(draw_numbers, boards):
    """
        Find the board that wins last
    """
    last_winner_board = None
    last_winner_nums = None

    nums = []
    for num in draw_numbers:
        nums.append(num)
        for board in boards:
            # skip the board if it already had bingo
            if board.winner:
                continue
            if check_board(board, nums):
                # keep track of the last winner
                last_winner_board = board
                last_winner_nums = nums.copy()
                board.winner = True

    # calculate the score for the last winner
    unmarked_sum = get_unmarked_sum(last_winner_board, last_winner_nums)
    final_score = last_winner_nums[-1] * unmarked_sum
    print(f"{unmarked_sum=}, last_called={num}, final_score={final_score}")


if __name__ == "__main__":
    (test_draw, test_boards) = parse_input("./test_input.txt")
    (draw, boards) = parse_input("./input.txt")

    print("========== Part A: Finding Winning Boards ==========")
    print("Test Input:")
    find_winning_board(test_draw, test_boards)

    print("\nReal Input:")
    find_winning_board(draw, boards)

    print("========== Part B: Finding Losing Boards ==========")
    print("Test Input:")
    find_losing_board(test_draw, test_boards)
    
    print("\nReal Input:")
    find_losing_board(draw, boards)