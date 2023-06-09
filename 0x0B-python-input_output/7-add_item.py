#!/usr/bin/python3
"""
Write a script that adds all arguments to a Python \
    list, and then save them to a file:
"""
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item(args, filename):
    """
    Adds an item to the file

    Args:
        args (_type_): _description_
        filename (_type_): _description_
    """
    if (os.path.exists(filename)):
        content = load_from_json_file(filename)
    else:
        content = []
    content.extend(args)
    save_to_json_file(content, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
