#!/usr/bin/python3
"""Module that contains list_division function."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element 2 lists.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        list: A new list of length list_length containing division results.
    """
    new_list = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div)
    return new_list
