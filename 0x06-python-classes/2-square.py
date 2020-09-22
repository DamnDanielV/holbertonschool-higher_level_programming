#!/usr/bin/python3
""" Square Module """


class Square:
    """ This is the docstring of Square Class """
    def __init__(self, size=0):
        """ defining the size of square """
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
