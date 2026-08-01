#!/usr/bin/python3
"""Module that contains safe_print_division function."""


def safe_print_division(a, b):
    """Divide 2 integers and print the result in finally block.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float or None: The result of division, or None if b is 0.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
