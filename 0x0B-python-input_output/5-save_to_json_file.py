#!/usr/bin/python3
import json
"""
Write a function that writes an Object to a text file, \
    using a JSON representation:
"""


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as object_file:
        object_file.write(json.dumps(my_obj))
