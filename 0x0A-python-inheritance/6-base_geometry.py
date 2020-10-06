#!/usr/bin/python3
"""module of a class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry without area"""
    def area(self):
        """public instance method that raises an exception"""
        raise Exception("area() is not implemented")
