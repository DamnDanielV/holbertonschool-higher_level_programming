#!/usr/bin/python3
"""modules write a file"""


def write_file(filename="", text=""):
    """writes a file text"""
    ch_wr = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        ch_wr += f.write(text)
        f.close()
    return ch_wr
