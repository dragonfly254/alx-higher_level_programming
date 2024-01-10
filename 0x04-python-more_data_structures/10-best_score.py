#!/usr/bin/python3


def best_score(a_dictionary):
    """best score function

    Args:
        a_dictionary: input dictionary

    Return: key with largest integer
    """
    if a_dictionary is None:
        return None

    large_value = 0
    large_key = None

    for key, value in a_dictionary.items():
        if value > large_value:
            large_value = value
            large_key = key

    return large_key
