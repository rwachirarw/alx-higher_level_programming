#!/usr/bin/python3
"""
Task to declare a BaseGeometry class
"""


class BaseGeometry:
    """
    A BaseGeometry class
    """
    def area(self):
        """Calculates the area

        Raises:
            Exception: raise an exception with\
                  the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer

        Args:
            name (str): the name of the value
            value: value to validate

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
