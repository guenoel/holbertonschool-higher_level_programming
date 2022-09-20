#!/usr/bin/python3
"""Module de fonctions mathématiques"""


def add_integer(a, b=98):
    """Function that add 2 variables"""

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    else:
        return int(a + b)