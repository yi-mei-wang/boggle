import random
import boggle_helpers as bh


def check_first_word(word, board):
    """
    Searches for the first letter of a given word in a board.

    Parameters:
    -----------
    word : str
        The string to search for

    board : list
        A 2D 4x4 list where each element is a random letter

    Returns:
    --------
    bool
        True if the first letter of word is found, and vice versa.
    """

    # Iterate through the rows of the board
    for row in board:
        # Iterate through the elements of each row
        for elem in row:
            if word[0] == elem:
                return True
    # Check if the first letter is found


def setup():
    # Initialise an empty board
    board = bh.empty_board(4)

    # Shuffle the 16 dice
    dice = bh.shuffle(bh.DICE)

    # Fill the current board
    return bh.shake(dice, board)


def play_game():
    board = setup()

    while True:
        bh.print_board(board)

        word_to_check = input('Enter the word to be checked: ')

        # Only check the rest of the word if the first word is found in the board
        if not check_first_word(word_to_check, board):
            print('WORD NOT FOUND')

        else:
            continue


play_game()
