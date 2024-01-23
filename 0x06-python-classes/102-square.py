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

    @property
    def size(self):
        """retrieves value of size"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets the value of size to agiven new value.

        Raise:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate area of square.

        Return: area of square.
        """
        return __size * __size

    def __lt__(self, other):
        """return ef self.size < other.size"""
        return self.size < other.size

    def __le__(self, other):
        """returns self.size <= other.size"""
        return self.size <= other.size

    def __eq__(self, other):
        """checks if self.size == other.size
        """
        return self.size == other.size

    def __ne__(self, other):
        """checks if self.size != other.size"""
        return self.size != other.size

    def __gt__(self, other):
        """checks if self.size > other.size"""
        return self.size > other.size

    def __ge__(self, other):
        """checks if self.size >= other.size"""
        return self.size >= other.size
