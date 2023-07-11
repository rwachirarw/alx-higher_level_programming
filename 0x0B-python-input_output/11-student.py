#!/usr/bin/python3
"""
Write a class Student that defines a student by: (based on 10-student.py)

    Public instance attributes:
        first_name
        last_name
        age
"""


class Student:
    """
    Defines a student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """_summary_

        Args:
            attrs (_type_, optional): _description_. Defaults to None.

        Returns:
            __dict__: dictionary of a class
        """
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for attr in attrs:
            if attr in self.__dict__.keys():
                my_dict[attr] = self.__dict__[attr]
        return my_dict

    def reload_from_json(self, json):
        """_summary_

        Args:
            json (_type_): _description_

        Returns:
            _type_: _description_
        """
        current_dict = self.__dict__
        for attr in json.keys():
            for current_attr in current_dict.keys():
                if attr == current_attr:
                    current_dict[current_attr] = json[attr]
        return current_dict
