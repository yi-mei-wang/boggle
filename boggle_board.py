import random
import boggle_helpers as bh


def check_word(word, board):
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

    anchors = []

    # Iterate through the rows of the board
    for y, row in enumerate(board):
        # Iterate through the elements of each row
        for x, elem in enumerate(row):
            # Check if the first letter is found
            if word[0] == elem:
                anchors.append((x, y))
                # If T is found in TEST, check if EST can be found
                # return check_around(word[1:], board, x, y, anchors)
    # return False
    return anchors


def check_around(word, board, x, y, history):
    """
    Parameters:
    -----------
    word : str
        A word or part thereof to search for in the board
    board : list
        A 2D list representing a board
    x : int
        The horizontal displacement of a char from the top-left-hand corner of the board
    y : int
        The vertical displacement of a char from the top-left-hand corner of the board
    history : list 
        Each element is a tuple representing the coordinates of past searches
    """

    # Exit condition: found the letter
    if len(word) == 0:
        return True

    print('word', word)
    print('history', history)
    print('x', x)
    print('y', y)

    # Possible places to search
    possibilities = bh.get_coords(x, y)
    print('possibilities', possibilities)
    print('possibilities[0]', possibilities[0])
    print(f'board[{possibilities[0][1]}][{possibilities[0][0]}]',
          board[possibilities[0][1]][possibilities[0][0]])

    new_x = possibilities[0][0]
    new_y = possibilities[0][1]

    # If the next character is found on the left, proceed to the next letter by slicing word
    if word[0] == board[new_y][new_x]:
        print('yes\n')
        history.append((new_x, new_y))
        return check_around(word[1:], board, new_x, new_y, history)

    # If found, continue by passing the co-ords to check (call get co-ords)
    # Look around the letter (remember to confine to the bounds of the board)
    # Get the co-ords to check
    # else:
    #     return check_around(word, board, , possibilities)


def find_in_coords(char, x, y, board):
    pos_to_check = bh.get_coords(x, y)

    new_coords = []

    for (new_x, new_y) in pos_to_check:
        if char == board[new_y][new_x]:
            new_coords.append((new_x, new_y))

    return new_coords


def find_word(word, anchors, board):
    if not len(word):
        return True

    # Go through every occurrence of the first char of word and search for the remainder of the word
    # Go through all occurrences of B
    for (x, y) in anchors:
        # If I can find the next char in the possible co-ordinates, I try to find the rest

        # Get the possible co-ordinates of the E in BEST
        possibilities = find_in_coords(word[0], x, y, board)

        # If E is found in the neighbouring cells of B,
        if possibilities:
            # Look for ST in all the occurrences of E
            if find_word(word[1:], possibilities, board):
                return True

    # If all the anchors have been searched and the word is still not found, trigger backtracking
    return False


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

        word_to_check = input('Enter the word to be checked: ').upper()

        anchors = check_word(word_to_check, board)
        print(anchors)

        print(find_word(word_to_check[1:], anchors, board))

        # Only check the rest of the word if the first word is found in the board
        # if not check_word(word_to_check, board):
        #     print('WORD NOT FOUND')

        # else:
        #     continue


play_game()
