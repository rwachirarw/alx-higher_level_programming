#!/usr/bin/python3
"""prevents the user from dynamically \
   creating new instance attributes, \
   except if the new instance attribute is called first_name

Raises:
    AttributeError: 'LockedClass' object has \
                             no attribute '
"""


class LockedClass:
    __slots__ = ['first_name']
    '''Class definition'''

    def __init__(self):
        '''Initializes instance of a class'''
        self.first_name = None

    def __setattr__(self, name, value):
        '''Sets atrributes for the instance'''
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has \
                                 no attribute '" + name + "'")
        super().__setattr__(name, value)
