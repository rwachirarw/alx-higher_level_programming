#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file \
    (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    A method that appends text to a file

    Args:
        filename (str, optional): Filename. Defaults to "".
        text (str, optional): text to be appended. Defaults to "".
    """
    with open(filename, "a") as file_object:
        return file_object.write(text)
