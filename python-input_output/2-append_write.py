#!/usr/bin/python3
"""Commentaire de module"""


def append_write(filename="", text=""):
    """Commentaire de méthode"""

    with open(filename, mode="a", encoding='utf-8') as a_file:
        return a_file.write(text)
