#!/usr/bin/python3


""" Magic class """


import math


class MagicClass:
    def __init__(self, radius=0):
        """ initialize instance radius to zero and checks that the radius
        must be a number
        Args:
            radius: radius
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """ method of an instance that returns the area """
        return 2 * math.pi * self.__radius ** 2

    def circumference(self):
        """ method of an instance that returns the circumference """
        return 2 * math.pi * self.__radius
