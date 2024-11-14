"""
file reader module
This module provides a function to read a text file and print out its content
"""
#!/usr/bin/python3
def read_file(filename=""):
    """
    This function hold a variable name file name means a file to be read
    """
    with open(filename, 'r', encoding='utf-8') as myFile:
        line = myFile.read()
        print(line)
