#!/usr/bin/python3
"""module of a class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle that inherets from BaseGeometry"""
    def __init__(self, width, height):
        """initializes a new object of class Rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method to calculates area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """return an specification of rectangle"""
        return ("[{}] {}/{}".format("Rectangle",
                self.__width, self.__height))


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """iniatilizes a object class Rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
