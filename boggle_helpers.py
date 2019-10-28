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


def empty_board(num):
    """Returns a blank board.

    Args:
    -----
        num: An int representing the desired dimension of the final board

    Returns:
    --------
        A num * num 2D list. The list contains num number of lists, where each child list contains num number of empty strings.
    """

    board = []
    for _ in range(num):
        board.append([''] * num)
    return board


def shake(dice, board):
    """Fills each spot in a board with a random side of a die.

    Replaces each element in a list of lists with a random char.

    Args:
    -----
        dice : A list of strings where each string represents a six-sided die
        board :  A list of lists that represents a Boggle board

    Returns:
    --------
        A board populated with random letters.
    """
    row = 0

    for index, die in enumerate(dice):
        col = index % 4

        board[row][col] = die[random.randint(0, 5)]

        if col == 3:
            row += 1

    return board


def shuffle(dice):
    """Shuffles the order of the elements in the list.

    Args:
    -----  
        dice : A list of strings

    Returns:
    --------
        A shuffled version of the original list.
    """
    random.shuffle(dice)
    return dice


def fill_board(n):
    """ Sets up a Boggle board.

    Populates a list of lists with randomly chosen letters.

    Args:
    -----
        n: An int representing the desired dimension of the resulting Boggle board

    Returns:
    --------
        A list containing n lists, which each contains n letters. For example:
        [['D', 'R', 'O', 'G'],
         ['S', 'X', 'R', 'H'],
         ['I', 'T', 'I', 'A'],
         ['H', 'S', 'N', 'P']]
    """

    # Shuffle the 16 dice
    dice = shuffle(DICE)

    # Fill the current board
    return shake(dice, empty_board(n))


def print_board(board):
    """Flattens and prints out an n * n board.

    Iterates through a 2D list and its constituent elements and prints them out neatly. 

    Args:
    -----
    board : A 2D list that represents a boggle board

    Returns:
    --------
    None
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


