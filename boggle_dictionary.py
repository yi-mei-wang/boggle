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


def load_dictionary(pathname):
    return [line.rstrip('\n') for line in open(pathname)]
