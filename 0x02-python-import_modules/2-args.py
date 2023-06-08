#!/usr/bin/python3
from sys import argv


def main():
    length = len(argv)
    print("{:d} arguments.".format(length - 1) if length == 1
          else "{:d} argument:".format(length - 1) if length == 2
          else "{:d} arguments:".format(length - 1))
    for i in range(1, length):
        print("{:d}: {:s}".format(i, argv[i]))


if __name__ == "__main__":
    main()
