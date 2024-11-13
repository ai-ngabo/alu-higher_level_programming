#!/usr/bin/python3
def write_file(filename="", text=""):
    with open('1-write_file', 'w', enconding='utf-8') as myFile:
        myFile.write('This School is so cool!\n')
