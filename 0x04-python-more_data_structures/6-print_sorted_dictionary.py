#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """print_sorted_dictionary function

    Args:
        a_dictionary: input dictionary.

    Returns:
        none but prints prints a dictionary by ordered keys.
    """
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
