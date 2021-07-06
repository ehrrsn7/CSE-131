"""
Program: Lab 05 - Sudoku
VALIDATION MODULES
"""

# import
from debug import debug
from file_interaction import get_combined_board

# define
valid_number_inputs = [ 1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 ]
valid_letter_inputs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
column_positions    = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8 }


# functions
def validate_input(user_input:str):
    debug("validate_input() called.")

    # case in-sensitive
    user_input = user_input.upper()

    # check if in format 'a1' (letter/number combo [case in-sensitive ('letter.upper()' used below)])
    if (# must be a str 
        not isinstance(user_input, str) or 

        # must have length of 2
        len(user_input) != 2):
        
        print("Unfortunately, this input is in the incorrect format... ")
        print("Please enter a a letter & number (ex: 'a5')")
        print("\t* Case is not sensitive *")
        print()
        return False

    # invalid characters
    if not user_input[0].isalnum() or not user_input.isalnum(): 
        print("Unfortunately, this input is in the incorrect format... ")
        print("The input cannot be non-alphanumeric characters")
        print()
        return False

    valid_letternum_format = False
    if user_input[0].isalpha() and user_input[1].isnumeric(): # format 'a1'
        valid_letternum_format = True
    if user_input[0].isnumeric() and user_input[1].isalpha(): # format '1a'
        valid_letternum_format = True

        # swap user_input letter and number combination if it is in the format '1a'
        user_input = f"{user_input[1]}{user_input[0]}"

    if not valid_letternum_format:
        print("Unfortunately, this input is in the incorrect format... ")
        print("The input must have one character and one number")
        print("ex: 'a1' or '1a' (both are the same coordinate, and both are valid)")
        print()
        return False
   
    # check if in correct range
    print(user_input)
    letter = str(user_input[0])
    number = int(user_input[1])

    if letter not in valid_letter_inputs:
        print("Error: letter out of range. Please enter a letter between A and I.")
        return False
    debug("Letter Validated.")

    if number not in valid_number_inputs:
        print("Error: number out of range. Please enter a number between 1 and 9.")
        return False
    debug("Number Validated.")

    # passed all tests = valid
    return True


def is_filled_square(user_input, board):
    debug("is_filled_sqaure() called.")

    # swap user_input letter and number if in format 
    
    # get user input in terms of letter/number
    letter = str(user_input[0]).capitalize()
    number = int(user_input[1])
    debug(f"square: '{letter}{number}'")

    # get location in terms of row/column
    row     = number - 1
    column  = column_positions[letter]

    # check value at position
    debug(f"Value at {user_input}:", board[row][column])
    if board[row][column] == 0: return False # passed test -- empty square :)

    # return True if square was filled
    print(f"Error: square {user_input} already has pre-defined value [{board[row][column]}]")
    return True


def apply_game_rules(user_input, board, user_board, value):
    debug("apply_game_rules() called.")

    # double-check if we've validated our input
    assert validate_input(user_input) == True
    
    combined_board = get_combined_board(board, user_board)
    
    # get user input in terms of letter/number
    letter = str(user_input[0]).capitalize()
    number = int(user_input[1])
    debug(f"square: '{letter}{number}'")
    # get location in terms of column/row
    column  = column_positions[letter]
    row     = number - 1

    # board is already filled
    if is_filled_square(user_input, board): return False

    # if board is not filled, clear if value is 0
    if value == 0: return True

    # input value must be in valid range
    if value not in range(10):
        print(
            "Error: input value not in correct range."
            "Must be a number between 1 and 9."
        )
        return False

    # double-check -- if value == 0 it will cause errors in the code below
    assert value != 0

    # validate by row
    if value in combined_board[row]:
        print(f"Unfortunately, this number [{value}] already is in this row. [position '{user_input}']")
        return False

    # validate by column
    # get column vals
    column_vals = []
    for row_i in combined_board:
        column_vals.append(row_i[column])
    # check column vals (just like with the row)
    if value in column_vals:
        print(f"Unfortunately, this number [{value}] already is in this column. [position '{user_input}']")
        return False

    # check if value already exists in square
    if not validate_by_square(column, row, combined_board, value, user_input): 
        return False

    # passed all tests
    return True

def validate_by_square(column, row, combined_board, value, user_input):

    valid   = True
    invalid = False

    # empty list to keep track of non-zero contents of square
    cell_contents = []

    # asserts for testing
    assert column in range(0, 8)
    assert row in range(0, 8)

    # the rows associated with square containing the coordinate:
    for row_i in range(int(row/3) * 3, int(row/3) * 3 + 3): 

        # the columns associated with square containing the coord:
        for col_i in range(int(column/3) * 3, int(column/3) * 3 + 3):
            cell_i_val = combined_board[row_i][col_i]
            if cell_i_val != 0:
                cell_contents.append(combined_board[row_i][col_i])
    
    # value matches a number found in the square containing the coord
    if value in cell_contents: 
        print(f"Unfortunately, this number [{value}] already is in this square. [position '{user_input}']")
        return invalid
    
    # value does not match any value in square
    return valid
