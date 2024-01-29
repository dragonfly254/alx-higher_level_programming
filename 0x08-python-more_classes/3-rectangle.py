#!/usr/bin/python3
"""
This is a rectangle module.

It gives access to an Rectangle class
used in creating the instances of rectangle.

It can be imported all used in ts own
"""


class Rectangle:
    """rectangular class"""

    def __init__(self, width=0, height=0):
        """ rectangle initializer

        Args:
            width: width of the rectangle, which must be an integer
                and greater than 0 or throw TypeError and ValueError
                respectiful

            height: height of the rectangle, which also  must be an integer
                and greater than 0 or throw TypeError and ValueError
                respectiful
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ returns the value of width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width of the rectangle

        Args:
            value: new value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ return value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of the height of the rectangle

        Args:
            value: new value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """computes n=and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """computes and return the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """prints the rectangle using # character"""
        if self.width and self.height:
            res = ""
            for i in range(self.height):
                res += "#" * self.width + "\n"
            return res
        else:
            return ""
