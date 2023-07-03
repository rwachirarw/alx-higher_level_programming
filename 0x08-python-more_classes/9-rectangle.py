#!/usr/bin/python3
'''Defines a Rectangle'''


class Rectangle:
    '''Defines a Rectangle'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        ''' Initialises instance of a class'''
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
        '''Returns the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        '''Defines the string function'''
        strn = ""
        if self.__width == 0 or self.__height == 0:
            return strn
        for h in range(self.__height):
            for w in range(self.__width):
                strn += str(self.print_symbol)
            if h < self.__height - 1:
                strn += "\n"
        return strn

    def __repr__(self):
        '''Defines a representation of a printable version of an object'''
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        '''Defines the delete method'''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        '''A static method that returns the biggest rectangle
        based on the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''A class method that returns a new Rectangle instance'''
        return cls(size, size)
