#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is not str or len(roman_string) == 0):
        return 0
    n = 0
    m = 0
    conv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for numr in roman_string:
        for key, val in conv.items():
            if key == numr:
                if m < val:
                    n -= (m * 2)
                n += val
                m = val
    return n
