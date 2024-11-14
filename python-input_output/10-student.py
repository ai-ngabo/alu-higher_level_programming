#!/usr/bin/python3
"""Writing class Student that defines student"""


class Student:
    """Representation of Student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of student instance"""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {y: getattr(self, y) for y in attrs if hasattr(self, y)}
        return self.__dict__
