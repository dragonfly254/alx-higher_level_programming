#!/usr/bin/python3
""" This is a square module"""


class Square:
    """creates empty square class"""

    def __init__(self, size=0):
        """
        initialiser

        Args:
            size: length of the side of square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
