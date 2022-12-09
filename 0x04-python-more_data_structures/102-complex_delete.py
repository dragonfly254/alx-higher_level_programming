#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dic = a_dictionary
    key_list = []
    for key, val in dic.items():
        if val == value:
            key_list.append(key)

    for k in key_list:
        dic.pop(k)

    return dic
