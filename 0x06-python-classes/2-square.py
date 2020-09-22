#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size >= 0:
                self.__zize = size
            else:
                raise ValueError("size must be >= 0")
