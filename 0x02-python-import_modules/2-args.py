#!/usr/bin/python3
from sys import argv
def main():
    args = len(argv) - 1
    i = 1
    if not args:
        print("0 arguments.")
    elif args == 1:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(args))
        for arg in argv[1:]:
            print("{}: {}".format(i, arg))
            i = i +1
if __name__ == '__main__':
    main()