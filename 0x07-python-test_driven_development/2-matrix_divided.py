#!/usr/bin/python3
"""
Module matriz divided
"""


def matrix_divided(matrix, div):
    """function to divide a matriz"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    len_fi = len(matrix[0])
    n_m = []
    for fila in (matrix):
        new_f = []
        if len_fi != len(fila):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(fila)):
            if not isinstance(fila[j], (int, float)):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
            new_f.append(round((fila[j] / div), 2))
        n_m.append(new_f)
    return n_m
