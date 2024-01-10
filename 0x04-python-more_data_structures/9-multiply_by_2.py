#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """multiply by 2 function

    Args:
        a_dictionary: input dictionary

    Return: new dictionary
    """
    new_dict = {}
    for key, item in a_dictionary.items():
        new_dict[key] = item * 2
    return new_dict
