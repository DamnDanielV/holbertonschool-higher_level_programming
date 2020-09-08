#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        t_p =(0, None)
    else:
        t_p =(len(sentence), sentence[0])
    return t_p
