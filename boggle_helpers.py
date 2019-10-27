import random

DICE = ["AAEEGN",
        "ELRTTY",
        "AOOTTW",
        "ABBJOO",
        "EHRTVW",
        "CIMOTU",
        "DISTTY",
        "EIOSST",
        "DELRVY",
        "ACHOPS",
        "HIMNQU",
        "EEINSU",
        "EEGHNW",
        "AFFKPS",
        "HLNNRZ",
        "DEILRX"]

# Generate a 4 x 4 board


def empty_board(num):
    """
    Returns a blank board.
    """

    board = []
    for _ in range(num):
        board.append(['-'] * num)
    return board


def shake(dice, board):
    """
    Fills each spot in the board with a random side of a die.

    Parameters:
    ---
    A list of strings where each string represents a six-sided die.

    Returns:
    ---
    A filled board
    """
    row = 0

    for index, die in enumerate(dice):
        col = index % 4

        board[row][col] = die[random.randint(0, 5)]

        if col == 3:
            row += 1

    return board


def shuffle(dice):
    """
    Shuffle the arrangement of the dice in the list
    """
    random.shuffle(dice)
    return dice


def print_board(board):
    """
    Prints out a 2d board.
    """
    print('-' * 10)

    for row in board:
        for letter in row:
            if letter == 'Q':
                letter = 'Qu'
            print(letter.ljust(2), end=' ')

        # Start the next row on a new line
        print('\r')

    print('-' * 10)


def get_coords(x, y):
    left = {"x": x - 1, "y": y}
    right = {"x": x + 1, "y": y}

    coords = []

    if x != 0:
        coords.append(left)

    if x != 3:
        coords.append(right)

    return coords
