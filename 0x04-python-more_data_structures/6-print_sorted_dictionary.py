#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """a print_sorted_dictionary function

    Args:
       a_dictionary: input dictionary


    return: none
    """
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
