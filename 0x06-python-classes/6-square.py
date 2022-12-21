#!/usr/bin/python3
"""This module gives access to Square class and its
   functions.
"""


class Square:
    """Represents a square

    Attributes:
        __size(int): Size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        flag = 0
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in position:
                if not isinstance(i, int) or i < 0:
                    flag = 1
                    raise TypeError("position must be a tuple of 2 positive integers")
            if flag == 0:
                self.__position = position


        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        flag = 0
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in value:
                if not isinstance(i, int):
                    flag = 1
                    raise TypeError("position must be a tuple\
                            of 2 positive integers")
            if flag == 0:
                self.__position = value

    def area(self):
        """The function computes the area of the square.

        Return:
            current square area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using #"""
        if self.__size == 0:
            print()
        else:
            jump = self.position[1]
            while (jump > 0):
                print()
                jump = jump - 1

            a, b = self.size, self.size
            for i in range(a):
                space = self.position[0]
                for j in range(b):
                    while(space > 0):
                        print("", end=" ")
                        space = space - 1
                    print("#", end="")
                print("")
