#!/usr/bin/python3
def append_write(filename="", text=""):
    with open('2-main', 'a', encoding='utf-8') as myFile:
        myFile.append('This School is so cool!')
