#!/usr/bin/python3
"""makes a POST request"""
from requests import post
from sys import argv


def req_post(url, email):
    """makes a post request with a parameter email"""
    params = {'email': email}
    res = post(url, params)
    print("{}".format(res.text))


if __name__ == '__main__':
    req_post(argv[1], argv[2])
