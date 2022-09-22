#!/usr/bin/python3
"""Module d affichage de string"""


def say_my_name(first_name, last_name=""):
    """fonction qui affiche le nom"""

    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str or last_name is None:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))

