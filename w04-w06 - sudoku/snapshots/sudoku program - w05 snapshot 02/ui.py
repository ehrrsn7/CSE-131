"""
Program: Lab 05 - Sudoku
UI MODULES
"""
from debug import debug
from validation import (
    validate_input,
    is_filled_square
)

def prompt(board, user_board):
    debug("in ui.py: prompt() called.")
    for i in range(200):

        # display prompt
        user_input = input("> ").capitalize()

        if   user_input == 'Q': return user_board
        if   user_input == 'W': return False
        elif user_input == 'C': display_commands()
        elif user_input == 'D': display_board(board, user_board)
        else: try_filling_square(user_input, board, user_board)

        print()


def try_filling_square(user_input, board, user_board):
    if validate_input(user_input):
        if is_filled_square(user_input, board, user_board):
            user_board = edit_board(user_input, user_board)
            display_board(board, user_board)


def edit_board(user_input, user_board):
    value = get_int("Please enter a number: ")
    print(f"Assigning {value} to {user_input}.")
    try: user_board[int(user_input[1])][column_positions[user_input[0]]] = value
    except ValueError as error: print(error)
    print(f"Successfully reassigned value to {user_board[int(user_input[1])][column_positions[user_input[0]]]}")
    return user_board

column_positions = { 'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8 }


def get_int(*prompt):
    for i in range(10):
        try:
            txt = ""
            for text in prompt: txt += text + " "; prompt = txt
            return int(input(prompt))
        except ValueError as error: print(error)
        else: break


def display_board(board, user_board):
    print(get_board(get_combined_board(board, user_board)))


def get_board(whichever_board):
    board_str = "\n   A B C   D E F   G H I \n"

    for i, row in enumerate(whichever_board):
        if i == 3 or i == 6: board_str += "\n   - - - + - - - + - - -"
        board_str += f"\n{i + 1}  "

        for j, value in enumerate(row):
            if value == 0: board_str += "  "
            else: board_str += f"{value} "
            if j == 2 or j == 5: board_str += "| "

    return board_str


from file_interaction import get_empty_board
def get_combined_board(board, user_board):
    combined_board = get_empty_board()
    for i, row in enumerate(combined_board):
        # print(row)
        for j, column in enumerate(row):
            if   board[i][j]      != 0: combined_board[i][j] = board[i][j]
            elif user_board[i][j] != 0: combined_board[i][j] = user_board[i][j]

    return board


def display_commands():
    # define commands
    commands = {
        "COMMAND"   : "DESCRIPTION",
        "-------"   : "------------",
        "q"         : "Save and Quit Game",
        "w"         : "Quit Game (without saving)",
        "c"         : "View Commands Again",
        "d"         : "Display Board",
        "Letter-number combination (ex: 'A1')": "Edit Square"
    }

    # display commands
    print("\nTo use this program, please enter any of the following:")
    for command in commands:
        print(f"{command:8}: {commands[command]}")

