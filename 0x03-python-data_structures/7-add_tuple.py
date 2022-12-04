#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """add_tuple function

    Args:
        tuple_a: the first input tuple.
        tuple_b: second input tuple.

    Returns: there sum.
    """
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a >= 2:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if len_b >= 2:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    if len_a < 2:
        if len_a == 1:
            a1 = tuple_a[0]
            a2 = 0
        else:
            a1 = 0
            a2 = 0

    if len_b < 2:
        if len_b == 1:
            b1 = tuple_b[0]
            b2 = 0
        else:
            b1 = 0
            b2 = 0
    return (a1 + b1, a2 + b2)
