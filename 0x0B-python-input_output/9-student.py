#!/usr/bin/python3
"""
Write a class Student that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
"""


class Student:
    """
    A student class
    """
    def __init__(self, first_name, last_name, age):
        """
        initialization of instance

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns:
            dict: dictionary object
        """
        return self.__dict__
