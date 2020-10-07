#!/usr/bin/python3
"""documentacion"""

def read_file(filename=""):
    """reads a file"""
    with open(filename, 'r') as f:
        print(f.readlines(), end="")
