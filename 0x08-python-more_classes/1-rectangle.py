#!/usr/bin/python3
"""
This is a Rectangle module.

it gives access to a rectangle class with
(width x height) dimensions.
    where width and height are integers greater than or
    to 0

"""


class Rectangle:
    """rectangular class"""
    def __init__(self, width=0, height=0):
        """initializes instances of the class.

        Attributes:
            width: width of the rectangle.
            height: the height of the rectangle.

        Raise:
            TypeError if width or height is not integer.
            ValueError if width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns width of the the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """changes the value of width to 'value' provided."""
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """returns the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """changes the value of height"""
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
