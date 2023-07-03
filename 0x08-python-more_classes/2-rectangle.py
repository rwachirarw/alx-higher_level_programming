#!/usr/bin/python3
'''Defines a Rectangle'''


class Rectangle:
    '''Defines a Rectangle'''
    def __init__(self, width=0, height=0):
        ''' Initialises instance of a class'''
        self.height = height
        self.width = width

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

    def area(self):
        '''Returns the area of the rectangle'''
        return self.__width * self.__height
    
    def perimeter(self):
        '''Returns the preimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
