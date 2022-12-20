#!/usr/bin/python3
"""this module give access to Square class"""


class Square:
    """creates a square"""
    def __init__(self, size=0):
        """initialize the square"""
        self.size = size

    @property
    def size(self):
        """returns the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of the size"""
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """return the area of the square"""
        return (self.__size * self.__size)

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
