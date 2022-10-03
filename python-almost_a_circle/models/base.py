#!/usr/bin/python3
"""Commentaire de module"""


class Base:
    """Class base ... no comments"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
