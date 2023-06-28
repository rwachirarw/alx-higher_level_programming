#!/usr/bin/python3

""" Defination of Class square """


class Square:
    """defines the class square """

    def __init__(self, size=0):
        """ initialize the object instance of the class
        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """gets the size of the square """
        return self.__size

    @size.setter
    """ sets the size of the square """
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2

    def __eq__(self, other):
        """ compares the =="""
        return self.area() == other.area()

    def __ne__(self, other):
        """ compares th !="""
        return self.area() != other.area()

    def __lt__(self, other):
        """ compares the < """
        return self.area() < other.area()

    def __le__(self, other):
        """compares the <="""
        return self.area() <= other.area()

    def __gt__(self, other):
        """ compares the > """
        return self.area() > other.area()

    def __ge__(self, other):
        """ compares the >= """
        return self.area() >= other.area()
