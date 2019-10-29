def get_neighbour_coords(x, y, n):
    """Generates the coordinates of all neighbouring cells of the provided cell.

    Looks at the cells to the left, right, top, bottom and diagonal of a cell based on the x- and y-coordinates provided. 

    Args:
    -----
        x : An int representing the x-coordinate of a cell
        y : An int representing the y-coordinate of a cell
        n : An int representing the dimension of the board containing the cells

    Returns:
    --------
        A list of tuples representing the coordinates of the neighbouring cells of a given cell. Only cells within the confines of a n * n board are included.
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


def find_first_char(char, board):
    """Searches for the first letter of a given char in a board.

    Iterates through the board to obtain the coordinates of all the occurrences of the first char of a word.

    Args: 
    -----
        char : A string respresenting the char to search for
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
            if char == elem:
                anchors.append((x, y))

    print(f'\n{char} is found in {anchors}\n')

    return anchors


def get_possible_coords(char, x, y, board, history):
    """Finds the coordinates of a char, if present on the board, based on the coordinates of the anchor provided.

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
    pos_to_check = get_neighbour_coords(x, y, 4)

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

    # Go through every occurrence of the first char of word
    for (x, y) in anchors:
        print(f'Searching for {word[0]} from around ({x}, {y})')

        # Search for the remainder of the word
        possibilities = get_possible_coords(word[0], x, y, board, history)

        print(f'{word[0]} is found in {possibilities}\n')

        # If E is found in the neighbouring cells of B,
        if possibilities:
            history.append((x, y))

            # Look for ST in all the occurrences of E
            if find_word(word[1:], possibilities, board, history):
                return True

            history.remove((x, y))

    # If all the anchors have been searched and the word is still not found, trigger backtracking
    return False
