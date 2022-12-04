#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print_matrix_integer function

    Args:
        matrix: input matrix.
    """
    if len(matrix) == 0:
        print("", end="")
        return
    for row in matrix:
        for col in row:
            print("{:d} ".format(col), end="")
        print()
