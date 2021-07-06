"""
Name: Elijah Harrison
Program: Lab 05 - Sudoku

MAIN AND UI MODULES

Description: Play Sudoku!
What was the hardest part?
- The organization of the program, for sure. 
- (for part 1) Implementing the logic for the loop took some time, but it was pretty straightforward.
- I'm still working on the game logic, and I imagine that will be the most difficult to try and get working. 
- However, that's a requirement for me to only worry about in Lab 06 :)

How long did it take for you to complete the assignment?
- 2 hours
"""

# main module
# (other modules imported and aviailable for use before main is run)
def main():
    debug("in main.py: main called")

    # get board from file
    filename, board = load_board()

    # user board
    user_board_filename, user_board = load_user_board()

    # initiate ui
    msg = user_interaction(board, user_board)
    if   msg == "don't save": print("Exiting program.")
    elif msg == "save board":
        print("Saving board...")

        # save board...
        results = save_board(user_board_filename, user_board)
        if results: print("Save success.")
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
    else: return "save board"


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

