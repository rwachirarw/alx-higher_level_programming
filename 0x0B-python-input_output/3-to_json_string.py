#!/usr/bin/python3
"""
Write a function that returns the JSON representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """
    A method that converts an object to a json string

    Args:
        my_obj (object): object to be converted to json

    Returns:
        str: json representation
    """
    return json.dumps(my_obj)
