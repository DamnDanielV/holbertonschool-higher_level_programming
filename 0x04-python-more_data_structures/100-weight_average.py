#!/usr/bin/python3
def weight_average(my_list=[]):
    sum, elem = 0, 0
    for i, j in my_list:
        sum += i * j
        elem += j
    return (sum / elem)
