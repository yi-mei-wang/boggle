def binary_search(target, my_list):
    """ Searches for a target in a sorted list recursively.

    Uses the binary search algorithm. Target is compared to the midpoint. If the former is not found, compare it to the latter. Depending on whether the target is smaller or larger than the midpoint, the irrelevant portion of the list is discarded.

    Args:
    -----
        target : A string or an int to be searched for
        my_list :  A sorted list to be searched from
    
    Returns:
    --------
        A boolean indicating whether the target is found.
    """
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


def load_dictionary(pathname):
    """Loads a dictionary in the form of a .txt file.

    Opens a .txt file. Strips the ending newline character from each line in the file before appending each line into a list.

    Args:
    -----
        pathname : A string representing the path to a .txt file. The file should contain a new word on each line. 

    Returns:
    --------
        A list whose elements are the words from the .txt file with their newline character stripped.
    """
    return [line.rstrip('\n') for line in open(pathname)]
