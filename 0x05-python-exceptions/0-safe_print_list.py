#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    def safe_print_list(my_list=[], x=0):
    n_elem = 0
    try:
        while x > 0:
            print(my_list[n_elem], end="")
            n_elem += 1
            x -= 1
    except IndexError:
        pass
    print()
    return n_elem
