#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace in list function.

    Args:
        my_list: input list.
        idx: index of element to be changed.
        element: new value.

    Returns:
        new modified list,
        original list if idx is negative or idx is out of range.
    """

    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element

    return my_list
