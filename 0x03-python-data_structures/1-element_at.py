#!/usr/bin/python3
def element_at(my_list, idx):
    """Element at function

    Args:
        my_list: input list
        idx: index of element to retrieve

    Returns:
        value of element in index idx,
        None if idx is negative or
        out of range.
    """

    if idx < 0 and idx > len(my_list)-1:
        return None
    return my_list[idx]
