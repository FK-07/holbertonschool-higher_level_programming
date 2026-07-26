#!/usr/bin/python3
""" Module that converts a Roman numeral to an integer """


def roman_to_int(roman_string):
    """ Converts a roman numeral string to integer """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        cur = roman_dict.get(roman_string[i], 0)
        nxt = roman_dict.get(roman_string[i + 1], 0) if i < length - 1 else 0

        if cur < nxt:
            total -= cur
        else:
            total += cur

    return total