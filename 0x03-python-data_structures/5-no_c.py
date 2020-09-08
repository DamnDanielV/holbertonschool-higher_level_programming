#!/usr/bin/python3
def no_c(my_string):
    my_string = ''.join(letter for letter in my_string if letter not in 'cC')
    return my_string
