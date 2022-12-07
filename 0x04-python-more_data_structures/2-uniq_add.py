#!/usr/bin/python3
def uniq_add(my_list=[]):
    """uniq_add function

    Args:
        my_list: input list.

    Returns:
        unique sum of list.
    """
    return sum(set(my_list))
