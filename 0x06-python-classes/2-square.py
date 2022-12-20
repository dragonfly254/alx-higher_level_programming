#!/usr/bin/python3
"""This module gives access to Square class"""


class Square:
    """
    defines a square with sides = size.
    """
    def __init__(self, size):
        """
        class initializer.

        args:
            size: size of the sides of the square.
        """
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
