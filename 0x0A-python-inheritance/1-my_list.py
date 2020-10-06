#!/usr/bin/python3
"""My list mdule"""


class MyList(list):
    """class MyList to print a sorted a list"""
    def print_sorted(self):
        """sorts a list"""
        print(sorted(self))
