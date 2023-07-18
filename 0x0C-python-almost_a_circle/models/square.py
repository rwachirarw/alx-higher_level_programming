#!/usr/bin/python3
'''Square'''

from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size, x=0, y=0, id=None):
        """_summary_

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute

        Returns:
            int: size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute

        Args:
            value (int): size to be assigned to the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square instance

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return the string representation of the Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """Return the dictionary representation of the square

        Returns:
            dict: Dictionary representation of the square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
