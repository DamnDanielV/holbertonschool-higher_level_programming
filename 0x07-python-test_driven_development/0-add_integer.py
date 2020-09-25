#!/usr/bin/python3
"""
Module for add integers
"""


def add_integer(a, b=98):
    """function to return a + b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
