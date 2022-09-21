#!/usr/bin/python3
"""Module de fonctions mathématiques"""


def add_integer(a, b=98):
    """function that add two variables"""

    if b is None or type(b) is not int and type(b) is not float or b != b:
        raise TypeError("b must be an integer")
    elif a is None or type(a) is not int and type(a) is not float or a != a:
        raise TypeError("a must be an integer")
    else:
        return int(a + b)
