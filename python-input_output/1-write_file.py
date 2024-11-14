#!/usr/bin/python3
"""file overwritting or creating if not exists!"""


def write_file(filename="", text=""):
    """opening file with utf-8 and overwrite"""
    with open(filename, 'w', enconding='utf-8') as myFile:
        return myFile.write(text)
