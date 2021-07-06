
import pytest
import json

import validation
import file_interaction

t = True
f = False

def test_validate_input():
    
    # generate all valid positions and populate a list with them
    valid_positions = []
    for letter in validation.valid_letter_inputs:
        for number in validation.valid_number_inputs:
            valid_positions.append(f"{letter}{number}")

    # more valid input cases
    # lowercase letter
    more_valid_positions = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1"]
    for i in more_valid_positions:
        valid_positions.append(i)

    # invalid input cases
    invalid_inputs = [
        # invalid letter input
        "J5", "Z4",
        # invalid number input
        "AA", "AZ",
        # incorrect format (size)
        "A10", "AA1", 
        # use of no. 0
        "A0",
    ]

    # tests
    for position in valid_positions:
        assert validation.validate_input(position) == True # validate valid inputs
    
    for position in invalid_inputs:
        assert validation.validate_input(position) == False # test invalid inputs

def test_is_filled_square():

    # import board from file 
    with open("boards/131.05.Medium.json") as file:
        combined_board = json.load(file)
        combined_board = combined_board["board"]

    # create dict of all board positions with empty values
    valid_positions = {}
    for letter in validation.valid_letter_inputs:
        for number in validation.valid_number_inputs:
            combo = f"{letter}{number}"
            valid_positions[combo] = 0

    # hard-coded non-zero values from file
    board_values = {
        "A1" : 8,
        "B1" : 5,
        "F1" : 2,
        "G1" : 4,
        "A2" : 7,
        "B2" : 2,
        "I2" : 9,
        "C3" : 4,
        "D4" : 1,
        "F4" : 7,
        "I4" : 2,
        "A5" : 3,
        "C5" : 5,
        "G5" : 9,
        "B6" : 4,
        "E7" : 8,
        "H7" : 7,
        "B8" : 1,
        "C8" : 7,
        "E9" : 3,
        "F9" : 6,
        "H9" : 4,
    }

    # replace 0 with values for all valid values
    for key, value in board_values.items():
        if key in valid_positions.keys():
            valid_positions[key] = value

    # test
    for pair in valid_positions.items():
        key = pair[0]
        value = pair[1]
        if key in board_values.keys(): # square is filled
            assert validation.is_filled_square(key, combined_board) == True
        else: # square is empty
            assert validation.is_filled_square(key, combined_board) == False

def test_apply_game_rules():

    # import board from file 
    with open("boards/131.05.Medium.json") as file:
        combined_board = json.load(file)
        combined_board = combined_board["board"]

    empty_board = file_interaction.get_empty_board()
    
    # test valid inputs
    valid_inputs = {
        "C1" : 3,
        "H8" : 2,
    }
    
    # valid exceptions
    valid_exceptions = {
        "E5" : 0, # clear value
    }
    for key, value in valid_exceptions.items(): 
        valid_inputs[key] = value

    # test invalid inputs
    invalid_inputs = {
        "E1" : 5, # already in row
        "A8" : 8, # already in column
        "C2" : 8, # already in square
    }

    for key, value in valid_inputs.items():
        assert validation.apply_game_rules(key, combined_board, empty_board, value) == True

    for key, value in invalid_inputs.items():
        assert validation.apply_game_rules(key, combined_board, empty_board, value) == False

if __name__ == "__main__":
    pytest.main(["-v", "", "test_validation.py"])
