#!/usr/bin/python3
"""last 10 commits of a repo"""
from requests import get
from sys import argv


def commits_github(repo, owner):
    """makes a request to github"""
    url = ('https://api.github.com/repos/{}/{}/commits'.format(owner, repo))
    res = get(url)
    js = res.json()
    for i in range(10):
        co = js[i]
        sha = co.get('sha')
        author = co.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, author))


if __name__ == '__main__':
    commits_github(argv[1], argv[2])
