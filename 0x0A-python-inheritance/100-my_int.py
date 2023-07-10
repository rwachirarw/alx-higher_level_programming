#!/usr/bin/pyhton3
"""
MyInt class
"""

class MyInt(int):
    """
    Return inverted definations for __eq__ and __ne__

    Args:
        int (_type_): integer to be inverted
    """
    def __eq__(self, other):
        """
        defines equality

        Args:
            other (int): other int to be compared with

        Returns:
            int: equality
        """
        return super().__ne__(other)
    
    def __ne__(self, other):
        """
        defines not equal

        Args:
            other (int): integer to be compared with

        Returns:
            int: not equal
        """
        return super().__eq__(other)
