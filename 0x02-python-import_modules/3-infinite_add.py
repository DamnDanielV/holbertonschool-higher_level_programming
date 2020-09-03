#!/usr/bin/python3
from sys import argv
def main():
    su = 0
    for args in argv[1:]:
        su += int(args)
    print("{:d}".format(su))
if __name__ == '__main__':
    main()

