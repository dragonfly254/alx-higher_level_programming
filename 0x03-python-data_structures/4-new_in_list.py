#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    l = len(my_list) - 1
    ls_copy = my_list.copy()

    if idx < 0 or idx > l:
        return ls_copy
    ls_copy[idx] = element
    return ls_copy
