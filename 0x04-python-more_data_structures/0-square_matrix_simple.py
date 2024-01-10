#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    computes the square value of all integers of a matrix.

    Args:
        matrix: a 2 dimensional array

    Return:
        new matrix asme size of the original but squared element

    """
    return [list(map(lambda x: x**2, (x for x in r))) for r in matrix]
