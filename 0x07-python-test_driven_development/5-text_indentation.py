#!/usr/bin/python3
"""module text indentation"""


def text_indentation(text):
    """ removes some characters"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for c in ['.', '?', ':']:
        text = text.replace(c, c + '\n\n')
    st_n = [line.strip() for line in text.split('\n')]
    st_n = '\n'.join(st_n)
    print(st_n, end='')
