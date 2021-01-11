#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import urllib.request as req


def main_request(url):
    """makes a request"""
    with req.urlopen(url) as res:
        r = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
    print("\t- utf8 content: {}".format(r.decode('utf8')))


if __name__ == '__main__':
    main_request("https://intranet.hbtn.io/status")
