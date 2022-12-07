#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """update_dictionary fuction

    Args:
        a_dictionary: input dictionary.
        key: key to replace or add key/value in a dictionary.
        value: new value.

    """
    if key in a_dictionary.keys():
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
