#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    A method that reads a file

    Args:
        filename (str, optional): file name to be read. Defaults to "".
    """
    with open(filename, "r", encoding="utf=8") as file_object:
        print(file_object.read())
