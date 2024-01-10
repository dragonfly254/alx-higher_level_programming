#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is None:
        return 0

    accum_weight_score = 0
    accum_weight = 0

    for score, weight in my_list:
        accum_weight_score += (score * weight)
        accum_weight += weight

    return accum_weight_score / accum_weight
