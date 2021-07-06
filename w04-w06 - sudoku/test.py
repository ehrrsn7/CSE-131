import validation
import json
import ui
import file_interaction

# generate all valid positions and populate a list with them
valid_positions = []
for letter in validation.valid_letter_inputs:
    for number in validation.valid_number_inputs:
        valid_positions.append(f"{letter}{number}")

with open("boards/131.05.Medium.json") as file:
    board = json.load(file)
    board = board["board"]

user_board = file_interaction.get_empty_board()

ui.display_board(board, user_board)

while True:
    user_board = ui.try_filling_square("prompt",   board, user_board)
    if input("Quit? ").lower() == 'q': break
