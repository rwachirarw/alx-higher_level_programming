#!/usr/bin/python3
""" A class that defines a square """


class Square:
    """ Defination of a class Square """

    def __init__(self, size=0, position=(0, 0)):
        """ initialise the instance of the class size to zero
        if no size attribute has been passed.

        Initialises position to a set of (0, 0)

        Args:
            size: size of the square initialise to zero
            position: position of thr square
        Returns:
            None
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """ gets the value of size
        Return:
            size
        """
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
        """ public instance method that returns the current square area
        Return:
            square
        """
        return self.__size * self.__size

    def my_print(self):
        """prints the square with #
        Returns:
            None
        """
        if self.__size == 0:
            print("")
        else:

            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """ prints a string """

        if self.__size == 0:
            return "\n"

        return "\n" * self.__position[1] + \
            "\n".join([" " * self.__position[0] + "#" * self.__size
                      for _ in range(self.__size)])

    @property
    def position(self):
        """gets position
        Return:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position
        Args:
            value: position of the square
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
