#!/usr/bin/python3
"""commentaire principal"""


class Square:
    """commentaire de classe"""

    def __init__(self, size=0):
        """commentaire d'instance"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size