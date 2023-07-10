#!/usr/bin/python3
"""
Task to check for the kind of class
"""


def is_kind_of_class(obj, a_class):
    """
    checks if an object is a kind of a class

    Args:
        obj (object): object to be checked
        a_class (class): class for the object to be checked against

    Returns:
        bool: True or False
    """
    return isinstance(obj, a_class)
