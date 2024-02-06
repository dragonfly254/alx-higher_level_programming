#!/usr/bin/python3
"""
this is pascal triangle module.
"""


def pascal_triangle(n):
    """ Function that returns the pascal triangle
    Args:
        n: number of lines
    Returns:
       matrix: a matrix with the pascal triangle

    """

    matrix = []
    prev = []

    for i in range(n):
        res_list = []
        pt_1 = -1
        pt_2 = 0
        for j in range(len(prev) + 1):
            if pt_1 == -1 or pt_2 == len(prev):
                res_list += [1]t_
            else:
                res_list += [prev[pt_1] + prev[pt_2]]
            pt_1 += 1
            pt_2 += 1
        matrix.append(res_list)
        prev = res_list[:]

    return matrix
