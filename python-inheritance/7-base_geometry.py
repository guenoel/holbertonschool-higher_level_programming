#!/usr/bin/python3
"""module - no comments"""


class BaseGeometry:
    """classe basegeometry"""

    def area(self):
        """commentaire de méthode qui leve une exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """commentaire de méthode"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
