#!/usr/bin/python3
"""Commentaire de module"""


def read_file(filename=""):
    """Commentaire de méthode"""

    with open(filename, mode="r", encoding='utf-8') as a_file:
        print(a_file.read(), end='')
    a_file.closed
