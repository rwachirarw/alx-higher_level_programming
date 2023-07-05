#!/usr/bin/python3
"""prevents the user from dynamically \
   creating new instance attributes, \
   except if the new instance attribute is called first_name

Raises:
    AttributeError: 'LockedClass' object has \
                             no attribute '
"""


class LockedClass:
    '''Class definition'''
    __slots__ = ['first_name']

    def __init__(self):
        '''Initializes instance of a class'''
        self.first_name = None
