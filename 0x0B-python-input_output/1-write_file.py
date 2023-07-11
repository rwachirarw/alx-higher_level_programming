#!/bin/usr/python3
"""
A method to write to a file
"""


def write_file(filename="", text=""):
    """
    This is a method that writes to a file

    Args:
        filename (str, optional): The file name. Defaults to "".
        text (str, optional): Text to be witten. Defaults to "".

    Returns:
        int: number of characters written
    """
    with open(filename, "w") as file_object:
        return file_object.write(text)
