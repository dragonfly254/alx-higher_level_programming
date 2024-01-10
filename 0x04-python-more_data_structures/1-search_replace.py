#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """A simple search and replace function,
    it searches a given element in a list and replaces it
    with a given new value.

    Args:
        my_list: input list
        search: element to search in the list
        replace: new element

    Return:
        new list.
    """
    new_list = my_list.copy()

    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace

    return new_list
