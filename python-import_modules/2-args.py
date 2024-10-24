#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))
