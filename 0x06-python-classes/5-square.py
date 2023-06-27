#!/usr/bin/python3
""" A class that defines a square by: """


class Square:
    """ Defination of a class Square """

    def __init__(self, size=0):
        """ initialise the instance of the class size to zero
        if no size attribute has been passed.

        Args:
            size: size of the square initialise to zero
        """
        self.__size = size

    @property
    def size(self):
        """ gets the value of size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size with the value. Also checks for Type and Value errors
        before setting
        Args:
            value: to be used to set the square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ public instance method that returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character # """
        if (self.__size == 0):
            print()
        else:
            for l in range(self.__size):
                for w in range(self.__size):
                    print("#", end="")
            print()
