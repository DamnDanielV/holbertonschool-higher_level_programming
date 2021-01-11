#!/usr/bin/python3
"""I love Javascript object notation!!!"""
from requests import post
from sys import argv


def req_params(url, user):
    """makes a post request"""
    params = {'q': user}
    res = post(url, params)
    try:
        if not res.json():
            print("No result")
        else:
            print("[{}] {}".format(res.json()['id'], res.json()['name']))
    except Exception:
        print("Not a valid JSON")


if __name__ == '__main__':
    url = "http://f1b12c907bf7.87bf5168.hbtn-cod.io:5000/search_user"
    if len(argv) == 1:
        req_params(url, "")
    else:
        req_params(url, argv[1])
