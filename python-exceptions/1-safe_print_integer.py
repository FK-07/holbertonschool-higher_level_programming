#!/usr/bin/python3
"""Module that contains safe_print_integer function."""


def safe_print_integer(value):
    """Print an integer with {:d}.format().

    Args:
        value: The value to print (can be of any type).

    Returns:
        bool: True if value was correctly printed (is integer),
              False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
