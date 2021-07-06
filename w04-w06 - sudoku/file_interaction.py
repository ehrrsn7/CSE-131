"""
Program: Lab 05 - Sudoku
FILE INTERACTION MODULES
"""

# import
from ast import dump
import json


def load_board(filename="boards/board.json"):
    debug("load_board() called.")
    return filename, get_board(filename)


def load_user_board(filename="boards/user_board.json"):
    debug("load_user_board() called.")
    return filename, get_board(filename)


def load_new_board():
    return load_board(input("Enter a filename for a sudoku board: "))


def save_board(board: list, user_board:list):
    debug("save_board() called.")
    user_board_filename:str = "boards/user_board.json"
    board_filename:str      = "boards/board.json"

    # save user board
    with open(user_board_filename, 'w') as file:
        print(f"Saving user_board at '{user_board_filename}'...")
        dump_contents = json.dumps({"name":"user board", "board":user_board}, indent=4)
        file.write(dump_contents)

    # save file board
    with open(board_filename, 'w') as file:
        print(f"Saving board at '{board_filename}'...")
        dump_contents = json.dumps({"name":"user board", "board":board}, indent=4)
        file.write(dump_contents)
    
    return True


def get_board(board_filename):
    debug("get_board() called.")
    board = get_empty_board()

    try:
        with open(board_filename) as file:

            # json file (default)
            if '.json' in board_filename:
                print("Loading board from .json file...")
                board = json.load(file)
                if "board" in board.keys(): # valid json file
                    board = board["board"]
                else: board = get_empty_board() # invalid json file

            # txt file
            if '.txt' in board_filename:
                print("Loading board from .txt file...")
                for line in file:
                    if '[' in line and ']' in line:
                        board.append(line)

                new_board = []
                open_bracket_found = 0
                for line in board:
                    print(line)
                    for char in line:
                        if char == '[': open_bracket_found += 1
                        if char == ']': open_bracket_found -= 1
                        if open_bracket_found == 1:
                            new_line = []
                            if isinstance(char, int):
                                new_line.append(int(char))
                            new_board.append(new_line)

    except FileNotFoundError as error:
        print(error)
        print("Loading empty board...")
        return get_empty_board()

    else:
        print("Board load success.")
        return board


def get_empty_board():
    return [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    ]

def get_combined_board(board, user_board):
    combined_board = get_empty_board()
    for i, row in enumerate(combined_board):
        for j, column in enumerate(row):
            if   board[i][j]      != 0: combined_board[i][j] = board[i][j]
            elif user_board[i][j] != 0: combined_board[i][j] = user_board[i][j]

    return combined_board

# define
from debug import debug
class InvalidBoard(Exception):
    def __init__(self, msg="Invalid Board! Getting Empty board..."):
        super().__init__(msg)