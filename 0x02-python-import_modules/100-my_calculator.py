#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    if len(argv) != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)

    dic_oper = {'+': add, '-': sub, '*': mul, '/': div}
    a = int(argv[1])
    b = int(argv[3])
    sel = argv[2]

    for op in dic_oper:
        if op == sel:
            res = dic_oper[op](a, b)
            print('{:d} {:} {:d} = {:d}'.format(a, op, b, res))
            exit(0)

    print('Unknown operator. Available operators: +, -, * and /')
    exit(1)

if __name__ == '__main__':
    main()