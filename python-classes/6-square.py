#!/usr/bin/python3
"""commentaire principal"""


class Square:
    """commentaire de classe"""

    def __init__(self, size=0, position=(0, 0)):
        """commentaire d'instance"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if position:
            self.position = position

    def area(self):
        """calcul de l aire"""

        return int(self.__size) ** 2

    @property
    def size(self):
        """getter for size"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""

        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")


    @property
    def position(self):
        """getter for position"""

        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""

        if type(value) is tuple and len(value) == 2 and type(value[0]) is int and value[0] >= 0 and type(value[1]) is int and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """print square with #"""
        if self.position[1] > 0:
    	    print()
        for i in range(self.size):
            for p in range(self.position[0]):
                print(" ", end='')
            for j in range(self.size):
                print("#", end='')
            print()
        if self.size == 0:
            print()
