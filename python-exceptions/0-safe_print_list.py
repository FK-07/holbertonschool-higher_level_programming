#!/usr/bin/python3
"""Module that contains safe_print_list function."""


def safe_print_list(my_list=[], x=0):
    """Print x elements of a list safely.

    Args:
        my_list (list): The list containing elements to print.
        x (int): The number of elements to print.

    Returns:
        int: The real number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
