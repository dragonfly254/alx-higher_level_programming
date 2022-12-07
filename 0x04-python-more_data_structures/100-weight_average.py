#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0

    sum_t = 0
    freq = 0

    for x, y in my_list:
        sum_t += x * y
        freq += y
    return sum_t/freq
