#!/usr/bin/python3
def uppercase(str):
    for char_str in range(len(str)):
        char = ord(str[char_str])
        if 97 <= char <= 122:
            char -= 32
        print("{}".format(chr(char)), end='')
    print()
