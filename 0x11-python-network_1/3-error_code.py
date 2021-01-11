#!/usr/bin/python3
"""sen a request and handled exceptions"""
import urllib.request as req
import urllib.error as err
from sys import argv


def request_error(url):
    """makes a request a handled errors"""
    request = req.Request(url)
    try:
        with req.urlopen(request) as res:
            print(res.read().decode("utf-8"))
    except err.URLError as error:
        print("Error code: {}".format(error.code))


if __name__ == '__main__':
    request_error(argv[1])
