import random
import os

BOARD_WIDTH = int(input("Enter board width\n > "))
BOARD_HEIGHT = int(input("Enter board height\n > "))

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

    while action not in (1, 2):
        action = input("Actions:\nPlace flag: 1\nUncover tile: 2\n > ")

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

def main():
    board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

    print_board(board)

    user_action_prompt()

if __name__  == '__main__':
    main()