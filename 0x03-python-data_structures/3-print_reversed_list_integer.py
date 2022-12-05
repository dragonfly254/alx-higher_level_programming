#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print reversed list integer function

    Args:
        my_list: input list.

    """
    for num in my_list[::-1]:
        print("{:d}".format(num))
