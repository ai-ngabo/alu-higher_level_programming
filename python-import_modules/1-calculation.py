#!/usr/bin/python3
def add(a, b):
    """My addition function
    Args:
        a: first integer
        b: second integer
    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function
    Args:
        a: first integer
        b: second integer
    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function
    Args:
        a: first integer
        b: second integer
    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function
    Args:
        a: first integer
        b: second integer
    Returns:
        The return value. a / b
    """
    return int(a / b)


from calculator_1 import add, sub, mul, div
a = 10
b = 5


print("{} + {} = {}".format(a, b, result_add))
print("{} - {} = {}".format(a, b, result_sub))
print("{} * {} = {}".format(a, b, result_mul))
print("{} / {} = {}".format(a, b, result_div))
