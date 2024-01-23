#!/usr/bin/python3
"""MagicClass module

This module gives access to the MagicClass that does exactly the
same as the given Python bytecode.

it has the following functions:
    *area - returns area of the circle
    *circumference - which returns circumference of the circle
"""
import math


class MagicClass:
    """ Class that stores and manipulate the info of a circle
    get the area and circunference"""
    def __init__(self, radius=0):
        """initializes the circle.

        Args:
            radius: radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ get the area depending of the radius of the circle
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """ get the circunference depending of the radius of the
        circle
        """
        return (2 * math.pi * self.__radius)
