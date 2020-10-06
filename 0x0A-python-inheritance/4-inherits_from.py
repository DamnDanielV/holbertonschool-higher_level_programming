#!/usr/bin/python3
"""check if an object is a specified class"""


def inherits_from(obj, a_class):
    """checks if an object is a subclass of a specified class"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
