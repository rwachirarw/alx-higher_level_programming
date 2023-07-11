#!/usr/bin/python3
"""
Write a function that writes an Object to a text file, \
    using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a method that saves to json file

    Args:
        my_obj (obj): python object
        filename (str): File to open
    """
    with open(filename, "w", encoding="utf-8") as object_file:
        object_file.write(json.dumps(my_obj))
