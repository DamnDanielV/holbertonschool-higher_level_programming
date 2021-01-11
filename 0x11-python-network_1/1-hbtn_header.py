#!/usr/bin/python3
"""script that takes an url and shows a header"""
import urllib.request as req
from sys import argv


def main_request(url):
    """takes an url an shows a header"""
    with req.urlopen(url) as res:
        headers = res.info()
    print("{}".format(headers.get("X-Request-Id")))


if __name__ == '__main__':
    main_request(argv[1])
