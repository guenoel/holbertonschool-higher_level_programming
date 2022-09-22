#!/usr/bin/python3
"""Module d affichage des formes"""


def print_square(size):
    """fonction qui affiche des carrés avec des dièzes"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()
