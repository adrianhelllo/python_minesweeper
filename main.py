import random
import os

COVERED_CELL_SYM = '■'
EMPTY_CELL_SYM = '□'
MINE_SYM = '⧆'
FLAG_SYM = '🚩'

BOARD_DIFF_SIZES = {
    'beginner' : (9, 9),
    'intermediate' : (16, 16),
    'expert' : (16, 30)
}

BOARD_DIFF_MINES = [10, 40, 99]

def clear():
    os.system('cls' if os.name == 'nt' else clear)

def user_action_prompt():
    action = input("Choose an action:\nPlace flag: 1\nUncover tile: 2\n > ")
    
    while int(action) not in (1, 2):
        action = input("Actions:\nPlace flag: 1\nUncover tile: 2\n > ")

def user_difficulty_prompt():
    difficulty = input("Pick a difficulty:\n  Beginner\n  Intermediate\n  Expert\n  Custom\n > ").lower()

    while difficulty not in ('beginner', 'intermediate', 'expert', 'custom'):
        difficulty = input("Pick a difficulty:\n  Beginner\n  Intermediate\n  Expert\n > ")

    return difficulty

def custom_board_prompt():
    board_w = int(input("Enter custom board width [w >= 9]\n > "))

    while board_w < 9:
        print("Custom board width must be greater than 9.")
        board_w = int(input("Enter custom board width [w >= 9]\n > "))

    board_h = int(input("Enter custom board height [h >= 9]\n > "))

    while board_h < 9:
        print("Custom board height must be greater than 9.")
        board_x = int(input("Enter custom board height [h >= 9]\n > "))

    mines = int(input("Enter custom mine amount [m >= 10]\n > "))

    while mines < 10 or mines > board_w * board_h - 9:
        print("Custom mine amount must be greater than 10 and less than width * height - 9.")
        board_x = int(input("Enter custom mine amount [m >= 10]\n > "))

    return ((board_w, board_h), mines)

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