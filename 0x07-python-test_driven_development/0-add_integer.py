#!/usr/bin/python3
'''Add an integer'''

def add_integer(a, b=98):
    '''
    This function that adds two integers.

    >>> add_integer(2, 3)
    5

    >>> add_integer(2.5, 3.5)
    5

    >>> add_integer('2', '3')
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    >>> add_integer(2, '3')
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
