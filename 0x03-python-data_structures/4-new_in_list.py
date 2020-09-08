#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listb = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return listb
    else:
        listb[idx] = element
        return listb
