#!/usr/bin/python3
"""module text indentation"""


def text_indentation(text):
    """function to print a string"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for letter in text:
        if letter == "." or letter == "?" or letter == ":":
            print("\n\n")
        print("{:s}".format(letter), end="")
