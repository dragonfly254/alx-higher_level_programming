#!/usr/bin/python3
def no_c(my_string):
    """no_c function

    Args:
        my_string: input string.

    Returns:
        new string without 'c' or 'C'.
    """
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char

    return new_string
