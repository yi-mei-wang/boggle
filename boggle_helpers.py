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
        num: An int representing the desired dimension of the final board

    Returns:
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
    """Generates the coordinates of all neighbouring cells of the provided cell.

    Generates the coordinates of the cells to the left, right, top, bottom and diagonal of a cell based on the x- and y-coordinates provided.

    Args:
    -----
        x : An int representing the x-coordinate of a cell
        y : An int representing the y-coordinate of a cell

    Returns:
    --------
        A list of tuples representing the coordinates of the neighbouring cells of a given cell. Only cells within the confines of a 4 * 4 board are included.
    """
    coords = [
        # Right
        (x + 1, y),
        # Left
        (x - 1, y),
        # Top
        (x, y - 1),
        # Bottom
        (x, y + 1),
        # Diagonals
        (x - 1, y - 1),
        (x + 1, y + 1),
        # Anti-diagonals
        (x + 1, y - 1),
        (x - 1, y + 1)
    ]

    return [coord for coord in coords if coord[0] >= 0 and coord[0] <= 3 and coord[1] >= 0 and coord[1] <= 3]


def binary_search(target, my_list):
    # Check the midpoint of the list
    start = 0
    endpoint = len(my_list) - 1
    midpoint = (start + endpoint) // 2

    if start > endpoint:
        return False

    else:
        if target == my_list[midpoint]:
            return True

        elif target < my_list[midpoint]:
            # endpoint = midpoint - 1
            return binary_search(target, my_list[0:midpoint])

        elif target > my_list[midpoint]:
            # start = midpoint + 1
            return binary_search(target, my_list[midpoint+1:])
