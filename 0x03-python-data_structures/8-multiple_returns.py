#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        t_p =(None, 0)
    else:
        t_p =(len(sentence), sentence[0])
    return t_p
