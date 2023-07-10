#!/usr/bin/python3
"""
Method that checks for an object
"""


def is_same_class(obj, a_class):
    """_summary_checks for the class of an object

    Args:
        obj (object): object to be checked
        a_class (class): class to check

    Returns:
        bool: True or False
    """
    return isinstance(obj, a_class) and type(obj) == a_class
