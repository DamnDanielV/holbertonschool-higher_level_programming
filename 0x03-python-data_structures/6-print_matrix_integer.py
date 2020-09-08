#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        ex = ''
        for column in row:
            ex += "{:d} ".format(column)
        print(ex[:-1])
