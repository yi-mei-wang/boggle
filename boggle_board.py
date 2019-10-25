import random
import boggle_helpers as bh


def play_game():
    # Initialise an empty board
    board = bh.empty_board(4)

    # Shuffle the 16 dice
    dice = bh.shuffle(bh.DICE)

    # Fill and print the current board
    bh.print_board(bh.shake(dice, board))


play_game()
