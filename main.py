import random
import os

COVERED_CELL_SYM = '■'
EMPTY_CELL_SYM = '□'
MINE_SYM = '⧆'
FLAG_SYM = '🚩'

CUSTOM_MIN_W = 9
CUSTOM_MIN_H = 9
CUSTOM_MIN_MINES = 10

BOARD_DIFF_SIZES = {
    'beginner' : (9, 9),
    'intermediate' : (16, 16),
    'expert' : (16, 30)
}

BOARD_DIFF_MINES = [10, 40, 99]

def clear():
    os.system('cls' if os.name == 'nt' else clear)

def user_action_prompt():
    action = input("Choose an action:\n  Place flag: 1\n  Uncover tile: 2\n > ")
    
    while int(action) not in (1, 2):
        action = input("Choose an action:\n  Place flag: 1\n  Uncover tile: 2\n > ")

def user_difficulty_prompt():
    difficulty = input("Pick a difficulty:\n  Beginner\n  Intermediate\n  Expert\n  Custom\n > ").lower()

    while difficulty not in ('beginner', 'intermediate', 'expert', 'custom'):
        difficulty = input("Pick a difficulty:\n  Beginner\n  Intermediate\n  Expert\n > ")

    return difficulty

def custom_board_prompt():
    board_w = int(input(f"Enter custom board width [w >= {CUSTOM_MIN_W}]\n > "))

    while board_w < CUSTOM_MIN_W:
        print(f"Custom board width must be greater than {CUSTOM_MIN_W}.")
        board_w = int(input(f"Enter custom board width [w >= {CUSTOM_MIN_W}]\n > "))

    board_h = int(input(f"Enter custom board height [h >= {CUSTOM_MIN_H}]\n > "))

    while board_h < CUSTOM_MIN_H:
        print(f"Custom board height must be greater than {CUSTOM_MIN_H}.")
        board_x = int(input(f"Enter custom board height [h >= {CUSTOM_MIN_H}]\n > "))

    mines = int(input(f"Enter custom mine amount [m >= {CUSTOM_MIN_MINES}]\n > "))

    while mines < CUSTOM_MIN_MINES or mines > board_w * board_h - 9:
        print(f"Custom mine amount must be greater than {CUSTOM_MIN_MINES} and less than width * height - 9.")
        board_x = int(input(f"Enter custom mine amount [m >= {CUSTOM_MIN_MINES}]\n > "))

    return ((board_w, board_h), mines)

def prompt_action_location(size, act_str):
    w, h = size

    x = int(input(f"Enter {act_str} column\n > "))
    while 
    y = int(input(f"Enter {act_str} row\n > "))

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

def main():
    difficulty = user_difficulty_prompt()

    if difficulty != 'custom':
        size: tuple = BOARD_DIFF_SIZES[difficulty]
        mines = BOARD_DIFF_MINES[list(BOARD_DIFF_SIZES.values()).index(size)]
    else:
        custom_properties = custom_board_prompt()

        size: tuple = custom_properties[0]
        mines = custom_properties[1]

    board = [[0 for _ in range(size[0])] for _ in range(size[1])]

    clear()

    print_board(board)

    print(size, mines)

    user_action_prompt()

if __name__  == '__main__':
    main()