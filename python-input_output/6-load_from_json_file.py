#!/usr/bin/python3
"""Creating an object from a JSON file"""
import json


def load_from_json_file(filename):
    """ The function to create ana object"""
    with open(filename, encoding='utf-8') as myFile:
        return json.load(myFile)
