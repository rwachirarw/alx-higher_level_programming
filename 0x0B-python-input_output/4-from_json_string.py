#!/usr/bin/python3
"""
Write a function that returns an object (Python data structure) \
    represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """
    A method that converts a json string to a python object

    Args:
        my_str (str): json string

    Returns:
        obj: python representation of an object
    """
    return json.loads(my_str)
