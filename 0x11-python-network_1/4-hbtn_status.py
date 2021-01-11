#!/usr/bin/python3
"""script that fetchs a url"""
from requests import get


def request_d():
    """request data from an url"""
    res = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(type(res.text), res.text))


if __name__ == '__main__':
    request_d()
