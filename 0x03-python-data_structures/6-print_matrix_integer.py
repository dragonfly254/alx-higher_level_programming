#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print_matrix_integer function

    Args:
        matrix: input matrix.
    """
    for row in matrix:
            print(" ".join("{:d}".format(col) for col in row))
