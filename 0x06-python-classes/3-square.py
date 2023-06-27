#!/usr/bin/python3
""" A class that defines a square by: """


class Square:
    """ Defination of a class Square """

    def __init__(self, size=0):
        """ initialise the instance of the class size to zero
        if no size attribute has been passed. we check for TypeError
        and ValueError before initializing

        Args:
            size: size of the square initialise to zero
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ public instance method that returns the current square area"""
        return self.__size * self.__size
