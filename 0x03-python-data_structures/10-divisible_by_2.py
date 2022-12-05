#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """divisible_by_2 function

    Args:
        my_list: input list.

    Returns:
        new list with true or false at ith index depending
        if ith element is divisible by two.
    """
    new_list = []

    for item in my_list:
        if item % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
