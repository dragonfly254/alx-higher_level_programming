#!/usr/bin/python3
"""
This module provides access to Square class.
"""


class Square:
    """
    creates a square of size 'size'
    """
    def __init__(self, size):
        """
        class initializer.

        args:
            size: the size of sides of the square
        """
        self.__size = size
