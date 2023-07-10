#!/usr/bin/python3
'''
A class that displays a list
'''


class MyList(list):
    """A class that prints a sorted list

    Args:
        list: builtin method for lists
    """
    def print_sorted(self):
        """Prints a sorted list
        """
        print(sorted(self))
