#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    n = {ke: val for ke, val in a_dictionary.items() if val == value}
    for key in n:
        a_dictionary.pop(key)
    return a_dictionary
