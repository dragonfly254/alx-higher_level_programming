#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """only_diff_elements function

    Args:
        set_1: first set.
        set_2: second set.

    Returns:
        set difference.
    """
    return (set_2 - set_1) | (set_1 - set_2)
