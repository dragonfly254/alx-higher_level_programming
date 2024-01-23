#!/usr/bin/python3
""" This is a square module"""


class Square:
    """creates empty square class"""

    def __init__(self, size=0, position=(0, 0)):
        """
        initialiser

        Args:
            size: length of the side of square
            position: position of the square in x-y coordinates.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Returns value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the value of the position
        Args:
            value: a tuple containing new value
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in value:
                if not isinstance(i, int):
                    raise TypeError("position must be a tuple\
                            of 2 positive integers")
            self.__position = value

    def area(self):
        """calculate area of square.

        Return: area of square.
        """
        return self.__size ** 2

    def my_print(self):
        """prints the square using "#" """
        if self.size == 0:
            print()
        else:
            y_axis = self.position[1]
            for i in range(y_axis):
                print()
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
