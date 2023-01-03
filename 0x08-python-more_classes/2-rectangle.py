#!/usr/bin/python3
"""
This is a Rectangle module.

it gives access to a rectangle class with
(width x height) dimensions.
    where width and height are integers greater than or
    0

methods:
    area(): returns the area of the rectangle.
        no args.
    perimeter():returns the perimeter of the rectangle or 0 if
        width or height ins 0. no args.
"""


class Rectangle:
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
        """retrieves the value of width"""
        self.width = width

    @width.setter
    def width(self, value):
        """width setter."""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = value

    @property
    def height(self):
        """retrieves value of value of height"""
        return self.height

    @height.setter
    def height(self, value):
        """height setter."""
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = height

    def area(self):
        """returns the area ot rectangle"""
        return self.height * self.width

    def perimeter(self):
        """returns perimeter of the rectangle or 0
        if height or width is 0.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (height + width)
