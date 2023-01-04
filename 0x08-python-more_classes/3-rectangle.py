#!/usr/bin/python3
"""

This is a module for class Rectangle.

"""


class Rectangle:
    """ defines a rectangle """

    def __init__(self, width=0, height=0):
        """rectangle initializer

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width of rectangle.

        Returns:
            width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """modifies width value.

        Args:
            value: new value of width.

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height value

        Returns:
            rectangle height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """modifies the height value.

        Args:
            value: new height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """computes area of the rectangle.

        Returns:
            rectangle area

        """
        return self.width * self.height

    def perimeter(self):
        """calculates the Rectangle perimeter

        Returns:
            rectangle perimeter

        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """returns the Rectangle of #.

        Returns:
            str of the rectangle

        """
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle
        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]
