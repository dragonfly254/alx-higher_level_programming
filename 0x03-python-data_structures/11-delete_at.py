#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """delete_at function

    Args:
        my_list: input list.
        idx: index of the item to be removed.

    Returns: orginal list with element at index idx
        removed, or original if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]

    return my_list
