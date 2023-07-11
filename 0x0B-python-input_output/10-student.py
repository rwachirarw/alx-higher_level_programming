#!/usr/bin/python3
"""
Write a class Student that defines a student by: (based on 9-student.py)

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

    def to_json(self, attrs=None):
        """_summary_

        Args:
            attrs (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for attr in attrs:
            if attr in self.__dict__.keys():
                my_dict[attr] = self.__dict__[attr]
        return my_dict
