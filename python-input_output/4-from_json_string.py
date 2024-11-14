#!/usr/bin/python3
"""Turning JSON string into JSON object--- diserialization"""
import json


def from_json_string(my_str):
    """
    function to return diserialized string into object
    """
    data1 = json.loads(my_str)
    return data1
