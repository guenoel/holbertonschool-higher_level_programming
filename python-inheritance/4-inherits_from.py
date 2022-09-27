#!/usr/bin/python3
"""module - no comments"""


def inherits_from(obj, a_class):
    """fonction qui verifie si l'objet est une instance 
    d une classe qui est heritée de la classe donnée"""

    return isinstance(obj, a_class) and type(obj) != a_class
