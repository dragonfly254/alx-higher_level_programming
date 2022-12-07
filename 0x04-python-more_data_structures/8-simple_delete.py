#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = {}
    for dkey, item in a_dictionary.items():
        new_dict[dkey] = item

    if key in new_dict.keys():
        del new_dict[key]

    return new_dict
