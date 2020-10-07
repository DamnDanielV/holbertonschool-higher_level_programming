#!/usr/bin/python3


def read_file(filename=""):
    """reads a file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print("".join(f.readlines()), end="")
        f.close()
