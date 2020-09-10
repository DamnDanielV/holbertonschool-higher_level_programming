#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for sort_k in sorted([key for key in a_dictionary]):
        print("{}: {}".format(sort_k, a_dictionary.get(sort_k)))
