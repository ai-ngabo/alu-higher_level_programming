#!/usr/bin/python3
"""Writting a class to define a student"""


class Student:
    """Represent Student"""
    def __init__(self, first_name, last_name, age):
        """Initialises the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation of student instance"""
        return self.__dict__
