#!/usr/bin/python3
"""
This is a base geometry module.
"""


class BaseGeometry:
    """ base geometry class """

    def area(self):
        """unimplimented area method

        Raises:
            not implemented Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator func - validates the value.

        Args:
            name: variable name
            value: value of the variable

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0

        Returns: none.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
