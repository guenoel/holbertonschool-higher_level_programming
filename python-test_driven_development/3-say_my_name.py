#!/usr/bin/python3
"""Module d affichage de string"""

import string

def say_my_name(first_name, last_name=""):
    """fonction qui affiche le nom"""

    if type(first_name) is str:
        print("My name is {} {}".format(first_name, last_name))
    else:
        raise TypeError("first_name must be a string")