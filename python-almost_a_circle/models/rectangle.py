#!/usr/bin/python3
"""Commentaire de module"""

from models.base import Base


class Rectangle(Base):
    """class rectangle that create nice rectangles"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function that return area of a rectangle"""
        return self.__height * self.__width

    def display(self):
        """Function that display rectangle with '#' character"""
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for b in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Method that update attributes of rectangle"""
        if args and len(args):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            # for i in kwargs
            # exec("%s = %d" % ("self." + i, kwargs[i]))
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary representation of the Rectangle attributes"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
