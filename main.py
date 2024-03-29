import boggle_dictionary as bd
import boggle_helpers as bh
import boggle_search as bs


def setup(n, pathname):
    """ Sets up the necessary components of a Boggle game.

    Args:
    -----
        n : An int representing the desired dimension of a Boggle board
        pathname : A string representing the path to a .txt file

    Returns:
    -------- 
        A 2D list of n * n dimension representing a Boggle board and a list containing all the words in the dictionary.g

    """
    board = bh.fill_board(n)
    dictionary = bd.load_dictionary(pathname)

    return board, dictionary


def main():
    """ Starts a Boggle game.

    Continuously obtains an input from the user, checks if it exists in the board, and validates it against a dictionary.

    Args:
    -----
        None

    Returns:
    --------
        None
    """
    board, dictionary = setup(4, 'dictionary.txt')

    while True:
        bh.print_board(board)

        # Get an input from the user
        word_to_find = input(
            'Enter the word to be checked: ').upper().replace('QU', 'Q')

        # Check if word if more 3 chars long
        if len(word_to_find) < 3:
            print('Choose a word that is equal to or longer than 3 characters long.')

        else:
            # Search for all occurrences of the first char
            anchors = bs.find_first_char(word_to_find[0], board)

            # Try to find the rest of the word in the board
            if bs.find_word(word_to_find[1:], anchors, board, []):
                print('Word is found in board!\n')

                # Search for word in the dictionary
                print('Checking if word is found in dictionary...')

                word_to_validate = word_to_find.replace('Q', 'QU')

                if bd.binary_search(word_to_validate.lower(), dictionary):
                    print(f'{word_to_validate} is a valid word!')

                else:
                    print(f'{word_to_validate} is not a valid word!')

            else:

                print('Word not found in board.\n\nPlease try with another word.\n')


if __name__ == "__main__":
    main()
