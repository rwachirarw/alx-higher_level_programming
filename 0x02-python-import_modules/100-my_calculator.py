#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    length = len(argv)
    if (length != 4):
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    if (argv[2] not in ['+', '-', '*', '/']):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if (argv[2] == '+'):
            result = add(int(argv[1]), int(argv[3]))
        elif (argv[2] == '-'):
            result = sub(int(argv[1]), int(argv[3]))
        elif (argv[2] == '*'):
            result = mul(int(argv[1]), int(argv[3]))
        else:
            result = div(int(argv[1]), int(argv[3]))
        print("{:d} {} {:d} = {:d}".format(int(argv[1]), argv[2],
              int(argv[3]), result))


if __name__ == "__main__":
    main()
