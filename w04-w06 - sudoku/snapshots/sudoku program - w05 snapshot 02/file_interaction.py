"""
Program: Lab 05 - Sudoku
FILE INTERACTION MODULES
"""

def load_board(filename="boards/board.txt"):
    debug("load_board() called.")
    return filename, get_board(filename)


def load_user_board(filename="boards/user_board.txt"):
    debug("load_user_board() called.")
    return filename, get_board(filename)


def save_board(user_board, user_board_filename="boards/user_board.txt"):
    debug("save_board() called.")
    success = True
    # TODO: display success/failure to save statements
    return success


def get_board(board_filename):
    debug("get_board() called.")
    board = []
    try:
        with open(board_filename) as file:
            for i, line in enumerate(file):
                board.append(line.strip())

    except FileNotFoundError as error:
        debug(error)
        return get_empty_board()
    
    else:
        board_list = []

        for line in board:
            new_line = []

            for char in line:
                if char.isnumeric(): new_line.append(int(char))

            if len(new_line) == 9:
                board_list.append(new_line)

        return board_list


def get_empty_board():
    return [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

# define
from debug import debug
class InvalidBoard(Exception):
    def __init__(self, msg="Invalid Board! Getting Empty board..."):
        super().__init__(msg)