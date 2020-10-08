#!/usr/bin/python3
"""module pascal"""


def pascal_triangle(n):
    """creates a pascal triangle"""
    if n <= 0:
        return list()
    n_start = 1
    pascal = [[n_start]]
    for c1 in range(1, n):
        aux = [n_start]
        for c2 in range(1, c1):
            aux.append(pascal[c1 - 1][c2 - 1] + pascal[c1 - 1][c2])
        aux.append(n_start)
        pascal.append(aux)
    return pascal
