#!/usr/bin/python3
from sys import argv


def main():
    sum = 0
    for i in range(1, len(argv)):
        sum += int(argv[i])
    print("{:d}".format(sum))


if __name__ == "__main__":
    main()
