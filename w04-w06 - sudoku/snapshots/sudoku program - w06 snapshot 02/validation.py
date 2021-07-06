"""
Program: Lab 05 - Sudoku
VALIDATION MODULES
"""

# import
from debug import debug

# define
valid_number_inputs = [ 1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 ]
valid_letter_inputs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
column_positions    = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8 }


# functions
def validate_input(user_input:str):
    debug("validate_input() called.")

    # check if in format 'a1' (letter/number combo)
    if not isinstance(user_input, str): return False # must be a str
    if not len(user_input) == 2:        return False # must have length of 2
    if not user_input[0].isalpha():     return False # first char must be a letter
    if not user_input[1].isnumeric():   return False # second char must be an int

    # check if in correct range
    letter = str(user_input[0])
    number = int(user_input[1])
    debug(f"input: '{letter}{number}'")

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
    print("Error: square already has pre-defined value.")
    return True


def apply_game_rules(user_input, combined_board, value):
    debug("apply_game_rules() called.")
    if value == 0: return True # ('clear' current value - assign to zero)

    # get user input in terms of letter/number
    letter = str(user_input[0]).capitalize()
    number = int(user_input[1])
    debug(f"square: '{letter}{number}'")
    # get location in terms of row/column
    row     = number - 1
    column  = column_positions[letter]

    # input value must be in valid range
    if value not in range(10):
        print(
            "Error: input value not in correct range."
            "Must be a number between 1 and 9."
        )
        return False

    # validate by row
    for cell in combined_board[row]:
        if value == cell:
            print("Unfortunately, this number already is in this row.")
            return False

    # validate by column
    # get column vals
    column_vals = []
    for row in combined_board:
        column_vals.append(row[column])
    # check column vals (just like with the row)
    for cell in column_vals:
        if value == cell:
            print("Unfortunately, this number already is in this column.")
            return False

    # validate by square

    # for reference:
    #     |     |    
    #  A  |  D  |  G 
    # ----+-----+----
    #  B  |  E  |  H 
    # ----+-----+----
    #  C  |  F  |  I 
    #     |     |    

    # get cell contents
    cell_contents = []

    if column in ['A', 'B', 'C']:
        for each_column in ['A', 'B', 'C']:

            # A
            if row in [1, 2, 3]:
                for each_row in [1, 2, 3]:
                    cell_val = combined_board[row][column_positions[column]]
                    if cell_val != 0: cell_contents.append(cell_val)

            # B
            elif row in [4, 5, 6]:
                for each_row in [4, 5, 6]:
                    cell_val = combined_board[row][column_positions[column]]
                    if cell_val != 0: cell_contents.append(cell_val)

            # C
            elif row in [7, 8, 9]:
                for each_row in [7, 8, 9]:
                    cell_val = combined_board[row][column_positions[column]]
                    if cell_val != 0: cell_contents.append(cell_val)


    if column in ['D', 'E', 'F']:
        for each_column in ['D', 'E', 'F']:

            # A
            if row in [1, 2, 3]:
                for each_row in [1, 2, 3]:
                    cell_val = combined_board[row][column_positions[column]]
                    if cell_val != 0: cell_contents.append(cell_val)

            # B
            elif row in [4, 5, 6]:
                for each_row in [4, 5, 6]:
                    cell_val = combined_board[row][column_positions[column]]
                    if cell_val != 0: cell_contents.append(cell_val)

            # C
            elif row in [7, 8, 9]:
                for each_row in [7, 8, 9]:
                    cell_val = combined_board[row][column_positions[column]]
                    if cell_val != 0: cell_contents.append(cell_val)


    if column in ['G', 'H', 'I']:
        for each_column in ['G', 'H', 'I']:

            # A
            if row in [1, 2, 3]:
                for each_row in [1, 2, 3]:
                    cell_val = combined_board[row][column_positions[column]]
                    if cell_val != 0: cell_contents.append(cell_val)

            # B
            elif row in [4, 5, 6]:
                for each_row in [4, 5, 6]:
                    cell_val = combined_board[row][column_positions[column]]
                    if cell_val != 0: cell_contents.append(cell_val)

            # C
            elif row in [7, 8, 9]:
                for each_row in [7, 8, 9]:
                    cell_val = combined_board[row][column_positions[column]]
                    if cell_val != 0: cell_contents.append(cell_val)


    # check square vals
    for cell in cell_contents:
        if value == cell:
            print("Unfortunately, this number already is in this column.")
            return False
    
    # passed all tests
    return True


