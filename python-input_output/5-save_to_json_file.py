#!/usr/bin/python3
"""writting an object to a text file using JSON"""


def save_to_json_file(my_obj, filename):
    """
    Function to return text file from object
    """
    with open(filename, 'w') as my myFile:
        json.dump(my_obj, myFile)
