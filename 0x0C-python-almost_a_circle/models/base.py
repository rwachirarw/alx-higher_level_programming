#!/usr/bin/python3
"""
Base class
"""
import json
import csv
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the instance of the class

        Args:
            id (_type_, optional): id of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): List of dictionaries

        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file

        Args:
            list_objs (list): List of instances

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        json_str = cls.to_json_string([obj.to_dictionary()
                                      for obj in list_objs]
                                      if list_objs is not None else [])
        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by the JSON string

        Args:
            json_string (str): JSON string representation of a list

        Returns:
            list: List represented by the JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create and return an instance with all attributes set
        Args:
            **dictionary: Double pointer to a
            dictionary representing attributes

        Returns:
            object: Instance with all attributes set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file and return a list of instances

        Returns:
            list: List of instances loaded from the JSON file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_str)
        instances = [cls.create(**dictionary) for dictionary in list_dicts]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs in CSV format and saves it to a file.

        Args:
            - list_objs: list of instances
        """

        if (
            type(list_objs) != list
            or (list_objs is not None and not
                all(isinstance(x, cls) for x in list_objs))
        ):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            if list_objs is not None:
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer.writerow(fields)
                for obj in list_objs:
                    row = [getattr(obj, field) for field in fields]
                    writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file.

        Returns: list of instances
        """

        filename = cls.__name__ + ".csv"
        instances = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                fields = next(reader)
                for row in reader:
                    instance = cls.create(**dict(zip(fields, row)))
                    instances.append(instance)
        return instances

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.

        Args:
            - list_rectangles: list of Rectangle instances
            - list_squares: list of Square instances
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
