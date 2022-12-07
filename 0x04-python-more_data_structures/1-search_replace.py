#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """search_replace function

    Args:
        my_list: input list.
        search: element to replace in the list.
        replace: new element.

    Returns:
        new modified list.
    """
    new_list = list(map(lambda x: replace if (x == search) else x, my_list))

    return new_list
