#!/usr/bin/python3
'''Defines a Rectangle'''


class Rectangle:
    '''Defines a Rectangle'''
    def __init__(self, width=0, height=0):
        ''' Initialises instance of a class'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Gets the width of a rectangle'''
        return self.__width

    @width.setter
    def width(self, width):
        '''Sets the width of a rectangle'''
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        '''Gets the width of a rectangle'''
        return self.__height

    @height.setter
    def height(self, height):
        '''Sets the width of a rectangle'''
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
