#!/usr/bin/python3
"""appending new file with utf-8"""
def append_write(filename="", text=""):
    """
    The function will append the new text to existing one!
    """

    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.append(text)
