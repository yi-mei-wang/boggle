import boggle_dictionary as bd
import boggle_helpers as bh
import boggle_search as bs


def setup(n):
    board = bh.fill_board(n)
    dictionary = bd.load_dictionary('dictionary.txt')

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
    board, dictionary = setup(4)

    while True:
        bh.print_board(board)

        word_to_find = input(
            'Enter the word to be checked: ').upper().replace('QU', 'Q')

        anchors = bs.check_first_letter(word_to_find, board)

        if bs.find_word(word_to_find[1:], anchors, board, []):
            print('Word is found in board!\n')
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
