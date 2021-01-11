#!/usr/bin/python3
"""using Github API"""
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv


def api_github(user, pas):
    """makes a request to github api"""
    url = 'https://api.github.com/user'
    res = get(url, auth=HTTPBasicAuth(user, pas))
    try:
        print(res.json()['id'])
    except Exception:
        print("None")


if __name__ == '__main__':
    api_github(argv[1], argv[2])
