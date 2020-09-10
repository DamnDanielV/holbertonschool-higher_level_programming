#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return[[m2[i] ** 2 for i in range(len(m2))] for m2 in matrix]
