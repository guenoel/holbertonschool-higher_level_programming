#!/usr/bin/python3
"""module - no comments"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """classe carré"""

    def __init__(self, size):
        """instanciation d un objet"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """compute area of the rectangle"""

        return self.__size * 2

    def __str__(self):
        """formated string"""

        return super().__str__()
