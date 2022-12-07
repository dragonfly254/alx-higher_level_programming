#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """update_dictionary fuction

    Args:
        a_dictionary: input dictionary.
        key: key to replace or add key/value in a dictionary.
        value: new value.

    """
    new_dict = {}
    for dkey, item in a_dictionary.items():
        new_dict[dkey] = item

    new_dict[key] = value

    return new_dict
