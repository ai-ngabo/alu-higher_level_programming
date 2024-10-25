#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements, pad with zeros if necessary
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Extract the first two elements of each tuple and add them
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
