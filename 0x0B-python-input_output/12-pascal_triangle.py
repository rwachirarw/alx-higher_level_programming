#!/usr/bin/python3
"""
Technical interview preparation:

    You are not allowed to google anything
    Whiteboard first

Create a function def pascal_triangle(n): \
    that returns a list of lists of integers \
        representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
    You are not allowed to import any module

"""


def pascal_triangle(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n <= 0:
        return []

    pascal_list = []
    for line in range(n):
        row = []
        C = 1
        for i in range(line + 1):
            row.append(C)
            C = C * (line - i) // (i + 1)
        pascal_list.append(row)

    return pascal_list
