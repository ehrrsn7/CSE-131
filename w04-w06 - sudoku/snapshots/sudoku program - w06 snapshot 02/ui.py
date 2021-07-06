"""
Program: Lab 05 - Sudoku
UI MODULES
"""

# import
from debug import debug
from file_interaction import (
    get_empty_board,
    save_board
)
from validation import (
    validate_input,
    is_filled_square,
    apply_game_rules
)

# define
formatting = False
column_positions = { 'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8 }

"""
PROMPT
"""
def prompt(board, user_board):
    debug("in ui.py: prompt() called.")
    while True:

        # display prompt, format input
        print(">", colors["bold"], colors["underline"], end="")

        # prompt input
        user_input = input().upper()
        print(colors["clear"], end="")

        # handle input
        if user_input == "CLEAR": user_board = clear_board(board, user_board)
        elif user_input == 'Q': return user_board
        elif user_input == 'S': save_board(user_board)
        elif user_input == 'W': return False
        elif user_input == 'C': display_commands()
        elif user_input == 'D': display_board(board, user_board)
        elif user_input == 'E': user_board = try_filling_square("prompt",   board, user_board)
        else:                   user_board = try_filling_square(user_input, board, user_board)

        print()


"""
COMMANDS
"""
commands = {
    "COMMAND"   : "DESCRIPTION",
    "-------"   : "------------",
    "q"         : "Save and Quit Game",
    "s"         : "Save Game",
    "w"         : "Quit Game (without saving)",
    "c"         : "View Commands Again",
    "d"         : "Display Board",
    "e"         : "Edit Square (Enter Coordinates)",
    "clear"     : "Clear Board (only clearing user input)"
}

colors = {
    "header"    : '\033[95m',
    "blue"      : '\033[94m',
    "cyan"      : '\033[96m',
    "green"     : '\033[92m',
    "warning"   : '\033[93m',
    "fail"      : '\033[91m',
    "bold"      : '\033[1m',
    "underline" : '\033[4m',
    "clear"     : '\033[0m'
}

def display_commands():
    # display instructions, set header/table styling
    print("\nTo use this program, please enter any of the following:", 
        colors["cyan"], colors["bold"])

    # print commands
    for command in commands:
        print(f"{command:8}: {commands[command]}")

        # end header styling, reset table styling
        if command == "COMMAND":
            if formatting: print(colors["clear"], colors["cyan"], end="")
    print(colors["clear"]) # end table styling
        


"""
BOARD: EDIT
"""
def try_filling_square(user_input, board, user_board):
    debug("try_filling_square() called,")

    # display instructions/reprompt (but only when 'e' was initially pressed.)
    if user_input == "prompt":
        print("\n"
            "Enter the coordinates of the square you would like to edit.\n"
            "They can only a combination of one letter and one number.\n"
            "Letter must be in range from A to I.\n"
            "Number must be in range from 1 to 9.\n"
        )
        user_input = input("Please enter coordinates: ").capitalize()

    # validate input    
    if not validate_input(user_input):
        print("Invalid user input.")
    else:
        debug("user input validated.")

        # check if square was filled
        if not is_filled_square(user_input, board):
            debug("Square is free to edit.")

            # edit board
            user_board = edit_board(user_input, board, user_board)

            # display board
            display_board(board, user_board)

    return user_board


def edit_board(user_input, board, user_board):
    debug("edit_board() called.")

    # prompt user for a number to fill the square with
    value = get_int("Please enter a number:   ")

    # apply game rules
    if not apply_game_rules(user_input, get_combined_board(board, user_board), value):
        # if game rules were validated, leave function without editing
        pass

    else:
        # get row/column indexes
        letter = str(user_input[0])
        number = int(user_input[1])
        debug(f"square: '{letter}{number}'")
        row     = number - 1
        column  = column_positions[letter]

        # edit square
        print(f"Assigning {value} to {user_input}.")
        user_board[row][column] = value

        # debug
        debug("New value (in user board):", user_board[row][column])
        from debug import DEBUG
        if DEBUG:
            print("New user board:")
            display_board(get_empty_board(), user_board)

    return user_board


def clear_board(board, user_board):
    print("Clearing board...")
    user_board = get_empty_board()
    print("Board restored to original state.")
    display_board(board, user_board)
    return get_empty_board()


"""
BOARD: DISPLAY
"""
def display_board(board, user_board):
    print(colors["green"], get_board(get_combined_board(board, user_board)), colors["clear"])


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
        for j, column in enumerate(row):
            if   board[i][j]      != 0: combined_board[i][j] = board[i][j]
            elif user_board[i][j] != 0: combined_board[i][j] = user_board[i][j]

    return combined_board


"""
OTHER
(Helper function for prompt)
"""
def get_int(*prompt):
    for i in range(2):
        try:
            txt = ""
            for text in prompt: txt += text + " "; prompt = txt
            return int(input(prompt))
        except ValueError as error: print(error)
        else: break

def toggle(condition: bool): return not condition