#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Instantiation of width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to returns area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """method to returns perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))
