#!/usr/bin/python3
def best_score(a_dictionary):
    lscore = 0
    hscorer = None

    for key, item in a_dictionary.items():
        if lscore < item:
            lscore = item
            hscorer = key
    return hscorer
