#!/usr/bin/python3
"""module of a class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle that inherets from BaseGeometry"""
    def __init__(self, width, height):
        """initializes a new object of class Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
