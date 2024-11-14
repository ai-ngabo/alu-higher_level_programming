#!/usr/bin/python3
"""returning json string"""
import json


def to_json_string(my_obj):
    """
    function to return a json  with object: string
    """
    data = json.dumps(my_obj)
    return data
