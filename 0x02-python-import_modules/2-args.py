#!/usr/bin/python3
from sys import argv


def main():
    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))


if __name__ == "__main__":
    main()
