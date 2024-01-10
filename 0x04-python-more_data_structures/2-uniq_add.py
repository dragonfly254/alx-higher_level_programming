#!/usr/bin/python3


def uniq_add(my_list=[]):
    """A unique add function

    Args:
        my_list: input list.

    Return: unique sum.
    """
    set_t = set(my_list)
    sm = sum(set_t)

    return sm
