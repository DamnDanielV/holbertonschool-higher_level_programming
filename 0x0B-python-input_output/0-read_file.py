#!/usr/bin/python3


def read_file(filename=""):
    """reads a file"""
    with open(filename, "r") as f:
        print("".join(f.readlines()), end="")
