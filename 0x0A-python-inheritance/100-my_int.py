#!/usr/bin/python3
"""module MyInt"""


class MyInt(int):
    """class rebel MyInt"""
    def __ne__(self, other):
        return (int(self) == int(other))

    def __eq__(self, other):
        return (int(self) != int(other))
