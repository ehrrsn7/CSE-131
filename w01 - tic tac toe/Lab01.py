# 1. Name:
#      Elijah Harrison
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      This assignment was pretty straightforward. I personally
#      am not very good with Dictionaries, but I looked them up
#      online and did some workarounds with them...I'm proud to
#      say I used them pretty intuitively in this assignment :)
#      The part that took the longest was figuring out bugs 
#      which ultimately had to do with my use of dictionaries.
#      - Demonstration video: https://youtu.be/qELhUf52FE4
# 5. How long did it take for you to complete the assignment?
#      1 Hour

# define/import
import json
import random

DEBUG = False
def debug(text):
    if DEBUG:
        print("\ndebug:", text)

# The characters used in the Tic-Tac-Too board
X = 'X'
O = 'O'
Blank = ' '
X_or_O_init = bool(random.getrandbits(1)) # random True or False

# A blank Tic-Tac-Toe board
def new_blank_board_list():
    return [
        # list of 'chars' (one-letter strings)
        Blank, Blank, Blank,
        Blank, Blank, Blank,
        Blank, Blank, Blank
    ]

def new_blank_board():
    return {
        "board": new_blank_board_list(),
        "x_or_nah": X_or_O_init, # bool
        "quit_game": False
    }

class Missing_File_Error(Exception):
    def __init__(self, message="Missing file!"):
        super().__init__(message)

def read_board(filename):
    '''Read the previously existing board from the file if it exists'''
    # Put file reading code here

    new_board = new_blank_board_list()

    try:
        """Read file into str"""
        board_str = str() # initialize
        with open(filename, 'r') as file: # read
            for line in file:
                if len(board_str) != 9: raise Missing_File_Error()
                for char, i in enumerate(line):
                    board_str[i] = char # set characters

    except Missing_File_Error as error:
        debug(error)

    else:
        """Create new board"""
        for char in board_str:
            if char == '.': char = ' '
            else: char = char.upper()
            new_board.append(char)

    """Return list"""
    return new_board

def save_board(board, filename="saved_board.txt", message=False):
    '''Save the current game to a file.'''
    # Put file writing code here

    # message
    print("Saving...")

    """Convert board to str"""
    board_str = str()
    for square in board["board"]:
        if square == ' ': square = '.'
        board_str += square
    
    """Save str to file"""
    with open(filename, 'w') as file:
        file.write(board_str)

def display_board(board: dict):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way'''
    # Put display code here
    board_list = []
    board_list = board.get("board")
    print(f" {board_list[0]} | {board_list[1]} | {board_list[2]} ")
    print(f"---+---+---")
    print(f" {board_list[3]} | {board_list[4]} | {board_list[5]} ")
    print(f"---+---+---")
    print(f" {board_list[6]} | {board_list[7]} | {board_list[8]} ")

    debug(board)

def is_x_turn(board: dict):
    """
    Determine whose turn it is
    """

    # debug
    debug("is_x_turn() called.")

    # Put code here determining if it is X's turn
    if board["x_or_nah"]:
        debug("x_or_nah == True (is now being set to false...)")
        board["x_or_nah"] = False
        return True
    else:
        board["x_or_nah"] = True
        return False

def get_player_input(board: dict):
    # debug
    debug("get_player_input() called.")

    """
    once every round, get player input, 
    first from x, then from y
    """
    if is_x_turn(board):
        player_input = input("\nX> ")
    else:
        player_input = input("\nO> ")
    
    debug(f"Player input recorded. ({player_input})")

    """
    Check condition where user input 'Q'
    """
    if player_input.isalpha():
        if player_input.upper() == "Q":
            debug("player input == 'q'")
            board["quit_game"] = True
            return True # functionality built-in: quit program and save when 'q' is pressed.
    else:
        """
        Convert input to int, handle errors
        """
        try: player_input = int(player_input) # get input
       
        except ValueError as error: # handle errors
            print(error)

        else: # debug
            debug("Correct input type :)!")

            player_input -= 1 # set value for list manipulation
            if player_input not in range(0, 9): # one last check
                player_input = Blank

            """
            Before we set the values, check if square was already used.
            """
            if board["board"][player_input] == Blank:

                """
                Set values
                """
                if not board["x_or_nah"]:
                    board["board"][player_input] = X # set X value
                else:
                    board["board"][player_input] = 'O' # set O value
            
            else:
                debug("Square is already used!")

def game_done(game_board: dict, message=False):
    # debug
    debug("game_done() called.")

    # access game board (list) within board dictionary
    board = game_board["board"]

    '''Determine if the game is finished'''
    # Game is finished if all the squares are filled
    tie = True
    for square in board:
        if square == Blank:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True

    # Game is finished if someone has completed a row
    for row in range(3):
        if board[row * 3] != Blank and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True
    # Game is finished if someone has completed a column
    for col in range(3):
        if board[col] != Blank and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True
    # Game is finished if someone has a diagonal
    if board[4] != Blank and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True
    return False

def play_game(board: dict):
    '''Play the game of Tic-Tac-Toe'''
    # Put game play code here. Return False when the user has indicated they are done
    while True:
        # once every round, display board
        display_board(board)

        # get player input
        quit_game = get_player_input(board)

        # save and quit game if input == 'q' 
        if quit_game:
            save_board(board, "saved_board.txt")
            break

        # debug
        debug("in play_game(): get_player_input() successful.")

        # once every round, check to see if game end requirements are met
        done = game_done(board, True)
        if done:
            debug("Game done.")
            display_board(board)
            save_board(new_blank_board())
            break

    return False


# The file read code, game loop code, and file close code goes here
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# set up board
board = new_blank_board()
debug(board)

# check for board on file
if read_board("saved_board.txt") != False:
    board["board"] = read_board("saved_board.txt")

# play the game! :)
play_game(board)
