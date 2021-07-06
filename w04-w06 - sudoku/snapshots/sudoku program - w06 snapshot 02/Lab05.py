"""
Name: Elijah Harrison
Program: Lab 05 - Sudoku Draft

MAIN AND UI MODULES

Description: Play Sudoku!
What was the hardest part?
- The DUMBEST little bug - my program wasn't displaying the 
    user's changes... I wasn't sure if it was even editing the board.
    The fix was changing the return value of 'get_combined_board'
    from 'board' to 'combined_board'. My program was working all along!
- Another bug: after editing, and after, editing my board, unless 
    saving within the program, my user_board would revert to its 
    original values... I realized I never put a return value for 
    user_board for neither 'prompt' nor 'try filling square'. 
    I put a return value in, and then voilá! :)

How long did it take for you to complete the assignment?
- 2 hours
"""

# main module
# (other modules imported and available for use before main is run)
def main():
    debug("in main.py: main called")

    # get board from file
    filename, board = load_board()

    # user board
    user_board_filename, user_board = load_user_board()

    # initiate ui
    result = user_interaction(board, user_board)

    # initiate exit routine (with or w/out saving - depending on ui)
    if result == "don't save":
        print("Exiting program.\n")

    elif isinstance(result, list):
        # save board...
        result = save_board(result)
        if result:  print("Save success.")
        else:       print("Save failed.")


# user interaction module
def user_interaction(board, user_board):
    debug("in main.py: ui() called.")

    # display board once
    display_board(board, user_board)

    # display commands once
    display_commands()

    # loop prompt
    final_result = prompt(board, user_board)

    if final_result == False: return "don't save"
    elif isinstance(final_result, list):
        user_board = final_result
        return user_board


# read/write to file
from file_interaction import load_board
from file_interaction import load_user_board
from file_interaction import save_board

# user interaction functions
from ui import display_commands
from ui import display_board
from ui import prompt 

# debug function
from debug import debug

# run
if __name__ == "__main__": main()

