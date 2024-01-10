#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """simple_delete function

    Args:
        a_dictionary: input dictionary
        key: key delete

    return: new dict with removed key
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
