#!/usr/bin/python3
"""sends a requests and displays the response"""
from requests import get
from sys import argv


def request_error(url):
    """makes a request and handled errors"""
    res = get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)


if __name__ == '__main__':
    request_error(argv[1])
