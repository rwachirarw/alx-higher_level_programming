#!/usr/bin/python3
"""
Task to check for instances and subclasses
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that \
        inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of a \
            class that inherited from the specified class; False otherwise.
    """
    return (isinstance(obj, a_class) and issubclass(type(obj), a_class)
            and type(obj) != a_class)
