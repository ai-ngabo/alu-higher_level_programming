#!/usr/bin/python3
"""This is  a file reader module to a filenem (utf-8) and print it to stdout"""


def read_file(filename=""):
    """This function hold a variable name file name means a file to be read"""
    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end='')
