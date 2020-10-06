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
