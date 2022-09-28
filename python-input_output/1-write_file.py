#!/usr/bin/python3
"""Commentaire de module"""


def write_file(filename="", text=""):
    """Commentaire de méthode"""

    with open(filename, mode="w", encoding='utf-8') as a_file:
        return a_file.write(text)
