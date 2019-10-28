import random
import boggle_helpers as bh


def check_first_letter(word, board):
    """Searches for the first letter of a given word in a board.

    Iterates through the board to obtain the coordinates of all the occurrences of the first char of word.

    Args: 
    -----
        word : A string containing the word to search for
        board : A 2-D list whose each element is a random letter

    Returns:
    --------
        A list containing coordinates of where the first letter occurs in the board 
    """

    anchors = []

    # Iterate through the rows of the board
    for y, row in enumerate(board):
        # Iterate through the elements of each row
        for x, elem in enumerate(row):
            # Check if the first letter is found
            if word[0] == elem:
                anchors.append((x, y))

    print(f'\n{word[0]} is found in {anchors}\n')

    return anchors


def find_in_coords(char, x, y, board, history):
    """Finds a char based on the coordinates provided.

    Searches for char in all the neighbouring cells of the starting point, which is represented by the x- and y-coordinates provided. Takes into account previous searches so a previously-used cell cannot be reused.

    Args:
    -----
        char : A single character to be searched for
        x : An int representing the x-coordinate of the starting point
        y : An int representing the y-coordinate of the starting point
        board : A 2-D list whose each element is a random letter
        history : A list of coordinates of past searches

    Returns:
    --------
        A list of the new coordinates to search.
    """
    pos_to_check = bh.get_coords(x, y)

    new_coords = []

    for (new_x, new_y) in pos_to_check:
        if (new_x, new_y) not in history:
            if char == board[new_y][new_x]:
                new_coords.append((new_x, new_y))

    return new_coords


def find_word(word, anchors, board, history):
    """ Finds a word in a Boggle board.

    Searches for a word or part thereof in a Boggle board using the coordinates given. Uses the backtracking algorithm to search depth first. 

    Args:
    -----
        word : A string representing the word to be searched for or part thereof
        anchors : A list of coordinates of where the word should be searched in relation to
        board : A 2-D list representing a Boggle board
        history : A list of coordinates of past searches

    Returns:
    --------
        A boolean indicating whether the word is found or not
    """

    # Exit condition
    if not len(word):
        return True

    # Go through every occurrence of the first char of word and search for the remainder of the word
    for (x, y) in anchors:
        print(f'Searching for {word[0]} from around ({x}, {y})')

        possibilities = find_in_coords(word[0], x, y, board, history)

        print(f'{word[0]} is found in {possibilities}\n')

        # If E is found in the neighbouring cells of B,
        if possibilities:
            history.append((x, y))

            # Look for ST in all the occurrences of E
            if find_word(word[1:], possibilities, board, history):
                return True

    # If all the anchors have been searched and the word is still not found, trigger backtracking
    return False


def setup(n):
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
    dice = bh.shuffle(bh.DICE)

    # Fill the current board
    return bh.shake(dice, bh.empty_board(n))


def play_game():
    board = setup(4)

    filename = '/Users/mei/work/teaching/python-sep-19/day-3/recursion/boggle/dictionary.txt'
    dictionary = [line.rstrip('\n') for line in open(filename)]

    while True:
        bh.print_board(board)

        word_to_check = input('Enter the word to be checked: ').upper()

        anchors = check_first_letter(word_to_check, board)

        if find_word(word_to_check[1:], anchors, board, []):
            print('Word is found in board!\n')
            print('Checking if word is found in dictionary...')

            if bh.binary_search(word_to_check.lower(), dictionary):
                print(f'{word_to_check} is a valid word!')
            else:
                print(f'{word_to_check} is not a valid word!')

        else:
            print('Word not found in board.\nPlease try with another word.')


play_game()
