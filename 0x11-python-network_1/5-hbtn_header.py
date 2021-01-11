#!/usr/bin/python3
"""send a request an shows a header"""
from requests import get
from sys import argv


def request_val(url):
    """makes a request and shows a header"""
    res = get(url)
    print("{}".format(res.headers.get("X-Request-Id")))


if __name__ == '__main__':
    request_val(argv[1])
