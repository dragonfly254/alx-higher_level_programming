#!/usr/bin/python3
def roman_to_int(roman_string):
    t_str = isinstance(roman_string, str)
    if not(t_str) or roman_string is None:
        return 0

    value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    res = 0
    i = 0
    len_s = len(roman_string)

    while (i < len_s):
        s1 = value.get(roman_string[i], -1)

        if (i + 1 < len_s):
            s2 = value.get(roman_string[i + 1], -1)
            if s1 >= s2:
                res += s1
                i += 1
            else:
                res += (s2 - s1)
                i += 2
        else:
            res += s1
            i += 1

    return res
