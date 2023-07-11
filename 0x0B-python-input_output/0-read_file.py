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
    with open(filename, "r") as my_file:
        print(my_file.read())
