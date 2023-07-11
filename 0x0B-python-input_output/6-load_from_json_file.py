#!/usr/bin/python3
"""
Write a function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """
    A method that loads from a json file

    Args:
        filename (string): contains JSON strings

    Returns:
        obj: python object
    """
    with open(filename, encoding="utf-8") as object_file:
        return json.load(object_file)
