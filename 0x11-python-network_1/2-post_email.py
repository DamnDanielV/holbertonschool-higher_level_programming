#!/usr/bin/python3
"""script that send a POST request"""
import urllib.request as req
import urllib.parse as parse
from sys import argv


def request_param(url, email):
    """sen a POST request"""
    params = {'email': email}
    data = parse.urlencode(params).encode('ascii')
    request = req.Request(url, data)
    with req.urlopen(request) as res:
        print("Your email is: {}".format(res.read().decode("utf-8")))


if __name__ == '__main__':
    request_param(argv[1], argv[2])
