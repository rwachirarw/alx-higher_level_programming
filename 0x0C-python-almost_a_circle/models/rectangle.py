#!/usr/bin/python3
'''rectangle.py'''
from models.base import Base


class Rectangle(Base):
    """Rectangle class

    Args:
        Base (class): parent class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of a Rectangle instance

        Args:
            width (int): width
            height (height): height
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width

    @width.setter
    def width(self, width):
        """_summary_

        Args:
            width (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__height

    @height.setter
    def height(self, height):
        """_summary_

        Args:
            height (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__x

    @x.setter
    def x(self, x):
        """_summary_

        Args:
            x (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__y

    @y.setter
    def y(self, y):
        """_summary_

        Args:
            y (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.height * self.width

    def display(self):
        """_summary_
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return ('[Rectangle] ({}) {}/{} - {}/{}'
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Update the attributes of the Square instance

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle

        Returns:
            dict: Dictionary representation of the rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
