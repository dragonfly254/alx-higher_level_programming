#!/usr/bin/python3
"""
This module gives access to Square class and its
functions.                                                        
"""


class Square:
    """Represents a square

    Attributes:
        __size(int): Size of the square.
    """
    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Returns size of the square"""
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
        """The function computes the area of the square.

        Return:
            current square area
        """
        return self.__size ** 2
