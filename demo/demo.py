import random

###########
# Helpers #
###########
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


def shuffle(dice):
    """Shuffles the order of the elements in the list.
    """
    copy = dice[:]
    random.shuffle(copy)
    return copy


def empty_board(num):
    """Returns a blank board.
    """

    board = []
    for _ in range(num):
        board.append([''] * num)
    return board


def shake(dice, board):
    """Fills each spot in a board with a random side of a die.
    """
    row = 0

    for index, die in enumerate(dice):
        col = index % 4

        board[row][col] = die[random.randint(0, 5)]

        if col == 3:
            row += 1

    return board


def fill_board(n):
    """ Sets up a Boggle board.
    """

    # Shuffle the 16 dice
    dice = shuffle(DICE)

    # Fill the current board
    return shake(dice, empty_board(n))


def print_board(board):
    """Flattens and prints out an n * n board.
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


#############
# SEARCH FNs#
#############


def find_first_char(char, board):
    """Returns ALL the occurrences of the first letter of a given char in a board.
    """

    first_char_coords = []

    # Iterate through the rows of the board
    for y, row in enumerate(board):
        # Iterate through the elements of each row
        for x, elem in enumerate(row):
            # Check if the first letter is found
            if char == elem:
                first_char_coords.append((x, y))

    print(f'\n{char} is found in {first_char_coords}\n')

    return first_char_coords


def get_neighbour_coords(x, y):
    """Generates the coordinates of all surrounding cells of the provided cell.
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


def get_possible_coords(char, x, y, board, history):
    """Finds the coordinates of a char, if present on the board, based on the coordinates of the anchor provided.

    Searches for char in all the neighbouring cells of the anchor. Takes into account previous searches so a previously-used cell cannot be reused.
    """
    pos_to_check = get_neighbour_coords(x, y)

    new_coords = []

    for (new_x, new_y) in pos_to_check:
        if (new_x, new_y) not in history:
            if char == board[new_y][new_x]:
                new_coords.append((new_x, new_y))

    return new_coords


def find_word(word, first_char_coords, board, history):
    """Recursively searches for part of a word using the starting points given.
    """

    # Exit condition
    if not len(word):
        return True

    # Go through every occurrence of the first char of word
    for (x, y) in first_char_coords:
        print(f'Searching for {word[0]} from around ({x}, {y})')

        # Check surrounding cell for the next char
        possibilities = get_possible_coords(word[0], x, y, board, history)

        print(f'{word[0]} is found in {possibilities}\n')

        # If the next char is found in surrounding cells
        if possibilities:
            # Tentative add current cell to history
            history.append((x, y))

            # Look for the subsequent char down this path
            if find_word(word[1:], possibilities, board, history):
                return True

            # Remove from history if current path does yield the remaining chars
            history.remove((x, y))

    # If all the first_char_coords have been searched and the word is still not found, trigger backtracking
    return False
