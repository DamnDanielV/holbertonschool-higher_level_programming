#!/usr/bin/python3
"""module read n lines"""


def read_lines(filename="", nb_lines=0):
    """read a given number of lines of a text file"""
    if nb_lines < 0:
        nb_lines = 0
    with open(filename, mode="r", encoding="utf-8") as f:
        for c, line in enumerate(f):
            if nb_lines == c and nb_lines:
                break
            print(line, end="")
        f.close()
