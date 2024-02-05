#!/usr/bin/python3
"""
This is a module containing MyList class.
"""


class MyList(list):
    """inherits the attributes references of class list

    Args:
        list: class list
    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        copy_lst = self.copy()
        copy_lst.sort()
        print(copy_lst)
