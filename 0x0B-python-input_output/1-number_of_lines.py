#!/usr/bin/python3
    """module number of lines
    """


def number_of_lines(filename=""):
    """function number of lines

    Args:
        filename (str)"".

    Returns:
        [int]: [count of lines]
    """
    c = 0
    with open(filename) as f:
        for line in f:
            c += 1
    return c
