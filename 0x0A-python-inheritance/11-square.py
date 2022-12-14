#!/usr/bin/python3
"""
This is the  square module.

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The square class."""

    def __init__(self, size):
        """initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """returns a string with the area """
        return super().area()

    def __str__(self):
        """returns a printable string """
        return "[Square] {}/{}".format(self.__size, self.__size)
