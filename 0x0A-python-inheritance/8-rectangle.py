#!/usr/bin/python3
"""module of a class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry without area"""
    def area(self):
        """public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates a value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class rectangle that inherets from BaseGeometry"""
    def __init__(self, width, height):
        """initializes a new object of class Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
