#!/usr/bin/python3
"""
Base class
"""
import json
import csv


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
        """Serialize instances to a CSV file

        Args:
            list_objs (list): List of instances

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        fieldnames = cls.get_csv_fieldnames()

        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file

        Returns:
            list: List of instances deserialized from the CSV file
        """
        filename = cls.__name__ + ".csv"
        instances = []

        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                instance = cls.create(**cls.from_csv_row(row))
                instances.append(instance)

        return instances

    def to_dictionary(self):
        """Return the dictionary representation of the instance

        Returns:
            dict: Dictionary representation of the instance
        """
        raise NotImplementedError

    def to_csv_row(self):
        """Return the CSV row representation of the instance

        Returns:
            dict: Dictionary representing a row in the CSV file
        """
        raise NotImplementedError

    @classmethod
    def get_csv_fieldnames(cls):
        """Return the fieldnames for the CSV file

        Returns:
            list: List of fieldnames
        """
        raise NotImplementedError

    @classmethod
    def from_csv_row(cls, csv_row):
        """Create and return a dictionary from a CSV row

        Args:
            csv_row (dict): Dictionary representing a row in the CSV file

        Returns:
            dict: Dictionary containing attribute values
        """
        raise NotImplementedError
