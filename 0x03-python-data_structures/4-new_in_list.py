#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """New_in_list function

    Args:
        my_list: input list.
        idx: index of the element to be changed.
        element: new element.

    Returns:
       new modified list,
       original unmodified list if idx is negative or
       out of range.
    """
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list

    new_list = []
    for item in my_list:
        new_list.append(item)
    new_list[idx] = element

    return new_list
