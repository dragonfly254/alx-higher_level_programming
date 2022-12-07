#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """square_matrix_simple function

    Args:
        matrix: input matrix to be squared.

    Returns:
        new matrix of same size with each value
        squared.
    """

    new_matrix = [list(map(lambda x: x**2, (x for x in row))) for row in (matrix)]
    return new_matrix
