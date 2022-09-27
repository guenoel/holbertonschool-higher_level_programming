#!/usr/bin/python3
"""module - no comments"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """czdcczdc"""

    def __init__(self, width, height):
        """si c'est pas validé comme int: une except est levée et pas d init
        sinon intanciation se fera"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """compute area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """formated string"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
