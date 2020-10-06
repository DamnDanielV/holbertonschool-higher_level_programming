#!/usr/bin/python3
"""module is same class"""


def is_same_class(obj, a_class):
    """the obj isinstance of a_class ?"""
    return (True if (type(obj) == a_class) else False)
