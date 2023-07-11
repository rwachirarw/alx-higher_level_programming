#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file, after each line\
      containing a specific string (see example):

    Prototype: def append_after(filename="", search_string="", new_string=""):
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
    You are not allowed to import any module
"""


def append_after(filename="", search_string="", new_string=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        search_string (str, optional): _description_. Defaults to "".
        new_string (str, optional): _description_. Defaults to "".
    """
    my_str = ""
    with open(filename, encoding="utf8") as object_file:
        for line in object_file:
            my_str += line
            if search_string in line:
                my_str += new_string

    with open(filename, mode="w") as object_file:
        object_file.write(my_str)
