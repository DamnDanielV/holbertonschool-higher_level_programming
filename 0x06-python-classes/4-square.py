#!/usr/bin/python3
""" Square Module """


class Square:
    """ This is a docstring of Square Class """
    def __init__(self, size=0):
        """ defining the size of square """
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size >= 0:
        self.__size = size
            else:
                raise ValueError("size must be >= 0")

    def area(self):
        """ area of a square """
        ar = self.__size ** 2
        return ar

    @property
    def size(self):
        """ size variable of Square class instance """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size variable of Square class instance """
        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
