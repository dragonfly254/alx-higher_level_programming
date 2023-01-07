#!/usr/bin/python3
"""
This is an add_integer module.
"""


def add_integer(a, b=98):
    """add integer function.

    Args:
        a (int or float): first number
        b (int or float): second number

    Raises:
        a must be an integer or b must be an integer
        if a or b is not an int or float.

    Returns:
        the addition of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
