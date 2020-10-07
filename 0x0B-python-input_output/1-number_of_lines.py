#!/usr/bin/python3


def number_of_lines(filename=""):
    c = 0
    with open(filename) as f:
        for line in f:
            c = c + 1
        f.close()
    return c
