#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()  # New line after printing the elements
    return count

# Example usage:
my_list = [1, 2, 3, 4]
x = len(my_list)
print("Number of elements printed:", safe_print_list(my_list, x))
