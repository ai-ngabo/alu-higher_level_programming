#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    for i in range(0, x):
        try:
            print("{:d}".format(nb_print))
            nb_print += 1
        except (ValueError, TypeError):
            pass
    print()
    return nb_print
