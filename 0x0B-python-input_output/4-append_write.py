#!/usr/bin/python3


def append_write(filename="", text=""):
    ch_w = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        ch_w += f.write(text)
        f.close()
    return ch_w
