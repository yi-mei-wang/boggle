import random
import boggle_helpers as bh
import boggle_search as bs


def setup(n):



def play_game():
    board = setup(4)

    filename = '/Users/mei/work/teaching/python-sep-19/day-3/recursion/boggle/dictionary.txt'
    dictionary = [line.rstrip('\n') for line in open(filename)]

    while True:
        bh.print_board(board)

        word_to_check = input('Enter the word to be checked: ').upper()

        anchors = bs.check_first_letter(word_to_check, board)

        if bs.find_word(word_to_check[1:], anchors, board, []):
            print('Word is found in board!\n')
            print('Checking if word is found in dictionary...')

            if bh.binary_search(word_to_check.lower(), dictionary):
                print(f'{word_to_check} is a valid word!')
            else:
                print(f'{word_to_check} is not a valid word!')

        else:
            print('Word not found in board.\nPlease try with another word.')


play_game()
