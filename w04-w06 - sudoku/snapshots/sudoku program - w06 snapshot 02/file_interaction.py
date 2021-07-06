"""
Program: Lab 05 - Sudoku
FILE INTERACTION MODULES
"""

# import
import json


def load_board(filename="boards/board.json"):
    debug("load_board() called.")
    return filename, get_board(filename)


def load_user_board(filename="boards/user_board.json"):
    debug("load_user_board() called.")
    return filename, get_board(filename)


def save_board(user_board:list, user_board_filename:str="boards/user_board.json"):
    debug("save_board() called.")

    with open(user_board_filename, 'w') as file:
        print("Saving board...")
        file.write(json.dumps({"board": user_board}))
    return True


def get_board(board_filename):
    debug("get_board() called.")
    try:
        with open(board_filename) as file:
            board = json.load(file)

    except FileNotFoundError as error:
        debug(error)
        return get_empty_board()
    
    else:
        board = board["board"]
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

# define
from debug import debug
class InvalidBoard(Exception):
    def __init__(self, msg="Invalid Board! Getting Empty board..."):
        super().__init__(msg)