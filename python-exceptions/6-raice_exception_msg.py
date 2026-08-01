#!/usr/bin/python3
"""Module that contains raise_exception_msg function."""


def raise_exception_msg(message=""):
    """Raise a NameError exception with a message.

    Args:
        message (str): The message to be passed to the exception.
    """
    raise NameError(message)
