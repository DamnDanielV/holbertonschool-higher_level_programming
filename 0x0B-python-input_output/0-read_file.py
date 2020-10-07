#!/usr/bin/python3
"""documentacion kaffadf"""

def read_file(filename=""):
    """reads a file"""
    with open(filename, 'r') as f:
        print(f.read(), end="")
